#include <cstdio>
#include <set>
#include <utility>
using namespace std;
int t,tt,x,y,i,j,k,n,m,z,w,p,ax[111][111],ay[111][111],bx[111][111],by[111][111],e[111][111],ee[111][111],u[111][111],r,md=1000003,c[111][111][44],d[111][111][44];
char s[111][111];
set <pair <int, pair <int, int> > > st;
long long pw2(int b) {
  if (b==0) return 1LL;
  if (b&1) return (pw2(b-1)*2)%md;
  long long x=pw2(b/2);
  return (x*x)%md;
}
void out(int i, int j) {
  set <pair <int, pair <int, int> > > :: iterator z=st.find(make_pair(e[i][j],make_pair(i,j)));
  if (z==st.end()) return;
  st.erase(z); e[i][j]--;
//  printf("out %d %d = %d\n",i,j,e[i][j]);
  st.insert(make_pair(e[i][j],make_pair(i,j)));
}
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m); st.clear();
    for (i=0; i<n; i++) for (j=0; j<m; j++) e[i][j]=0;
    for (i=0; i<n; i++) {
      scanf("%s",s[i]);
      //puts(s[i]);
      for (j=0; j<m; j++) {
      if (s[i][j]=='-') {
        ax[i][j]=i;
        ay[i][j]=(j+1)%m;
        bx[i][j]=i;
        by[i][j]=(j+m-1)%m;
      } else if (s[i][j]=='|') {
        ax[i][j]=(i+1)%n;
        ay[i][j]=j;
        bx[i][j]=(i+n-1)%n;
        by[i][j]=j;
      } else if (s[i][j]=='/') {
        ax[i][j]=(i+1)%n;
        ay[i][j]=(j+m-1)%m;
        bx[i][j]=(i+n-1)%n;
        by[i][j]=(j+1)%m;
      } else {
        ax[i][j]=(i+1)%n;
        ay[i][j]=(j+1)%m;
        bx[i][j]=(i+n-1)%n;
        by[i][j]=(j+m-1)%m;
      }
      c[ax[i][j]][ay[i][j]][e[ax[i][j]][ay[i][j]]]=i;
      d[ax[i][j]][ay[i][j]][e[ax[i][j]][ay[i][j]]]=j;
      e[ax[i][j]][ay[i][j]]++;
      c[bx[i][j]][by[i][j]][e[bx[i][j]][by[i][j]]]=i;
      d[bx[i][j]][by[i][j]][e[bx[i][j]][by[i][j]]]=j;
      e[bx[i][j]][by[i][j]]++;
      }
    }
    for (i=0; i<n; i++) for (j=0; j<m; j++) { st.insert(make_pair(e[i][j],make_pair(i,j))); ee[i][j]=e[i][j]; }
    //for (i=0; i<n; i++,puts("")) for (j=0; j<m; j++) printf("%d ",e[i][j]);
    for (z=n*m, w=0; z>0; z--) {
//    set <pair <int, pair <int, int> > > :: iterator zz;
//    for (zz=st.begin(); zz!=st.end(); zz++) printf("%d (%d %d) , ",(*zz).first,(*zz).second.first,(*zz).second.second); puts("");
      p=(*st.begin()).first;
//      printf("%d = ",p);
      if (p<1 || p>2) break;
      if (p==2) w++;
      i=(*st.begin()).second.first;
      j=(*st.begin()).second.second;
//      printf("%d %d ",i,j);
      st.erase(st.begin());
      if (st.empty()) break;
      for (k=0; k<ee[i][j]; k++) {
        x=c[i][j][k];
        y=d[i][j][k];
        if (u[x][y]!=t) {
//          printf("from %d %d\n",x,y);
          u[x][y]=t;
          if (ax[x][y]!=i || ay[x][y]!=j) out(ax[x][y],ay[x][y]);
          if (bx[x][y]!=i || by[x][y]!=j) out(bx[x][y],by[x][y]);
          break;
        }
      }
//      for (int i=0; i<n; i++,puts("")) for (int j=0; j<m; j++) printf("%d ",e[i][j]);
//puts("__");
    }
    if (p<=0) r=0; else r=pw2(w);
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
