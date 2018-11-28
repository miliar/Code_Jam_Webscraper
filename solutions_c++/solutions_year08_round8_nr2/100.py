#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <iostream>
using namespace std;
#define DEBUG(X) cout << #X << " " << X << endl;
const int MAXN=310;
const int INF=1<<28;
const int SZ=1<<14;

class T
{
public:
  T() { }
  T(int _a, int _b) { a=_a; b=_b; }
  int a,b;
};

class CMPT
{
public:
  bool operator () (const T &a, const T &b)
  { return a.b==b.b?a.a<b.a:a.b<b.b; }
};

int n, nc;
map<string,int> col;
vector<T> v[MAXN];
int tree[2*SZ+100];
int c[3];

void treeInsert(int p, int tLeft, int tRight, int pos, int val)
{
  if(tLeft==tRight) { 
    if(tree[p]==-1 || val<tree[p])
      tree[p]=val; 
    return; 
  }
  if(pos <= (tLeft+tRight)/2)
    treeInsert(2*p, tLeft, (tLeft+tRight)/2, pos, val);
  else
    treeInsert(2*p+1, (tLeft+tRight)/2+1, tRight, pos, val);
  int a=tree[2*p], b=tree[2*p+1];
  if(a==-1) tree[p]=b;
  else if(b==-1) tree[p]=a;
  else tree[p]=min(a,b);
  return;
}

int getMin(int p, int tLeft, int tRight, int l, int r)
{
  if(r<tLeft || l>tRight) return -1;
  if(tLeft==tRight) return tree[p];
  if(l<=tLeft && r>= tRight) return tree[p];
  
  int a=getMin(2*p, tLeft, (tLeft+tRight)/2, l, r);
  int b=getMin(2*p+1, (tLeft+tRight)/2+1, tRight, l, r);
  if(a!=-1 && b!=-1) return min(a,b);
  if(a==-1) return b;
  if(b==-1) return a;
  return -1;
}

int solve()
{
  //printf("NEw solbve\n");
  int p[3];
  memset(tree,-1,sizeof(tree));
  treeInsert(1, 0, SZ-1, 0, 0);
  
  p[0]=p[1]=p[2]=0;
  int sz[3], mv[3], pos, a,b;
  sz[0]=v[c[0]].size(), sz[1]=v[c[1]].size(), sz[2]=v[c[2]].size();
  while(p[0]<sz[0] || p[1]<sz[1] || p[2]<sz[2]) {
    pos=0;
    for(int i=0;i<3;i++)
      if(p[i]<sz[i]) mv[i]=v[c[i]][p[i]].b;
      else mv[i]=INF;
    if(mv[0] <= mv[1] && mv[0]<=mv[2]) pos=0;
    if(mv[1] <= mv[0] && mv[1]<=mv[2]) pos=1;
    if(mv[2] <= mv[0] && mv[2] <= mv[1]) pos=2;
    
    a=v[c[pos]][p[pos]].a, b=v[c[pos]][p[pos]].b;
    /*printf("Taking...\n");
    DEBUG(a); 
    DEBUG(b);
    printf("\n");*/
    
    p[pos]++;
    
    int minv = getMin(1, 0, SZ-1, a-1, b-1);
    if(minv>-1)
      treeInsert(1,0, SZ-1, b, minv+1);
  }
  int r=getMin(1,0,SZ-1, 10000, 10000);
  //pDEBUG(r);
  if(r==-1) return INF;
  return r;
}

int main()
{
  int tt, ta,tb;
  char str[20];
  scanf("%d", &tt);
  for(int t1=1;t1<=tt;t1++) {
    for(int i=0;i<MAXN;i++) v[i].clear();
    col.clear();
    nc=0;
    scanf("%d", &n);
    for(int i=0;i<n;i++) {
      scanf("%s%d%d", str, &ta, &tb);
      int pos=-1;
      if(col.find(str) != col.end())
	pos=col[str];
      else {
	pos=nc;
	col[str]=nc;
	nc++;	
      }
      v[pos].push_back(T(ta,tb));
    }

    for(int i=0;i<nc;i++)
      sort(v[i].begin(),v[i].end(),CMPT());
      
    
    int ret=INF;
    nc+=2;
    for(c[0]=0;c[0]<nc;c[0]++)
      for(c[1]=c[0]+1;c[1]<nc;c[1]++)
	for(c[2]=c[1]+1; c[2] < nc; c[2]++)
	  ret=min(ret,solve());
       

    printf("Case #%d: ", t1);
    if(ret==INF) printf("IMPOSSIBLE\n");
    else printf("%d\n", ret);
    fflush(stdout);
  }
}
