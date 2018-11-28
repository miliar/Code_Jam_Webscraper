#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define PATH "/home/tushar/Desktop/"
#define INPUTFILE PATH "C-large.in"
#define OUTPUTFILE PATH "C-large.out"
using namespace std;

int G[1000],V[1000],M[1000];

int main()
{
	freopen(INPUTFILE,"r",stdin);
	freopen(OUTPUTFILE,"w",stdout);
	int t,R,k,N;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		cin>>R>>k>>N;
		memset(M,-1,sizeof(M));
		for(int j=0;j<N;++j)
			cin>>G[j];
		for(int r=1,a=0;r<=R;++r)
		{
			int sum = 0,m=a;
			for(int b=0;sum+G[a] <= k && b<N;++b,a=(a+1)%N)sum += G[a];
			if(M[m] == a)
				break;
			else
				M[m] = a,V[m] = sum;
			}
		long long val = 0;
		for(int x=0,r=1;r<=R;++r)
		{
			val += V[x];
			x = M[x];
			}
		cout<<"Case #"<<i<<": "<<val<<endl;
		}
	return 0;
	}
