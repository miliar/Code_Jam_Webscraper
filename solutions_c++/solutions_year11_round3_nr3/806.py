// gcj_3.cpp : Defines the entry point for the console application.
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

int a[10000];
int n,st,fin;

int test(int ch)
{
	rep(i,n)
	{
		if (a[i]%ch!=0 && ch%a[i]!=0) return 0;
	}
	return 1;

}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen ("c.in","r",stdin);
	freopen ("c.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testnum=0; testnum<testcase; testnum++)
	{
		printf("Case #%d: ",testnum+1);
		int t;
		scanf("%d %d %d",&n,&st,&fin);
		rep(i,n) scanf("%d",&a[i]);
		int f=0;
		for(int i=st; i<=fin; i++)
		{
			if (test(i)) {f=i; break;}
		}

		if (f) printf("%d\n",f);
		else printf("NO\n");



	
		
	}
	return 0;
}

