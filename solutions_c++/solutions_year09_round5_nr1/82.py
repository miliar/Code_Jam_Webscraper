#include <cstdio>
#include <cstring>
#include <set>
#include <algorithm>
#include <map>
using namespace std;
const int dir[4][2]={0,1,1,0,0,-1,-1,0};

struct point {
  int x,y;

  point () {
  }

  point (int x_,int y_) {
    x=x_;y=y_;
  }
};

bool operator < (point a,point b) {
  return a.x<b.x || (a.x==b.x && a.y<b.y);
}

bool operator == (point a,point b) {
  return a.x==b.x && a.y==b.y;
}

int k;

struct sta {
  point p[6];

  void unit() {
    sort(p+1,p+k+1);
  }
};

bool operator < (sta a,sta b) {
  for (int i=1;i<=k;i++) {
    if (a.p[i]<b.p[i]) return true;
    if (b.p[i]<a.p[i]) return false;
  }
  return false;
}

bool operator == (sta a,sta b) {
  for (int i=1;i<=k;i++) 
    if (!(a.p[i]==b.p[i])) return false;
  return true;
}

sta q[2000000];
char g[20][20];
int n,m,ng,ns;
sta st,goal;
int f[2000000];
set<sta> hh;
map<sta,bool> con;
char bl[10];
int fa[10];
//int ff[100000];
//bool db;

int gabs(int a) {
  return (a>0)?(a):(-a);
}

int root(int a) {
  return (fa[a]<0)?(a):(fa[a]=root(fa[a]));
}

bool isbad(sta a) {
  //  if (k==1) return false;
  //  return gabs(a.p[1].x-a.p[2].x)+gabs(a.p[1].y-a.p[2].y)>1;
  memset(fa,-1,sizeof(fa));
  for (int i=1;i<=k;i++) 
    for (int j=i+1;j<=k;j++) {
      if (gabs(a.p[i].x-a.p[j].x)+gabs(a.p[i].y-a.p[j].y)==1) {
	//	if (db) printf("my %d %d\n",i,j);
	int r1=root(i),r2=root(j);
	if (r1!=r2) {
	  if (r1<r2) fa[r2]=r1; else fa[r1]=r2;
	}
	//	fa[root(j)]=root(i);
      }
    }
  bool ok=false;
  for (int i=1;i<=k;i++) {
    if (root(i)!=1) {
      //      if (db) printf("shit! %d\n",i);
      ok=true;
      break;
    }
  }
  return ok;
}

bool valid(int x,int y,sta tmp) {
  for (int i=1;i<=k;i++) {
    if (tmp.p[i].x==x && tmp.p[i].y==y) return false;
  }
  return x>=1 && x<=n && y>=1 && y<=m && g[x][y]!='#';
}

int main() {
  int c,C=0;
  for (scanf("%d",&c);c>0;c--) {
    scanf("%d%d",&n,&m);
    //    printf("%d %d\n",n,m);
    gets(bl);
    ng=0,ns=0;
    bool a0=true;
    memset(st.p,0,sizeof(st.p));
    memset(goal.p,0,sizeof(goal.p));
    for (int i=1;i<=n;i++) {
      for (int j=1;j<=m;j++) {
	scanf("%c",&g[i][j]);
	if (g[i][j]=='o' || g[i][j]=='w') st.p[++ns]=point(i,j);
	if (g[i][j]=='x' || g[i][j]=='w') goal.p[++ng]=point(i,j);
	if (g[i][j]=='x') a0=false;
      }
      gets(bl);
    }
    if (ns!=ng) {
      printf("Case #%d: %d\n",++C,-1);
      continue;
    }
    if (a0) {
      printf("Case #%d: %d\n",++C,0);
      continue;
    }
    k=ns;
    st.unit();goal.unit();
    
    //    for (int i=1;i<=k;i++) printf("%d %d   ",goal.p[i].x,goal.p[i].y);
    //printf("\n");

    hh.clear();
    con.clear();
    int h=0,t=1;
    q[1]=st;f[1]=0;

    //    ff[1]=0;
    
    hh.insert(st);
    bool check=false;
    while (h<t) {
      sta now=q[++h];
      
      bool ibn=isbad(now);
      //      printf("ibn %d\n",ibn);

      /*            printf("now %d\n",h);
	for (int i=1;i<=k;i++) printf("%d %d   ",now.p[i].x,now.p[i].y);
	printf("\n");*/

      for (int i=1;i<=k;i++) {
	for (int j=0;j<4;j++) {
	  sta tmp=now;

	  if (!valid(tmp.p[i].x+dir[j][0],tmp.p[i].y+dir[j][1],tmp)) continue;
	  if (!valid(tmp.p[i].x-dir[j][0],tmp.p[i].y-dir[j][1],tmp)) continue;

	  tmp.p[i]=point(tmp.p[i].x+dir[j][0],tmp.p[i].y+dir[j][1]);
	  tmp.unit();

	  bool dup=false;
	  for (int x=2;x<=k;x++) {
	    if (tmp.p[x-1]==tmp.p[x]) {
	      dup=true;
	      break;
	    }
	  }


	  if (dup) continue;

	  //	  printf("Shit\n");
	  
	  //	  for (int ii=1;ii<=k;ii++) printf("%d %d   ",tmp.p[ii].x,tmp.p[ii].y);
	  //	  printf("\n");

	  //	  printf("%d\n",isbad(tmp));
	  if (ibn && isbad(tmp)) continue;

	  //	  printf("Shit\n");


	  if (hh.find(tmp)==hh.end()) {
	    
	    hh.insert(tmp);
	    q[++t]=tmp;
	    f[t]=f[h]+1;
	    //	    ff[t]=h;
	    if (tmp==goal) {
	      printf("Case #%d: %d\n",++C,f[t]);

/*	      int tt=t;
	      db=true;
	      while (tt!=0) {
		for (int ii=1;ii<=k;ii++) printf("%d %d   ",q[tt].p[ii].x,q[tt].p[ii].y);
		printf("%d",isbad(q[tt]));
		printf("\n");
		
		tt=ff[tt];
		}*/

	      check=true;
	      break;
	    }
	  }
	}
	if (check) break;
      }
      if (check) break;
    }
    if (!check) printf("Case #%d: %d\n",++C,-1);
  }
}
