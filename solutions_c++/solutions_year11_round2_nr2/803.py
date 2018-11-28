// gcgb.cpp : Defines the entry point for the console application.
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

double eps = 0.000000000001;
vector<PII> a;
int n;
double d;

int test(double t)
{
	double p=-100000000;
	rep(i,n)
	{
		double nt=(a[i].Y-1)*d/2.0;
		if (nt-t>eps) return 0;
		double pos=a[i].X-nt;		
		double zal=t-nt;
		double left=pos-zal;
		double right=pos+zal;

		if (pos-p>eps)  //p<pos
		{
			p=max(p,left);
			p+=d*a[i].Y;
		} else
		{
			if (p>right) return 0;
			p+=d*a[i].Y;
		}
	}

	return 1;

	

}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen ("b.in","r",stdin);
	freopen ("b.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testnum=0; testnum<testcase; testnum++)
	{
		printf("Case #%d: ",testnum+1);
		int t;
		scanf("%d %d",&n,&t);
		d=t;
		a.clear();
		
		rep(i,n)
		{
			PII t;
			scanf("%d %d\n",&t.X,&t.Y);
			a.push_back(t);			
		}
		sort(a.begin(), a.end());
		double good = 1000010.0;
		double bad =0;
		while (good-bad>eps)
		{
			double midl=(bad+good)/2;
			if (test(midl)) good=midl;
			else bad=midl;
		}
		printf("%.9f\n",good);



	
		
	}
	return 0;
}

