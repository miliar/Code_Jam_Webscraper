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

int t,n,m;
char c;
int T[11][1<<11];
int B[11];

int gogo(int mask,int p)
{
      if(p == n) return 0;
      else
      {
            if(T[p][mask] != -1) return T[p][mask];
            T[p][mask] = 0;
            REP(j,1<<m)
            {
                  bool can = true;
                  int cnt = 0;
                  REP(i,m) if( j&(1<<i)) 
                  {
                        cnt++;
                        if( (mask&(1<<i)) || (i>0 && (j&(1<<(i-1)))) || (i<m-1 && (j&(1<<(i+1))))) {can = false;break;} 
                  }
                  if(can)
                  {
                        int nmask = B[p+1];
                        REP(i,m) if(j&(1<<i))
                        {
                              if(i>0) nmask = nmask | (1<<(i-1));
                              if(i<m-1) nmask = nmask | (1<<(i+1));
                        }
                        T[p][mask] >?= cnt + gogo(nmask,p+1);
                  }
            }
            return T[p][mask];
      }
}

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d",&n,&m);
            B[n] = 0;
            REP(i,n)
            {
                  B[i] = 0;
                  REP(j,m) 
                  {
                        scanf(" %c ",&c);
                        if(c == 'x') B[i] += 1<<j;
                  }
            }            
            int ans = 0;
            REP(i,n) REP(j,1<<m) T[i][j] = -1;
            printf("Case #%d: %d\n",t2,gogo(B[0],0));
      }
      return 0;
}
