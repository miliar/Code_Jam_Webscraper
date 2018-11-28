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
#define MOD 10007

////////////////////////////////////////////////////////////////////////////////

int t;
int n,m,r,a,b;
int B[1000][1000];

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d %d",&n,&m,&r);
            REP(i,n) REP(j,m) B[i][j] = 0;
            REP(i,r)
            {
                  scanf("%d %d",&a,&b);a--,b--;
                  B[a][b] = -1;
            }
            B[0][0] = 1;
            FOR(i,0,n-2) FOR(j,0,m-2) if(B[i][j] != -1)
            {
                  if(i+2<n && j+1<m && B[i+2][j+1]!=-1) B[i+2][j+1] = (B[i+2][j+1]+B[i][j])%MOD;
                  if(i+1<n && j+2<m && B[i+1][j+2]!=-1) B[i+1][j+2] = (B[i+1][j+2]+B[i][j])%MOD;
            }
            printf("Case #%d: %d\n",t2,B[n-1][m-1]);
      }
      return 0;
}
