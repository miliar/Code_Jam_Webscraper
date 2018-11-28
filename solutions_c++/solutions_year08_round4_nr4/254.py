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
int n,k;
char B[1000000];
char C[1000000];
int W[10];

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d\n",&k);
            gets(B);n = strlen(B);
            int ans = 100000000;
            REP(i,k) W[i] = i;
            do
            {
                  int start = 0;
                  int cst = 1;
                  while(start < n)
                  {
                        REP(i,k) C[start + i] = B[start + W[i]];
                        start += k;
                  } 
                  FOR(i,1,n-1) cst+= C[i] != C[i-1];
                  ans <?= cst;
            } while(next_permutation(W,W+k));            
            
            printf("Case #%d: %d\n",t2,ans);
      }
      return 0;
}
