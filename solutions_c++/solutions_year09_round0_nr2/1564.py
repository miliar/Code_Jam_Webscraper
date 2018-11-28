#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long int huge;
const int inf=0x3f2f1f0f;
const huge hinf=0x3fff2fff1fff0fffll;

#define foreach(i...) _foreach(i)
#define all(v) v.begin(), v.end()
#define _foreach(i, b, e) for(__typeof(b) i=b; i!=e; i++)
#define MAXN 110
#define MAXG 30
#define P(p) (p).first][(p).second
typedef pair<int,int> ponto;
int mapa[MAXN][MAXN];
int grupo[MAXN][MAXN];
char letra[MAXG];
ponto dx[4] = {make_pair(-1,0), make_pair(0,-1),
	       make_pair(0,1), make_pair(1,0)};

ponto operator+(ponto a, ponto b)
{
  return make_pair(a.first+b.first, a.second+b.second);
}
ponto conecta(ponto a)
{
  if (mapa[P(a)]==inf)
    return a;
  ponto r=a;
  for(int i=0; i<4; ++i)
    if (mapa[P(a+dx[i])]<mapa[P(r)])
      r=a+dx[i];
  return r;
}
void dfs(ponto p, int cor)
{
  grupo[P(p)]=cor;
  for(int i=0; i<4; ++i)
    if (conecta(p+dx[i])==p)
      dfs(p+dx[i], cor);
}
int main()
{
  int test;
  int n, m;
  int nr;
  char ch;
  scanf(" %d", &test);
  for(int z=1; z<=test; ++z)
    {
      scanf(" %d %d", &n, &m);
      for(int i=0; i<n+2; ++i)
	mapa[i][0]=mapa[i][m+1]=inf;
      for(int j=0; j<m+2; ++j)
	mapa[0][j]=mapa[n+1][j]=inf;
      for(int i=1; i<=n; ++i)
	for(int j=1; j<=m; ++j)
	  scanf(" %d", &mapa[i][j]);
      nr=0;
      for(ponto p=make_pair(1,1); p.first<=n; ++p.first)
	for(p.second=1; p.second<=m; ++p.second)
	  if (conecta(p)==p)
	    dfs(p,++nr);
      for(int i=0; i<=nr; ++i)
	letra[i]=0;
      printf("Case #%d:\n", z);
      ch='a';
      for(int i=1; i<=n; ++i)
	{
	  for(int j=1; j<=m; ++j)
	    {
	      if (letra[grupo[i][j]]==0)
		letra[grupo[i][j]]=ch++;
	      printf("%c ", letra[grupo[i][j]]);
	    }
	  printf("\n");
	}
    }
  return 0;
}
