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


////////////////////////////////////////////////////////////////////////////////

int t,n,c;
map<string,int> M;
int A[500],B[500],C[500];
char bufor[1000];
int DP[10001];

int compute(int a,int b,int c)
{
      REP(i,10001) DP[i] = 1000000000;
      DP[0] = 0;
      FOR(i,1,10000) REP(j,n) if((C[j] == a || C[j] == b || C[j] == c) && i == B[j]) 
            FOR(k,A[j],i) DP[i] <?= DP[k-1] + 1;
      return DP[10000];
}

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d",&n);
            M.clear();c =0;
            REP(i,n)
            {
                  scanf(" %s %d %d",bufor,&A[i],&B[i]);
                  if(M[string(bufor)] == 0) M[string(bufor)] = ++c;
                  C[i] = M[string(bufor)];
            }
            int ret = 1000000000;
            FOR(i,1,c) FOR(j,1,i) FOR(k,1,j) ret <?= compute(i,j,k);
            printf("Case #%d: ",t2);
            if(ret == 1000000000) printf("IMPOSSIBLE\n");
            else printf("%d\n",ret);
      }
      return 0;
}
