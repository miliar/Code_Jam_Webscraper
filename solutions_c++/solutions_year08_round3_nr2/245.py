#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
#include "math.h"
using namespace std;

#define PROBLEM_A 0
#define PROBLEM_B 1
#define PROBLEM_C 0

#if PROBLEM_A
void main()
{
	ifstream ip("A-large.in");
	ofstream op("A-large.out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return;
	}

	int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
		long long P,K,L,val;
		vector <long long> freq;
		ip>>P>>K>>L;

		for(long long j=0;j<L;++j)
		{
			ip>>val;
			freq.push_back(val);
		}
		sort(freq.begin(),freq.end());
		reverse(freq.begin(),freq.end());
		long long retval = 0;
		long long curval = 1;
		bool done = true;
		for(long long k=1;k<=L;++k)
		{
			if(curval > P)
			{
				done = false;
				break;
			}
			retval += curval*freq[k-1];
			if(0 == k%K)
				++curval;
		}
		op<<"Case #"<<i<<": ";
		if(done)
			op<<retval<<endl;
		else
			op<<"Impossible"<<endl;
	}
	ip.close();
	op.close();
}
#endif

#if PROBLEM_B
vector <vector <string> > vecop;
long long findnum(string &str,string &op)
{
	long long ret = 0;
	long long cur = 0;
	ret = str[0] - '0';
	for(int i=0;i<op.length();++i)
	{
		switch(op[i])
		{
		case ' ':
			ret *=10;
			ret += str[i+1]-'0';
			break;
		case '+':
			cur = str[i+1]-'0';
			for(int j=i+1;j<op.length()&&op[j] == ' ';++j,++i)
			{
				cur *= 10;
				cur += str[j+1] - '0';
			}
			ret += cur;
			break;
		case '-':
			cur = str[i+1]-'0';
			for(int j=i+1;j<op.length()&&op[j] == ' ';++j,++i)
			{
				cur *= 10;
				cur += str[j+1] - '0';
			}
			ret -= cur;
			break;
		}
	}
	return ret;
}
void findugly(string str,vector <long long> &ugly,int curpos,string &op)
{
	if(curpos == str.length()-1)
	{
		vecop[str.length()].push_back(op);
		long long val = findnum(str,op);
		val = (val < 0 ) ? -val : val;
		if(!val)
			ugly.push_back(val);
		else if(!(val%2))
			ugly.push_back(val);
		else if(!(val%3))
			ugly.push_back(val);
		else if(!(val%5))
			ugly.push_back(val);
		else if(!(val%7))
			ugly.push_back(val);
	}
	else
	{
		op += '+';
		findugly(str,ugly,curpos+1,op);
		op[op.length()-1] = '-';
		findugly(str,ugly,curpos+1,op);
		op[op.length()-1] = ' ';
		findugly(str,ugly,curpos+1,op);
		op.erase(op.begin()+op.length()-1);
	}
}

void main()
{
	ifstream ip("B-small.in");
	ofstream op("B-small.out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return;
	}

	int N;
	ip>>N;

	vector <string> strvec;
	for(int itr = 0; itr < 50;++itr)
		vecop.push_back(strvec);

	for(int i=1;i<=N;++i)
	{
		string str,oper;
		vector<long long> ugly;
		ip>>str;
		if(vecop[str.length()].size())
		{
			for(long long j=0;j<vecop[str.length()].size();++j)
			{
				long long val = findnum(str,vecop[str.length()][j]);
				val = (val < 0 ) ? -val : val;
				if(!val)
					ugly.push_back(val);
				else if(!(val%2))
					ugly.push_back(val);
				else if(!(val%3))
					ugly.push_back(val);
				else if(!(val%5))
					ugly.push_back(val);
				else if(!(val%7))
					ugly.push_back(val);
			}
		}
		else
		{
			findugly(str,ugly,0,oper);
		}
		op<<"Case #"<<i<<": "<<ugly.size()<<endl;
	}
	ip.close();
	op.close();
}
#endif
#if PROBLEM_C
long long findcombo(long long val)
{
	switch(val)
	{
	case 1:
		return 0;
	case 2: 
		return 1;
	default :
		return findcombo(val-1)*val;
	}
}
void main()
{
	ifstream ip("C-small.in");
	ofstream op("C-small.out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return;
	}

	int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
		long long n, m, X, Y , Z;
		vector <long long> limit, marr;
		vector <vector <long long> > all;

		ip>>n>>m>>X>>Y>>Z;
		for(long long j=0;j<m;++j)
		{
			long long val;
			ip>>val;
			marr.push_back(val);
		}
		for (long long k = 0 ;k<n; ++k)
		{
		  limit.push_back(marr[k % m]);
		  marr[k % m] = (X * marr[k % m] + Y * (k + 1)) % Z;
		}
		for(long long l=0;l<limit.size()-1;++l)
		{
			int count = 1;
			marr.clear();
			marr.push_back(limit[l]);
			for(long long itr=l+1;itr<limit.size();++itr)
				if(limit[itr] > marr[marr.size()-1])
					marr.push_back(limit[itr]);
				else if(limit[itr] == marr[marr.size()-1])
					count *= 2;
			for(long long ct=0;ct<count;++ct)
				all.push_back(marr);
		}
		long long retval = limit.size();
		for(int itr1=0;itr1<all.size();++itr1)
			retval += findcombo(all[itr1].size());
		op<<"Case #"<<i<<": "<<retval<<endl;
	}
	ip.close();
	op.close();
}
#endif
