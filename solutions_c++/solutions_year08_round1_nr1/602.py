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
bool cmp(long long i,long long j)
{
	return i>j;	
}
int main()
{
	int noTest=0;
	int serial=0;
	cin>>noTest;

	while(noTest)
	{
		int vecSize=0;
		long long result=0;
		cin>>vecSize;

		vector<long long> vecArr1(vecSize,0);
		vector<long long> vecArr2(vecSize,0);

		serial++;

		for(int i=0;i<vecSize;i++)
		{
			cin>>vecArr1[i];
		}	

		for(int i=0;i<vecSize;i++)
		{
			cin>>vecArr2[i];
		}	
		
		sort(vecArr1.begin(),vecArr1.end());
		sort(vecArr2.begin(),vecArr2.end(),cmp);

		for(int i=0;i<vecSize;i++)
		{
			result = result + (vecArr1[i]*vecArr2[i]);	
		}

		cout<<"Case #"<<serial<<": "<<result<<endl;
		noTest--;
	}
	return 0;
}
