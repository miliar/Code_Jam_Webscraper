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

int t,na,nb,r,a,b,c,d;
vi T[2000];
vi P[2000];
int A[2000];
int B[2000];

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d %d",&r,&na,&nb);
            REP(i,2000) T[i].clear();
            REP(i,2000) P[i].clear();
            REP(i,2000) A[i] = B[i] = 0;
            REP(i,na)
            {
                  scanf("%d:%d %d:%d",&a,&b,&c,&d);
                  T[a*60+b].pb(c*60 + d + r);
            }

            REP(i,nb)
            {
                  scanf("%d:%d %d:%d",&a,&b,&c,&d);
                  P[a*60+b].pb(c*60 + d + r);
            }
            
            int a1 = 0, a2 = 0;
            REP(i,1440)
            {
                  REP(j,SIZE(T[i]))
                  {
                        if(A[i]) A[i]--;else a1++;
                        B[T[i][j]]++;
                  }
                  A[i+1] += A[i];
                  REP(j,SIZE(P[i]))
                  {
                        if(B[i]) B[i]--;else a2++;
                        A[P[i][j]]++;
                  }
                  B[i+1] += B[i];
            }
            
            
            printf("Case #%d: %d %d\n",t2,a1,a2);
      }
      return 0;
}
