#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;
 
int s, m, X[11000], Y[11000];
int dx[6]={-1,-1,0,1,1,0};
int dy[6]={-1,0,1,1,0,-1};
map <pair <int, int>, int> M[2];
int tc[2];
set <int> S[12000];
pair <int, int> C[7];

void dfs (int g, pair <int, int> c)
{
  int x=c.first, y=c.second, nx, ny;
  M[g][c]=tc[g];
  for (int i=0; i<6; i++)
  {
    nx=x+dx[i], ny=y+dy[i];
    if (M[g].count(mp(nx,ny))!=0 && M[g][mp(nx,ny)]==0)
      dfs(g,mp(nx,ny));
  }
}

string check (int n)
{
  int x, y, ddx, ddy, i, j, k, nx, ny;
  map <pair <int, int>, int> :: iterator it;
  set <int> :: iterator it2;
  string res="";
  M[0].clear(), M[1].clear();
  for (i=0; i<n; i++)
    M[0][mp(X[i],Y[i])]=0;
  for (i=0; i<n; i++)
    for (j=0; j<6; j++)
    {
      nx=X[i]+dx[j], ny=Y[i]+dy[j];
      if (M[0].count(mp(nx,ny))==0)
        M[1][mp(nx,ny)]=0;
    }
  for (i=0; i<2; i++)
    for (tc[i]=0, it=M[i].begin(); it!=M[i].end(); it++)
      if (it->second==0)
        tc[i]++, dfs(i,it->first);
  bool fl=0;
  for (i=0; i<6; i++)
    for (j=i+1; j<6; j++)
      if (M[0].count(C[i])!=0 && M[0].count(C[j])!=0 && M[0][C[i]]==M[0][C[j]])
        fl=1;
  if (fl)
    res="bridge";
  fl=0;
  for (i=0; i<6; i++)
  {
    S[i].clear();
    x=C[i].first, y=C[i].second, ddx=(C[i+1].first-C[i].first)/(s-1), ddy=(C[i+1].second-C[i].second)/(s-1);
    //cerr<<"??? "<<C[i].first<<" "<<C[i].second<<"    "<<C[i+1].first<<" "<<C[i+1].second<<endl;
    for (j=1, x+=ddx, y+=ddy; j<s-1; j++, x+=ddx, y+=ddy)
    {
      //cerr<<x<<" "<<y<<endl;
      if (M[0].count(mp(x,y))!=0)
        S[i].insert(M[0][mp(x,y)]);
    }
   // cerr<<endl;
  }
  //cerr<<"!!!!!"<<endl;
  for (i=0; i<6; i++)
    for (j=i+1; j<6; j++)
      for (k=j+1; k<6; k++)
        for (it2=S[i].begin(); it2!=S[i].end(); it2++)
          if (S[j].count(*it2)!=0 && S[k].count(*it2)!=0)
            fl=1;
  if (fl)
    (res=="")?(res="fork"):(res+="-fork");
  fl=0;
  for (i=0; i<12000; i++)
    S[i].clear();
  for (it=M[1].begin(); it!=M[1].end(); it++)
  {
    x=it->first.first, y=it->first.second;
    for (j=0; j<6; j++)
    {
      nx=x+dx[j], ny=y+dy[j];
      if (M[0].count(mp(nx,ny))!=0)
        S[M[0][mp(nx,ny)]].insert(it->second);
    }
  }
  for (i=0; i<12000; i++) 
    if (S[i].size()>1)
      fl=1;
  if (fl)
    (res=="")?(res="ring"):(res+="-ring");
  return res;
}

int main()
{
  int tst, cnt, i, r;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<cnt<<endl;
    scanf("%d%d", &s, &m);
    for (i=0; i<=6; i++)
      C[i]=mp(s+(s-1)*dx[i%6],s+(s-1)*dy[i%6]);
    for (i=0; i<m; i++)
      scanf("%d%d", &X[i], &Y[i]);
    printf("Case #%d: ", cnt);
    r=1;
    while (check(r)=="" && r<=m)
      r++;
    if (r>m)
      puts("none");
    else
      cout<<check(r)<<" in move "<<r<<endl;
  }
  return 0;
}
