#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<list>
#include<utility>
#include<ctime>
#include<cstdlib>
#include<string>
#include<complex>
#include<algorithm>
using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef long long LL;
typedef unsigned long long LLU;

#define ZUO 1000000000
#define PB push_back 
#define ST first
#define ND second
#define MP make_pair
#define ALL(x) x.begin(),x.end()

char A[100][100];
vector<char> X[100];

int test1(int i, int j, int k,int n)
{
	if(X[i][j]=='.') return 0;
	int istart=i;
	while(i>1&&j>1&&X[i][j]==X[i-1][j-1]) {
		i--;
		j--;
	}
	if (istart-i>=k-1)
		if (X[i][j]=='R')
			return 1;
		else 
			return 2;
	else return 0;
}

int test2(int i, int j, int k,int n)
{
	if(X[i][j]=='.') return 0;
	int istart=i;
	while(i<n&&j>1&&X[i][j]==X[i+1][j-1]) {
		i++;
		j--;
	}
	if (i-istart>=k-1)
		if (X[i][j]=='R')
			return 1;
		else 
			return 2;
	else return 0;
}

int test3(int i, int j, int k,int n)
{
	if(X[i][j]=='.') return 0;
	int jstart=j;
	while(j>1&&X[i][j]==X[i][j-1])
		j--;
	if (jstart-j>=k-1)
		if (X[i][j]=='R')
			return 1;
		else 
			return 2;
	else return 0;
}

int test4(int i, int j, int k,int n)
{
	if(X[i][j]=='.') return 0;
	int istart=i;
	while(i>1&&X[i][j]==X[i-1][j])
		i--;
	if (istart-i>=k-1)
		if (X[i][j]=='R')
			return 1;
		else 
			return 2;
	else return 0;
}

int main()
{
	int z;
	scanf("%d",&z);
	for(int zz=1;zz<=z;zz++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		for(int i=0;i<=n;i++)
		{
			X[i].clear();
		}
		for(int i=1;i<=n;i++)
		{
				scanf("%s",A[i]+1);
		}
		for(int i=1;i<=n;i++)
			for(int j=n;j>=1;j--)
			{
				if(A[i][j]=='.') continue;
				else
				{
					X[i].PB(A[i][j]);
				}
			}
		for(int i=1;i<=n;i++)
		{
			while(X[i].size()<=n) X[i].PB('.');
			reverse(X[i].begin(),X[i].end());
		}
		bool red=false, blue=false;
		int x;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				x=test1(i,j,k,n);
				if(x==1) red=true;
				else
				if(x==2) blue=true;
				x=test2(i,j,k,n);
				if(x==1) red=true;
				else
				if(x==2) blue=true;
				x=test3(i,j,k,n);
				if(x==1) red=true;
				else
				if(x==2) blue=true;
				x=test4(i,j,k,n);
				if(x==1) red=true;
				else
				if(x==2) blue=true;
			}
		printf("Case #%d: ",zz);
		if (red&&blue) printf("Both\n");
		else
		if (red) printf("Red\n");
		else
		if (blue) printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
