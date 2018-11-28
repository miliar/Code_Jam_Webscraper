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


////////////////////////////////////////////////////////////////////////////////

map<string,int> M;
int n,m,t;
int DP[2001][501];
char bufor[5000];

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d\n",&n);
            REP(i,n)
            {
                  gets(bufor);
                  M[string(bufor)] = i;
            }
            scanf("%d\n",&m);
            REP(i,m+1) REP(j,n) DP[i][j] = -1;
            
            REP(i,m)
            {
                  gets(bufor);
                  int v = M[string(bufor)];
                  if(i == 0)
                  {
                        REP(j,n) if(j!=v) DP[1][j] = 0;
                  }
                  else
                  {
                        REP(j,n) if(j!=v && DP[i][j]!=-1 && (DP[i+1][j]==-1 || DP[i+1][j] > DP[i][j])) DP[i+1][j] = DP[i][j];
                        REP(j,n) if(j!=v && DP[i][v]!=-1 && (DP[i+1][j] == -1 || DP[i+1][j] > DP[i][v] + 1)) DP[i+1][j] = DP[i][v] + 1;
                  }
            }
            int ans = 1000000;
            if(m == 0) ans = 0;
            REP(i,n) if(DP[m][i]!=-1) ans<?=DP[m][i];
            printf("Case #%d: %d\n",t2,ans);
      }
      return 0;
}
