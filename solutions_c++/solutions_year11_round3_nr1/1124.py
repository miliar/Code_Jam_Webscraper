#include<cassert>
#include<queue>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>

#define eps 1e-12

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;

char s[100][100];
int dx[4]={0,0,1,1};
int dy[4]={0,1,0,1};
int n,m;
char f[4]={'/','\\','\\','/'};
bool bad(int x,int y)
{
  if(x>=0 && x<n)
    if(y>=0&&y<m)
      return true;
  return false;
}
bool doit(int x,int y)
{
  forn(i,4)
  {
    int nx=x+dx[i];
    int ny=y+dy[i];
    if(!bad(nx,ny) || s[nx][ny] != '#')
      return false;
    s[nx][ny]=f[i];
  }    
  return true;
}
int main()         
{
  //assert(freopen(taskname"in","r",stdin));
  //assert(freopen(taskname"out","w",stdout));
  int test_n;
  scanf("%d",&test_n);
  forn(test_id,test_n)
  {
    printf("Case #%d: \n",test_id+1);
    scanf("%d %d ",&n,&m);
    forn(i,n)
      gets(s[i]);
    bool fl=true;
    forn(i,n)
      forn(j,m)
        if(s[i][j]=='#')
          if(!doit(i,j))
          {
            fl=false;
          }
    if(fl)
      forn(i,n)
        puts(s[i]);
    else
      puts("Impossible");
  }
  return 0;
}

