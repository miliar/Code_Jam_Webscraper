#include<cstdio>
#include<vector>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
using namespace std;
#define MAX 10000
#define INF 1000000000
int n,m,matched[MAX],dist[MAX];
vector<int> s[MAX];
bool b[MAX];
bool check(int x) {
  b[x]=true;
  for (int i=0; i<s[x].size(); i++) if (s[x][i]!=matched[x]
    && (!matched[s[x][i]] || dist[x]+1==dist[matched[s[x][i]]]
    && !b[matched[s[x][i]]] && check(matched[s[x][i]]))) {
    matched[x]=s[x][i];
    matched[s[x][i]]=x;
    return true;
  }
  return false;
}
int matching() {
  int i,j,k,ans=0;
  vector<int> q;  
  for (i=1; i<=n+m; i++) matched[i]=0;
  while (1) {
    q.clear();
    for (i=1; i<=n; i++) {
      if (!matched[i]) {
        q.push_back(i);
        dist[i]=0;
      } else
        dist[i]=INF;
      b[i]=false;
    }
    for (i=0; i<q.size(); i++) for (j=0; j<s[q[i]].size(); j++) {
      k=s[q[i]][j];
      if (!matched[k]) goto proceed;
      if (dist[q[i]]+1<dist[matched[k]]) {
        q.push_back(matched[k]);
        dist[matched[k]]=dist[q[i]]+1;
      }
    }      
    break;
proceed:
    for (i=1; i<=n; i++) ans+=!matched[i] && check(i);
  }
  return ans;
}
int N,K,p[1010][1010];
main(){
  int t;scanf("%d",&t);for(int tt=1;tt<=t;tt++){
    scanf("%d %d",&N,&K);
    for(int i=0;i<N;i++)for(int j=0;j<K;j++)scanf("%d",&p[i][j]);
    n=m=N;
    for(int i=0;i<MAX;i++)s[i].clear();
    for(int i=0;i<N;i++)for(int j=0;j<N;j++){
      bool less=1;
      for(int k=0;k<K;k++)less&=p[i][k]<p[j][k];
      if(less)s[i+1].push_back(N+j+1);
    }
    printf("Case #%d: %d\n",tt,N-matching());
  }
}

