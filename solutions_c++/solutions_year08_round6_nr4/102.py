#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long LL;
const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
const LL MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
#define CMAX(a,b) if(b>a)a=b
#define CMIN(a,b) if(b<a)a=b
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

#define PB push_back
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

typedef pair<int,int> PII;

inline int getNum()
{
    char ch;
    int Res = 0;
    while ( (ch = getchar()) != ' ' && ch != '\n')
       Res = Res * 10 + ch - '0';
    return Res;
}

inline int getNum2()
{
    char ch;
    bool p = 1;
    int Res = 0;
    if((ch = getchar()) == '-')
       p = 0; 
    else
       Res = ch - '0'; 
    while ( (ch = getchar()) != ' ' && ch != '\n')
       Res = Res * 10 + ch - '0';
    return p ? Res : -Res;
}
bool G1[16][16], G2[16][16];
int N, M;
bool used[16];
int prm[16];
bool Check()
{
	int i, j;
	FOR(i, 1, M)
		FOR(j, 1, M)
		   if(G2[i][j])
		   {
			   if(!G1[prm[i]][prm[j]]) return 0;
		   }
  // SHOW1(prm, M + 1);
   return 1;
}

bool DFS(int p)
{
	int i;
	if(p > M)
	{
		return Check();
	}
	else
	{
        FOR(i, 1, N)
		{
			if(!used[i])
			{
				used[i] = 1;
				prm[p] = i;
				if(DFS(p + 1)) return 1;
				used[i] = 0;
			}

		}

	}
	return 0;

}

bool Solve()
{
	MST(used, 0);
	if(DFS(1)) return 1;
	return 0;
}
int main()
{
	int i, j, k, Case, ctr, a, b;
    freopen("D_S2.in", "r", stdin);
    freopen("D_S2.out", "w", stdout);
    scanf("%d", &Case);
    for(ctr = 1; ctr <= Case; ++ctr)
    {
		MST(G1, 0);
		MST(G2, 0);

		scanf("%d", &N);

		for(i = 1; i < N; ++i)
			scanf("%d%d", &a, &b), G1[a][b] = G1[b][a] = 1;
		scanf("%d", &M);
		for(i = 1; i < M; ++i)
			scanf("%d%d", &a, &b), G2[a][b] = G2[b][a] = 1;

		printf("Case #%d: %s\n", ctr, Solve() ? "YES" : "NO");
    }
    //system("pause");
	return 0;
}

