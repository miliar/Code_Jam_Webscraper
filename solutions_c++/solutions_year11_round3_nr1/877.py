// gcj_1.cpp : Defines the entry point for the console application.
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

char a[200][200];
int n,m;

int change(int i, int j, char ch)
{
	if (i<n && a[i][j]=='#') a[i][j]=ch;
	else return 0;

	return 1;
}

int done()
{
	rep(i,n)
		rep(j,m)
		if (a[i][j]=='#') 
		{
			if (!change(i,j,'/')) return 0;
			if (!change(i,j+1,'\\' )) return 0;
			if (!change(i+1,j,'\\')) return 0;
			if (!change(i+1,j+1,'/')) return 0;
		}
	return 1;
}
int _tmain(int argc, _TCHAR* argv[])
{
	freopen ("a.in","r",stdin);
	freopen ("a.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testnum=0; testnum<testcase; testnum++)
	{
		printf("Case #%d:\n",testnum+1);
		scanf("%d %d\n",&n,&m);
		rep(i,n)
			scanf("%s\n",&a[i]);			
		if (!done()) printf("Impossible\n");
		else 
		{
			rep(i,n)
				printf("%s\n",a[i]);
		}
	
	}
	return 0;
}



