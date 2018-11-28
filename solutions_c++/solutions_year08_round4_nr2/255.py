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

int t;
int a,n,m;

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d %d",&n,&m,&a);
            
            printf("Case #%d:",t2);
            bool found = false;
            FOR(i,0,n) FOR(j,0,m) FOR(h,0,n) FOR(k,0,m)
            if( ABS(i * j - j * h - k * i) == a)
            {
                        found = true;
                        printf(" %d %d %d %d %d %d\n",i,0,0,j,h,k);
                        goto zonk;
            }
            zonk:
            if(!found) printf(" IMPOSSIBLE\n");
      }
      return 0;
}
