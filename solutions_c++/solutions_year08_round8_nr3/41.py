//MADE BY lordmonsoon A.I.
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())

#define MOD 1000000009
////////////////////////////////////////////////////////////////////////////////



int t , n, k , a , b;
vi T[1000];
int C[501][501];

int power(int a,int n,int m)
{
      if(n == 0) return 1;
      else
      {
            long long s = power(a,n>>1,m);
            s *= s;s %= m;
            if(n&1) s = (s * a)%m;
            return s;
      }
}

int inverse(int a,int m)
{
      return power(a,m-2,m);
}

int newton(int n,int k)
{
      long long ret = 1;
      FOR(i,n-k+1,n) ret = (ret * i)%MOD;
//      FOR(i,2,k) ret = (ret * inverse(i,MOD))%MOD;
      return ret;
}

int gogo(int v,int u,int p1)
{
      long long ret = newton(k - p1, SIZE(T[v]) - (u!=v));
      REP(i,SIZE(T[v])) if(T[v][i] != u) ret = (ret * gogo(T[v][i],v,SIZE(T[v])) ) % MOD;
      return ret;     
}

int main()
{
      C[0][0] = C[1][0] = C[1][1] = 1;
      FOR(i,2,500)
      {
            C[i][0] = C[i][i] = 1;
            FOR(j,2,i-1) C[i][j] = (C[i-1][j] + C[i-1][j-1]) % MOD;
      }
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d",&n,&k);
            FOR(i,1,n) T[i].clear();
            REP(i,n-1)
            {
                  scanf("%d %d",&a,&b);
                  T[a].pb(b);
                  T[b].pb(a);
            }
            printf("Case #%d: %d\n",t2,gogo(1,1,0));
      }
      return 0;
}
