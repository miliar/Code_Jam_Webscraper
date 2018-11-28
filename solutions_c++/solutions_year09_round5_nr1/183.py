#include <cstdio>
#include <map>
#include <algorithm>
using namespace std;


const int INF = 1000000000;
const int M = 13;
char s[M][M];
int m,n;

struct point {
  int x,y;
  point(int a=0,int b=0):y(a),x(b){}
  bool operator<(const point &p)const {
    return x==p.x ? y<p.y : x<p.x;
  }
  bool operator==(const point &p)const {
    return x==p.x && y==p.y;
  }
};

struct stan {
  point p[2];
  void norm() {
    if(p[1]<p[0]) swap(p[0],p[1]);
  }
  inline bool operator<(const stan &s) const {
    return p[0]==s.p[0] ? p[1]<s.p[1] : p[0]<s.p[0];
  }
  inline bool operator==(const stan &s) const {
    return p[0]==s.p[0] && p[1]==s.p[1];
  }
  void print() const {
    printf("[%d,%d], [%d,%d]\n",p[0].y,p[0].x,p[1].y,p[1].x);
  }
};

stan pc,kn;

map<stan,int> dist;
stan q[10*M*M*M*M];

inline int int_abs(int x) { return x<0?-x:x; }
bool isstable(const stan &s) {
  return int_abs(s.p[0].x-s.p[1].x)+int_abs(s.p[0].y-s.p[1].y)==1;
}

inline bool ins(int y,int x) {
  return 1<=y && y<=m && 1<=x && x<=n;
}

inline bool iscorrect(stan s) {
  return !(s.p[0]==s.p[1]) && int_abs(s.p[0].x-s.p[1].x)+int_abs(s.p[0].y-s.p[1].y)<=2;
}

int rx[]={-1,1,0,0};
int ry[]={0,0,-1,1};
int iler=4;

map<stan,bool> vis;

int prevx[]={1,-1,0,0};
int prevy[]={0,0,1,-1};

void bfs() {
  dist.clear();
  vis.clear();
  pc.norm();
  kn.norm();
  dist[pc]=0;
  int beg=0,end=0;
  q[end++]=pc;
  vis[pc]=true;
  while(beg<end) {
    stan X=q[beg++];
/*    printf("wyciagam: ");
    X.print();
    X.norm();
    printf("dist=%d\n",dist[X]);*/
    if(isstable(X)) {
      for(int i=0;i<2;++i) {
        for(int j=0;j<iler;++j) {
          stan nowy=X;
          point P;
          P.x = X.p[i].x+rx[j];
          P.y = X.p[i].y+ry[j];
          if(!ins(P.y,P.x)) continue;
          if(s[P.y][P.x]=='#' || P==X.p[1-i]) continue;
          point PREV;
          PREV.x=X.p[i].x+prevx[j];
          PREV.y=X.p[i].y+prevy[j];
          if(!ins(PREV.y,PREV.x)) continue;
          if(s[PREV.y][PREV.x]=='#' || PREV==X.p[1-i]) continue;
          nowy.p[i]=P;
          if(!iscorrect(nowy)) continue;
          nowy.norm();
          map<stan,int>::iterator it=dist.find(nowy);
          if(vis[nowy]) continue;
          bool ok=true;
          for(int k=0;k<2;++k) {
            if(s[nowy.p[k].y][nowy.p[k].x]=='#')
              ok=false;
          }
          if(!ok) continue;
/*          printf("ze stanu ");
          X.print();
          printf("do stanu: ");
          nowy.print();
          printf("\n");*/
            nowy.norm();
            dist[nowy]=dist[X]+1;
            vis[nowy]=true;
            q[end++]=nowy;
            if(nowy==kn) return;
        }
      }
    } else {
      for(int i=0;i<2;++i) {
        for(int j=0;j<iler;++j) {
          stan nowy=X;
          point P;
          P.x = X.p[i].x+rx[j];
          P.y = X.p[i].y+ry[j];
          if(!ins(P.y,P.x)) continue;
          if(s[P.y][P.x]=='#' || P==X.p[1-i]) continue;
          point PREV;
          PREV.x=X.p[i].x+prevx[j];
          PREV.y=X.p[i].y+prevy[j];
          if(!ins(PREV.y,PREV.x)) continue;
          if(s[PREV.y][PREV.x]=='#' || PREV==X.p[1-i]) continue;
          nowy.p[i]=P;
          nowy.norm();
/*          printf("rozwazam: ");
          nowy.print();
          printf("\n");*/
          if(!isstable(nowy)) continue;
//          printf("jest stable!\n");
          if(!iscorrect(nowy)) continue;
//          printf("jest poprawny!\n");
          if(vis[nowy]) continue;
//          printf("nieodwiedzony!\n");
          bool ok=true;
          for(int k=0;k<2;++k) {
            if(s[nowy.p[k].y][nowy.p[k].x]=='#')
              ok=false;
          }
//          printf("OK=%d\n",ok);
          if(!ok) continue;
/*          printf("ze stanu ");
          X.print();
          printf("do stanu: ");
          nowy.print();*/
//          if(vis[nowy]) continue;
//          map<stan,int>::iterator it=dist.find(nowy);
//          if(it==dist.end()) {
            dist[nowy]=dist[X]+1;
            vis[nowy]=true;
            q[end++]=nowy;
            if(nowy==kn) return;
        }
      }
    }
  }
}

void solve() {
  int cnt1=0,cnt2=0;
  for(int i=1;i<=m;++i) {
    for(int j=1;j<=n;++j) {
      if(s[i][j]=='o' || s[i][j]=='w') {
        pc.p[cnt1++]=point(i,j);
      }
      if(s[i][j]=='x' || s[i][j]=='w') {
        kn.p[cnt2++]=point(i,j);
      }
    }
  }
/*  printf("Pc: ");
  pc.print();
  printf("\n");
  printf("KN: ");
  kn.print();
  printf("\n");*/
  bfs();
//  map<stan,int>::iterator it=dist.find(kn);
//  if(it==dist.end()) printf("-1");
  stan kn2=kn;
//  printf("kn "); kn.print();
  swap(kn2.p[0],kn2.p[1]);
//  printf("kn2: "); kn2.print();
//  printf("dist[kn] = %d dist[kn2] = %d\n",dist[kn],dist[kn2]);
  if(vis[kn]==false && vis[kn2]==false) printf("-1");
  else {
    stan kn2=kn;
    swap(kn2.p[0],kn2.p[1]);
    int ret=INF;
    map<stan,int>::iterator it=dist.find(kn2);
    if(it!=dist.end() && vis[kn2]==true)
      ret=min(ret,dist[kn2]);
    it=dist.find(kn);
    if(it!=dist.end() && vis[kn]==true)
      ret=min(ret,dist[kn]);
    printf("%d",ret);
  }
}

int odl[M][M];
point kol[M*M*10];
void simple() {
  int beg=0,end=0;
  point pc,kn;
  for(int i=1;i<=m;++i) for(int j=1;j<=n;++j) {
    if(s[i][j]=='o' || s[i][j]=='w') {
      pc=point(i,j);
    }
    if(s[i][j]=='x' || s[i][j]=='w') {
      kn=point(i,j);
    }
  }
//  printf("pc=[%d,%d] kn=[%d,%d]\n",pc.y,pc.x,kn.y,kn.x);
  for(int i=1;i<=m;++i)
    for(int j=1;j<=n;++j)
      odl[i][j]=INF;
  odl[pc.y][pc.x]=0;
  kol[end++]=pc;
  while(beg<end) {
    point P = kol[beg++];
//    printf("P=[%d,%d]\n",P.y,P.x);
    for(int i=0;i<iler;++i) {
      point next=P,prev=P;
      next.x+=rx[i];
      next.y+=ry[i];
      prev.x+=prevx[i];
      prev.y+=prevy[i];
//      printf("next=[%d,%d] prev=[%d,%d]\n",next.y,next.x,prev.y,prev.x);
      if(!ins(prev.y,prev.x) || !ins(next.y,next.x)) continue;
      if(s[prev.y][prev.x]=='#') continue;
      if(s[next.y][next.x]=='#') continue;
      if(odl[next.y][next.x]==INF) {
        odl[next.y][next.x]=odl[P.y][P.x]+1;
        kol[end++]=next;
      }
    }
  }
  if(odl[kn.y][kn.x]==INF) printf("-1");
  else printf("%d",odl[kn.y][kn.x]);
}

int main() {
  int d;
  scanf("%d\n",&d);
  for(int j=1;j<=d;++j) {
    scanf("%d %d\n",&m,&n);
    for(int i=1;i<=m;++i)
      scanf("%s\n",s[i]+1);
    int boxes=0;
    for(int i=1;i<=m;++i)
      for(int j=1;j<=n;++j)
        if(s[i][j]=='o' || s[i][j]=='w') ++boxes;
/*    for(int i=1;i<=m;++i) {
      for(int j=1;j<=n;++j) {
        printf("%c",s[i][j]);
      }
      printf("\n");
    }*/
    printf("Case #%d: ",j);
    if(boxes==1) simple();
    else solve();
    printf("\n");
  }
  return 0;
}
