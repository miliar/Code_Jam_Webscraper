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

char T[512][512];
LL Z[512][512];
LL sumX[512][512];
LL sumY[512][512];
LL sum[512][512];
int n, m, d;

void sol()
{
	FOR(a,1,n) FOR(b,1,m)
	{
		Z[a][b] = (LL)(int(T[a][b]-'0')+d);
		sum[a][b] = sum[a-1][b]+sum[a][b-1]-sum[a-1][b-1]+Z[a][b];
		sumX[a][b] = sumX[a-1][b]+sumX[a][b-1]-sumX[a-1][b-1]+Z[a][b]*(LL)a;
		sumY[a][b] = sumY[a-1][b]+sumY[a][b-1]-sumY[a-1][b-1]+Z[a][b]*(LL)b;
	}
	DFOR(k,min(n,m),3)
		FOR(a,1,n-k+1)
			FOR(b,1,m-k+1)
			{
				LL s = sum[a+k-1][b+k-1]-sum[a-1][b+k-1]-sum[a+k-1][b-1]+sum[a-1][b-1]
					- (Z[a][b] + Z[a+k-1][b] + Z[a][b+k-1] + Z[a+k-1][b+k-1]);
				LL sX = sumX[a+k-1][b+k-1]-sumX[a-1][b+k-1]-sumX[a+k-1][b-1]+sumX[a-1][b-1]
					- (Z[a][b]*(LL)a + Z[a+k-1][b]*(LL)(a+k-1) +
						Z[a][b+k-1]*(LL)a + Z[a+k-1][b+k-1]*(LL)(a+k-1));
				LL sY = sumY[a+k-1][b+k-1]-sumY[a-1][b+k-1]-sumY[a+k-1][b-1]+sumY[a-1][b-1]
					- (Z[a][b]*(LL)b + Z[a+k-1][b]*(LL)b +
						Z[a][b+k-1]*(LL)(b+k-1) + Z[a+k-1][b+k-1]*(LL)(b+k-1));
				if (sX*(LL)2 == (LL)(a+a+k-1)*s && sY*(LL)2 == (LL)(b+b+k-1)*s)
				{
					cout << k;// << " " << a << " " << b;
					return;
				}
			}
	cout << "IMPOSSIBLE";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Tests;
	cin >> Tests;
	FOR(z,1,Tests)
	{
		RE("%d%d%d", &n, &m, &d);
		gets(&T[0][0]);
		FOR(a,1,n) gets(&T[a][1]);
		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}