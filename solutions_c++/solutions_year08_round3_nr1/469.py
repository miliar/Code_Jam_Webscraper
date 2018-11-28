#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <bitset>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#define SZ(A) int(A.size())
#define pb push_back
using namespace std;
bool cmp(int a,int b)
{
	return a>b;
}
int main()
{
	int numCases=0,serial=0;
	cin>>numCases;

	while(numCases)
	{
		int P=0,K=0,L=0;
		long long result=0;

		cin>>P>>K>>L;

		vector <int>  frequency(L,0);

		for(int i=0;i<L;i++)
		{
			cin>>frequency[i];
		}

		sort(frequency.begin(),frequency.end(),cmp);

		int mulFactor=1;
		serial++;


		if(L>P*K)
		{
			cout<<"Case #"<<serial<<": "<<"Impossible"<<endl;
		}
		else
		{
			for(int i=0;i<SZ(frequency);i++)
			{
				mulFactor = ceil((i+1)/double(K));
				result = result + mulFactor*frequency[i];
			}
			cout<<"Case #"<<serial<<": "<<result<<endl;
		}
			
		numCases--;
	}
	return 0;
}
