#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n;
int nxt[2048];
int ans[2048];

void dfs( int i, int j, int k )
{
	if (i==j) return;

	FOR(a,i,j-1) if (nxt[a]==j)
	{
		int zz = ( (LL)ans[k]*(k-j) - (LL)(ans[k]-ans[j])*(k-a) - 1 ) / (LL)(k-j);
		int ii = i;
		FOR(b,i,j-1) if (nxt[b]==j)
		{
			ans[b] = zz;
			dfs( ii, b, j );
			ii = b+1;
		}
		return;
	}
}

void sol()
{
	FOR(a,1,n-1) FOR(b,a+1,n-1)
		if (b < nxt[a] && nxt[b] > nxt[a])
		{
			cout << " Impossible";
			return;
		}

	CLR(ans);
	int Z = o_O;
	ans[n] = Z;
	int i=1;
	FOR(a,1,n-1) if (nxt[a]==n)
	{
		ans[a] = Z-1;
		dfs(i,a,n);
		i=a+1;
	}

	FOR(a,1,n) WR(" %d", ans[a]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	RE("%d", &t);
	FOR(z,1,t)
	{
		cerr << z << "\n";
		RE("%d", &n);
		FOR(a,1,n-1) RE("%d", &nxt[a]);

		cout << "Case #" << z << ":";
		sol();
		cout << "\n";
	}

	return 0;
}
