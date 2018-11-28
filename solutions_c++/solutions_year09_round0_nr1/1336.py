// ggl1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
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



string dic[5200];
int k,tc,len;
int p[2][5200];
int var[30];

int calc(string st)
{
	int kil=len;
	rep(i,len) p[0][i]=i;
	int ind=0;
	rep(i,27) var[i]=-1;
	rep(i,k)
	{
		if (st[ind]=='(')
		{
			ind++;
			while (st[ind]!=')') var[ st[ind]-'a' ]=i,ind++;
		} var[ st[ind]-'a' ]=i;
		ind++;
		int k1=0;
		rep(j,kil)
		{
			int v=p[i%2][j];
			if ( var[ dic[v][i]-'a' ]==i) p[1-i%2][k1++]=v;
		}
		kil=k1;
	}
	return kil;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d %d %d",&k,&len,&tc);
	getchar();
	char temp[520];
	rep(i,len)
	{
		gets(temp);
		dic[i]=string(temp);
	}

	rep(i,tc)
	{
		gets(temp);
		printf("Case #%d: %d\n",i+1,calc( string(temp) ));
	}

	
	
	return 0;
}

