#include <cstdio>
#include <string>
#include <map>
using namespace std;
const int dx[6]={0,1,1,0,-1,-1};
const int dy[6]={1,1,0,-1,-1,0};
map <pair <int, int>, int> M;
int t,tt,it,n,m,i,k,num,real,x,y,nx,ny,bc[77],p[10100],hi[10100],lo[10100],g[10100][6];
bool rx,ry,rz,was;
int corners(int x, int y) {
  if (x==1 && y==1) return 1;
  if (x==1 && y==n) return 2;
  if (x==n && y==n+n-1) return 4;
  if (x==n+n-1 && y==n+n-1) return 8;
  if (x==n+n-1 && y==n) return 16;
  if (x==n && y==1) return 32;
  return 0;
}
int edges(int x, int y, int z) {
  int r=0;
  if (x==1 && ((z>>0)&1)==0 && ((z>>1)&1)==0) r|=1;
  if (y-x==n-1 && ((z>>1)&1)==0 && ((z>>2)&1)==0) r|=2;
  if (y==n+n-1 && ((z>>2)&1)==0 && ((z>>3)&1)==0) r|=4;
  if (x==n+n-1 && ((z>>3)&1)==0 && ((z>>4)&1)==0) r|=8;
  if (x-y==n-1 && ((z>>4)&1)==0 && ((z>>5)&1)==0) r|=16;
  if (y==1 && ((z>>5)&1)==0 && ((z>>1)&0)==0) r|=32;
  return r;
}
int findset(int x) {
  if (x!=p[x]) p[x]=findset(p[x]);
  return p[x];
}/*
bool dfs(int i, int l) {
  d[l]=i;
  u[i]=it;
  for (int k=0; k<6; k++) if (g[i][k]!=0 && u[g[i][k]]!=it) {
    if (dfs(g[i][k],l+1)) return true;
  } else if () {
  return false;
}*/
int u[222][222],w[222][222],qx[222*222],qy[222*222];
bool bfs() {
  int fi=0,fr=1;
  qx[0]=qy[0]=0; u[0][0]=it;
  while (fi<fr) {
    int x=qx[fi];
    int y=qy[fi++];
    for (int k=0; k<6; k++) {
      int nx=x+dx[k];
      int ny=y+dy[k];
      if (nx<0 || nx>n+n || ny<0 || ny>n+n || w[nx][ny]==t || u[nx][ny]==it) continue;
      u[nx][ny]=it;
      qx[fr]=nx;
      qy[fr++]=ny;
    }
  }
  return fr!=(n+n+1)*(n+n+1)-i;
}
int main() {
  freopen("Bsm.in","r",stdin);
  freopen("Bsm.out","w",stdout);
  for (i=1; i<77; i++) bc[i]=bc[i/2]+(i&1);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    printf("Case #%d: ",t);
    M.clear();
    scanf("%d%d",&n,&m);
    //if (n<10) printf("%d %d\n",n,m);
    if (n<2 || n>50) puts("!");
    for (i=1; i<=m; i++) {
      scanf("%d%d",&x,&y);
      //if (n<10) printf("%d %d\n",x,y);
      w[x][y]=t;
      M[make_pair(x,y)]=i;
      p[i]=i;
      hi[i]=corners(x,y);
      lo[i]=edges(x,y,hi[i]);
      if (bc[hi[i]]>1) puts("~");
      if (bc[lo[i]]>1) puts("$");
      //printf("%d\n",hi[i]);
      //printf("%d\n",lo[i]);
      for (k=0; k<6; k++) {
        nx=x+dx[k];
        ny=y+dy[k];
        if (M.count(make_pair(nx,ny))) {
          real=M[make_pair(nx,ny)];
          num=findset(real);
          hi[i]|=hi[num];
          lo[i]|=lo[num];
          p[num]=i;
          //g[i][k]=num;
          //g[num][(k+3)%6]=i;
        }// else g[i][k]=0;
      }
      ++it;
      //printf("h %d\n",hi[i]);
      //printf("l %d\n",lo[i]);
      rx=(bc[hi[i]]>=2);
      ry=(bc[lo[i]]>=3);
      //rz=dfs(i,0);
      rz=bfs();
      if (rx || ry || rz) {
        was=false;
        if (rx) {
          was=true;
          printf("bridge");
        }
        if (ry) {
          if (was) printf("-"); else was=true;
          printf("fork");
        }
        if (rz) {
          if (was) printf("-"); else was=true;
          printf("ring");
        }
        printf(" in move %d\n",i);
        break;
      }
    }
    if (i>m) puts("none"); else for (i++; i<=m; i++) scanf("%d%d",&x,&y);
  }
  return 0;
}
