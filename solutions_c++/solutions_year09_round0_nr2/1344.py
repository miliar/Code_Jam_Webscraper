#include<cstdio>
using namespace std;

#define INF 1000000007
#define REP(z,n) for(int (z)=0;(z)<(n);++(z))

int v[103][103];
int p[103][103];
int c,h,w;

int dx[]={-1, 0, 0, 1};
int dy[]={0, -1, 1, 0};

int getp(int x, int y)
{
 if(x<0 || x>=h) return INF;
 if(y<0 || y>=w) return INF;
 return p[x][y];
}

int dfs(int x, int y)
{
 if(v[x][y]!=0) return v[x][y];
 int min=INF;
 REP(i,4) if(getp(x+dx[i], y+dy[i])<min) min=getp(x+dx[i], y+dy[i]);
 if(min<getp(x,y))
 {
  REP(i,4) if(getp(x+dx[i], y+dy[i])==min) {v[x][y]=dfs(x+dx[i], y+dy[i]); break; }
 }
 else
 {
  v[x][y]=c++;
 }
 return v[x][y];
}

int main()
{
 int t; scanf("%d", &t);

 REP(q,t)
 {
  c=1;
  scanf("%d%d", &h, &w);
  REP(i,h)
   REP(j,w) { scanf("%d", &p[i][j]); v[i][j]=0; }
  REP(i,h)
   REP(j,w)
  {
   if(v[i][j]==0) v[i][j]=dfs(i,j);
  }
  printf("Case #%d:\n", q+1);
  REP(i,h)
  {
   REP(j,w) printf("%c ", (v[i][j]-1)+'a');
   printf("\n");
  }
 }





}
