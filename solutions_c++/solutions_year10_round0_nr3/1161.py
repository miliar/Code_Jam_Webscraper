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

int R, k, n;
LL g[1024];
LL c[1024];
int nxt[1024];

void sol()
{
	FOR(a,0,n-1)
	{
		LL s=0;
		FOR(b,0,n)
		{
			if (s+g[(a+b)%n]>k || b==n)
			{
				c[a]=s;
				nxt[a]=(a+b)%n;
				break;
			}
			s+=g[(a+b)%n];
		}
	}

	int i=0;
	unsigned long long ans=0;
	FOR(a,1,R)
	{
		ans+=c[i];
		i=nxt[i];
	}

	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	FOR(a,1,t)
	{
		cerr << a << "\n";
		cin >> R >> k >> n;
		FOR(b,0,n-1) cin >> g[b];
		cout << "Case #" << a << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}