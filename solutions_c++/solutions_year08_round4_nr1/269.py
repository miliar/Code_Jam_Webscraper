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
int m,v;

int P[2000000];
int C[2000000];
int B[2000000];


pi gogo(int ind)
{
      if(ind>(m-1)/2)
      {
                  if(C[ind] == 1) return pi(0,100000000);
                  else return pi(100000000,0);
      }
      else
      {
            pi ret = pi(100000000,100000000);
            
            pi a = gogo(ind+ind);
            pi b = gogo(ind+ind+1);
            if(B[ind] == 1) 
            {
                  ret.fst <?= a.fst + b.fst;
                  ret.snd <?= a.fst + b.snd;
                  ret.snd <?= a.snd + b.snd;
                  ret.snd <?= a.snd + b.fst;
            }
            else
            {
                  ret.fst <?= a.fst + b.fst;
                  ret.fst <?= a.fst + b.snd;
                  ret.snd <?= a.snd + b.snd;
                  ret.fst <?= a.snd + b.fst;
            }
            
            if(C[ind])
            {
                  if(B[ind] == 0)
                  {
                        ret.fst <?= a.fst + b.fst + 1;
                        ret.snd <?= a.fst + b.snd + 1;
                        ret.snd <?= a.snd + b.snd + 1;
                        ret.snd <?= a.snd + b.fst + 1;
                  }
                  else
                  {
                        ret.fst <?= a.fst + b.fst + 1;
                        ret.fst <?= a.fst + b.snd + 1;
                        ret.snd <?= a.snd + b.snd + 1;
                        ret.fst <?= a.snd + b.fst + 1;
                  }
            }
            
            return ret;
      }
}

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d",&m,&v);
            FOR(i,1,(m-1)/2)
                  scanf("%d %d",&B[i],&C[i]);
            FOR(i,(m-1)/2+1,m)
                  scanf("%d",&C[i]);
            pi pp = gogo(1);
            printf("Case #%d: ",t2);
            if(v == 1)
            {
                  if(pp.fst >= 100000000) printf("IMPOSSIBLE\n");
                  else printf("%d\n",pp.fst);
            }
            else
            {
                  if(pp.snd >= 100000000) printf("IMPOSSIBLE\n");
                  else printf("%d\n",pp.snd);
            }
      }
      return 0;
}
