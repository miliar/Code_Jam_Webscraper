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

int sol(int A, int B)
{
	char S[10];
	int ans=0;
	int Z[10];
	FOR(a,A,B)
	{
		sprintf(S, "%d", a);
		int n = (int)strlen(S);
		int i = 0;
		FOR(b,1,n-1)
		{
			FOR(c,0,n-2) swap(S[c], S[c+1]);
			if (S[0]!='0')
			{
				int z;
				sscanf(S, "%d", &z);
				if (a < z && z <= B)
					Z[i++] = z;
			}
		}
		sort( Z, Z+i );
		Z[i] = -1;
		FOR(b,0,i-1) if (Z[b]!=Z[b+1]) ans++;
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	RE("%d", &t);

	FOR(a,1,t)
	{
		int A, B;
		RE("%d%d", &A, &B);
		WR("Case #%d: %d\n", a, sol(A, B));
	}

	return 0;
}
