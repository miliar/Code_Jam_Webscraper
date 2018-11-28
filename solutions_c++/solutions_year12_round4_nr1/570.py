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

int n, W;
int D[10010], L[10010];
int mx[10010];

bool sol()
{
	CLR(mx);
	mx[1] = D[1];
	FOR(a,1,n)
	{
		if (W-D[a] <= mx[a]) return true;
		FOR(b,a+1,n) if (D[b] <= D[a]+mx[a])
			mx[b] = max(mx[b], min(D[b]-D[a], L[b]));
	}

	return false;
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
		FOR(a,1,n) RE("%d%d", &D[a], &L[a]);
		RE("%d", &W);

		cout << "Case #" << z << ": ";
		if (sol()) cout << "YES";
		else cout << "NO";
		cout << "\n";
	}

	return 0;
}
