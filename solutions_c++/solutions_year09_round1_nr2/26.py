
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>

using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)

const int maxn=24;

const int maxnode=maxn*maxn*4;

int d[maxnode];
int mark[maxnode];

int s, t;
int m,n;
int N;

inline int enc(int i, int j, int k) {
  return (i*n+j)*4+k;
}
void dec(int x, int &i, int &j, int &k) {
  k=x%4;
  x/=4;
  j=x%n;
  i=x/n;
}

struct Light {
  int s, w, t;
  int p;
  void proc() {
    p=s+w;
    t%=p;
    t-=p; //make sure t is negative! :D
  }
  int hw(int from) {
    from-=t;
    from%=p;
    if (from<s) return s-from;
    return 0;
  }
  int vw(int from) {
    from-=t;
    from%=p;
    if (from < s) return 0;
    return p-from;
  }
}light[maxn][maxn];

inline void go(int i, int j, int k, int val) {
  int y= enc(i,j,k);
  if (d[y]==-1 || val<d[y]) d[y]=val;
}

void dij() {
  memset(d,-1,sizeof d);
  memset(mark,0,sizeof mark);
  
  d[s]=0;
  mark[s]=0;
  for (;;) {
    int minv=-1;
    int mini=-1;
    FOR (i,N) {
      if (!mark[i] && d[i]!=-1 && (minv==-1 || d[i]<minv)) {
	minv=d[i];
	mini=i;
      }
    }
    if (minv==-1) break;
    int x=mini;
    mark[x]=1;
    int i, j, k;
    dec(x, i, j, k);
    //cerr<<i<<" "<<j<<" "<<k<<endl;
    
    if (k==0) {
      if (j>0) go(i,j-1,1,minv+2); //left
      go(i,j,1, minv+light[i][j].hw(minv)+1); //right
      go(i,j,2, minv+light[i][j].vw(minv)+1); //up
      if (i<m-1) go(i+1,j,2,minv+2); //down
    }
    if (k==1) {
      go(i,j,0,minv+light[i][j].hw(minv)+1); //left
      if (j<n-1) go(i,j+1,0,minv+2); //right
      go(i,j,3,minv+light[i][j].vw(minv)+1); //up
      if (i<m-1) go(i+1,j,3,minv+2); //down
    }
    if (k==2) {
      if (j>0) go(i,j-1,3,minv+2); //left
      go(i,j,3, minv+light[i][j].hw(minv)+1); //right
      if (i>0) go(i-1,j,0,minv+2); //up
      go(i,j,0,minv+light[i][j].vw(minv)+1); //down
    }
    if (k==3) {
      go(i,j,2,minv+light[i][j].hw(minv)+1); //left
      if (j<n-1) go(i,j+1,2,minv+2); //right
      if (i>0) go(i-1,j,1,minv+2); //up
      go(i,j,1,minv+light[i][j].vw(minv)+1); //down
    }

  }

}

int main() {

  int nt;
  cin>>nt;
  for (int T=1;T<=nt;T++) {
    cin>>m>>n;
    FOR (i,m)
      FOR (j,n)
      {
	cin>>light[i][j].s>>light[i][j].w>>light[i][j].t;
	light[i][j].proc();
      }
    N=m*n*4;
    s=enc(m-1,0,0);
    t=enc(0,n-1,3);
    dij();
    assert(d[t]!=-1);
    cout<<"Case #"<<T<<": "<<d[t]<<endl;
  }

  return 0;
}
