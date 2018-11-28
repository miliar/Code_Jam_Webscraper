// gcg.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
  
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;

int a[120][120];
int k[120];
int n;
double wp[120],owp[120],owwp[120];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen ("a.in","r",stdin);
	freopen ("a.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testnum=0; testnum<testcase; testnum++)
	{
		printf("Case #%d:\n",testnum+1);
		scanf("%d\n",&n);
	//	printf("WP:\n");
		rep(i,n)
		{
			char st[500];
			scanf("%s\n",&st);			
			rep(j,n)
				if (st[j]=='.') a[i][j]=-1;
				else if (st[j]=='0') a[i][j]=0;
				else if (st[j]=='1') a[i][j]=1;
			int kil=0;
			double sum=0.0;
		    rep(j,n)
			if (a[i][j]!=-1) sum+=a[i][j],kil++;
			wp[i]=sum;
			k[i]=kil;
		//	printf("%.7f ",wp[i]/k[i]);
		}
	//	printf("\nOWP:\n");
		rep(i,n)
		{
			
			double sum=0.0;
			rep(j,n) if (a[i][j]!=-1) 
			{
				double r=wp[j];
				if (a[i][j]==0) r-=1;
				sum+=r/(k[j]-1);
			}
			owp[i]=sum;
		//	printf("%.7f ",owp[i]/k[i]);
		}
	//	printf("\nOWWP:\n");
		rep(i,n)
		{
			
			double sum=0.0;
			rep(j,n) if (a[i][j]!=-1) 
			 sum+=owp[j]/k[j];
			owwp[i]=sum;
		//	printf("%.7f ",owwp[i]/k[i]);
		}

		rep(i,n)
		{
			double res=(0.25*wp[i]+0.5*owp[i]+0.25*owwp[i])/k[i];
			printf("%.10f\n",res);
		}



		



	}
	return 0;
}

