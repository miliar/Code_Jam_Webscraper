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

int W, L;
int n;
int R[16];
int X[16], Y[16];

int big_rand()
{
	return (rand()%1000)*1000000 + (rand()%1000)*1000 + (rand()%1000);
}

bool check()
{
	FOR(a,1,n) FOR(b,a+1,n)
	{
		LL dx = X[a]-X[b];
		LL dy = Y[a]-Y[b];
		LL dr = R[a]+R[b];
		if (dx*dx + dy*dy < dr*dr) return false;
	}
	return true;
}

void sol()
{
	while(1)
	{
		FOR(a,1,n)
		{
			X[a] = big_rand()%(W+1);
			Y[a] = big_rand()%(L+1);
		}
		if (check())
		{
			FOR(a,1,n) WR(" %.2lf %.2lf", (double)X[a], (double)Y[a]);
			return;
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	RE("%d", &t);
	FOR(a,1,t)
	{
		cerr << a << "\n";
		RE("%d%d%d", &n, &W, &L);
		FOR(b,1,n) RE("%d", &R[b]);

		cout << "Case #" << a << ":";
		sol();
		cout << "\n";
	}

	return 0;
}
