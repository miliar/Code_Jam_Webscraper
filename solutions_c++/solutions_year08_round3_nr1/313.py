#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
#include "math.h"
using namespace std;

#define PROBLEM_A 1
#define PROBLEM_B 0
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

	for(int i=1;i<=N;++i)
	{
		op<<"Case #"<<i<<": "<<endl;
	}
	ip.close();
	op.close();
}
#endif
#if PROBLEM_C
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
		op<<"Case #"<<i<<": "<<endl;
	}
	ip.close();
	op.close();
}
#endif
