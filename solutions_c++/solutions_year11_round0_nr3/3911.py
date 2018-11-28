//Compiled using Visual Studio C++ 2010 Express - Version 10.0.30319.1 RTMRel
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
//#include <bitset>

using namespace std;

typedef vector<int> IVECTOR;
typedef vector<int>::iterator IVECTOR_ITR;
typedef vector<char> CVECTOR;
typedef vector<float> FVECTOR;
typedef vector<string> SVECTOR;
typedef vector<long long> LLVECTOR;

typedef map<int,int> IIMAP;
typedef map<int,string> ISMAP;
typedef map<string,string> SSMAP;
typedef map<string,int> SIMAP;


#define FOR(i,a,n) for (int i=a;i<n;i++)
#define FORN(i,a,n) for (int i=n-1;i>=a;i--)


#define FOR1(i,a,n) for (int i=a;i<=n;i++)
#define FOR1N(i,a,n) for (int i=n;i>a;i--)

void printcase (int n, int sum)
{
	if (sum)
	{
		printf("Case #%d: %d\n",n,sum);
	}
	else
	{
		printf("Case #%d: NO\n",n);
	}
}


int main (int argv, char* argc[])
{
	freopen("in.txt","r+",stdin);
	freopen("out.txt","w+",stdout);

	int t = 0;
	scanf("%d",&t);

	FOR(i,0,t)
	{
		int n;
		cin >> n;

		LLVECTOR intarray;
		long long ixorsum = 0, isum=0;
		FOR (j,0,n)
		{
			long long temp;
			cin >> temp;

			ixorsum ^= temp;
			isum += temp;
			intarray.push_back(temp);			
		}

		if (!ixorsum)
		{
			sort(intarray.begin(),intarray.end());

			isum -= intarray[0];
		}
		else
		{
			isum = 0;
		}
		
		printcase(i+1,isum);

	}


	fclose(stdin);
	fclose(stdout);
}