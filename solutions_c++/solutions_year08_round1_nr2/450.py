#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
#include "math.h"
using namespace std;
#define MSP 0
#define MS 1
#define NUM 0

#if MSP
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
		int vals;
		ip>>vals;

		vector <int> num1,num2;

		for(int l =0;l<vals;++l)
		{
			int tmp;
			ip>>tmp;
			num1.push_back(tmp);
		}
		for(int j =0;j<vals;++j)
		{
			int tmp;
			ip>>tmp;
			num2.push_back(tmp);
		}
		sort(num1.begin(),num1.end());
		sort(num2.begin(),num2.end());
		long retval = 0;

		for(int k=0;k<vals;++k)
			retval += num1[k]*num2[num2.size()-k-1];
		op<<"Case #"<<i<<": "<<retval<<endl;
	}
	ip.close();
	op.close();
}
#endif

#if NUM
void main()
{
	ifstream ip("C-small-attempt1.in");
	ofstream op("C-small-attempt1.out");

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

	double tmp = sqrt(double(5))+3;
	for(int i=1;i<=N;++i)
	{
		long val,tmpval;
		double vald = 1;
		ip>>val;

		for(int j = 0;j<val; ++j)
		{
			vald *= tmp;
			tmpval = vald;
			tmpval = tmpval % 1000;
			vald = vald - (int)vald + tmpval;
		}
		val = vald;
		val = val % 1000;
		op<<"Case #"<<i<<": ";
		if(val < 100)
			op<<'0';
		if(val < 10)
			op<<'0';
		if(val)
			op<<val<<endl;
		else
			op<<'0'<<endl;
	}
	ip.close();
	op.close();
}
#endif
#if MS
class cust
{
public : 
	int index,malt;
};
void main()
{
	ifstream ip("B-small-attempt0.in");
	ofstream op("B-small-attempt0.out");

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
		int M;
		vector < vector <cust> > cst; 
		vector < vector <int> > allcombo;
		vector < int > allcombomalt;
		ip>>M;

		for(int itr3 = 0;itr3 < pow(double(2),M); ++itr3)
		{
			vector <int> combo;
			int val = itr3;
			int count = 0;
			for(int itr4 = 0; itr4 < M; ++itr4 )
			{
				if(val%2)
					++count;
				combo.push_back(val%2);
				val /= 2;
			}
			reverse(combo.begin(),combo.end());
			allcombo.push_back(combo);
			allcombomalt.push_back(count);
		}
		int T;
		ip>>T;

		for(int j=0;j<T;++j)
		{
			int read;
			ip>>read;
			vector < cust > tmp;

			for(int k=0;k<read;++k)
			{
				cust val;
				int idx,malt;
				ip>>val.index>>val.malt;
				tmp.push_back(val);
			}
			cst.push_back(tmp);
		}
		for(int itr1=0;itr1<allcombo.size();++itr1)
		{
			for(int itr2 = 0;itr2 < cst.size(); ++itr2)
			{
				bool found = false;
				for(int itr5 = 0;itr5<cst[itr2].size();++itr5)
					if(allcombo[itr1][cst[itr2][itr5].index-1] == cst[itr2][itr5].malt)
					{
						found = true;
						break;
					}					
				if(!found)
				{
					allcombomalt[itr1] = M+1;
				}
			}
		}
		int mincount = 0;
		for(int itr6=0;itr6<allcombo.size();++itr6)
			mincount = (allcombomalt[mincount] < allcombomalt[itr6]) ? mincount : itr6;
		op<<"Case #"<<i<<":";
		if(allcombomalt[mincount] == M+1)
			op<<" IMPOSSIBLE"<<endl;
		else
		{
			for(int itr7=0;itr7<allcombo[mincount].size();++itr7)
				op<<" "<<allcombo[mincount][itr7];
			op<<endl;
		}
	}
	ip.close();
	op.close();
}
#endif