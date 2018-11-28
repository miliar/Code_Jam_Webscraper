#include <iostream>
#include <cstring>
#include <algorithm>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)
#define clr(a,v) memset(a,v,sizeof(a))

using namespace std;

#define MAX 10123
#define INF 10123

int n_tests,test;
int M,V;
int oper[MAX],change[MAX],T[MAX][2],calc[MAX][2],state[MAX];
int i,j,k,ans;

int isleaf(int i)
{
  return i>(M-1)/2;
}

int result(int op,int a,int b)
{
  if (op==0) 
  {  
    //cout << (int) (a|| b)<< endl;
    return a || b;
  }
  //cout << (int) (a && b) << endl;
  return a && b;
}

int solve(int i,int v)
{
  if (calc[i][v]) return T[i][v];
  if (isleaf(i))
  {
    if (v==state[i])
    {
      T[i][v]=0;
    }
    else
    {
      T[i][v]=INF;
    }
  }
  else
  {
    int l,r,a,b;
    l=2*i;
    r=2*i+1;
    // no change
    T[i][v]=INF;
    for_to(a,0,1)
    {
      for_to(b,0,1)
      {
        // no change
        if (result(oper[i],a,b)==v && solve(l,a)!=INF && solve(r,b)!=INF)
        {
          T[i][v]=min(T[i][v],solve(l,a)+solve(r,b));
        }
        // change
        if (change[i])
        {
          if (result(1-oper[i],a,b)==v && solve(l,a)!=INF && solve(r,b)!=INF)
          {
            T[i][v]=min(T[i][v],1+solve(l,a)+solve(r,b));
          }
        }
      }
    }
  }
  calc[i][v]=1;
  //cout << i << ", " << v << ": " << T[i][v] << endl;
  return T[i][v];
}

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%d %d",&M,&V);
    for_to(i,1,(M-1)/2)
    {
      scanf("%d %d",&oper[i],&change[i]);
      //cout << "read " << i << " " << oper[i] << " " << change[i] << endl;
    }
    for_to(i,(M-1)/2 + 1,M)
    {
      scanf("%d",&state[i]);
      //cout << "read " << i << " " << state[i] << endl;
    }
    clr(calc,0);
    ans=solve(1,V);
    if (ans==INF) printf("Case #%d: IMPOSSIBLE\n",test);
    else printf("Case #%d: %d\n",test,ans);
  }
  return 0;
}
