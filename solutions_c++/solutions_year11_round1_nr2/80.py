#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>

#define FOR(i,n) for(i=0;i<n;i++)
#define MAXN 111111
#define MAXM 111

using namespace std;

int N,M,size[MAXN],points[MAXN],pointsn[MAXN];
char D[MAXN][11],L[MAXM][30];
bool ok[MAXN];

vector< vector<int> > t,tn,tt,ttn;
vector<int> tmp,tmp2;
int best=-1,besti=0;

void go(char c,int x){
  int i,j,k,p=points[x];
  bool ok=false;;
  FOR(i,t[x].size()){
    FOR(j,size[t[x][i]]){ if(D[t[x][i]][j]==c){ ok=true; break; }}
  }
  if(!ok){
    pointsn[(int)tn.size()]=p;
    tn.push_back(t[x]);
    return;
  }
  tt.clear();
  tt.push_back(t[x]);
  FOR(i,size[t[x][0]]){
    ttn.clear();
    FOR(j,tt.size()){
      tmp.clear();
      tmp2.clear();
      FOR(k,tt[j].size()){
        if(D[tt[j][k]][i]==c) tmp.push_back(tt[j][k]);
        else tmp2.push_back(tt[j][k]);
      }
      if(!tmp.empty()) ttn.push_back(tmp);
      if(!tmp2.empty()) ttn.push_back(tmp2);
    }
    tt=ttn;
  }
  FOR(i,tt.size()){
    ok=false;
    FOR(j,size[tt[i][0]]) if(D[tt[i][0]][j]==c) ok=true;
    if(!ok) pointsn[(int)tn.size()]=p+1;
    else pointsn[(int)tn.size()]=p;
    tn.push_back(tt[i]);
  }
}

int solve(int l){
  int best=-1,besti=0,p,i,j,k;
  t.clear();
  FOR(i,11){
    tmp.clear();
    FOR(j,N) if(size[j]==i) tmp.push_back(j);
    if(!tmp.empty()){
      points[(int)t.size()]=0;
      t.push_back(tmp);
    }
  }
  FOR(i,26){
    tn.clear();
    FOR(j,t.size()) go(L[l][i],j);
    t=tn;
    FOR(j,tn.size()) points[j]=pointsn[j];
  }
  FOR(i,t.size()){
    if(points[i]>best||(points[i]==best&&t[i][0]<besti)){
      best=points[i];
      besti=t[i][0];
    }
  }
  return besti;
}

int main(int argc, char *argv[]){
  int T,t,i;
  scanf("%d",&T); 
  FOR(t,T){
    scanf("%d%d",&N,&M);
    FOR(i,N){
      scanf("%s",D[i]);
      for(size[i]=0;D[i][size[i]]!='\0';size[i]++);
    }
    FOR(i,M) scanf("%s",L[i]);
    printf("Case #%d:",t+1);
    FOR(i,M) printf(" %s",D[solve(i)]);
    printf("\n");
  }
  return 0;
}
