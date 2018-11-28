#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#define MAXL 1005
#define MAXN 50
using namespace std;

int testcase,K,P[50],N=34,L,t1,t2,ans,indeg[MAXN],outdeg[MAXN];
char S[MAXL];
bool seen[MAXN],C[MAXN][MAXN],visit[MAXN];
vector <int> G[MAXN];

void dfs(int x){
  visit[x] = 1;
  for(vector<int>::iterator it=G[x].begin();it!=G[x].end();++it)
    if(!visit[*it]) dfs(*it);
}

int main(){
  freopen("D-small-attempt1.in","r",stdin);
  freopen("D.out","w",stdout);
  memset(P,-1,sizeof(P));
  P['o'-'a'] = 26;
  P['i'-'a'] = 27;
  P['e'-'a'] = 28;
  P['a'-'a'] = 29;
  P['s'-'a'] = 30;
  P['t'-'a'] = 31;
  P['b'-'a'] = 32;
  P['g'-'a'] = 33;
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
    scanf("%d %s",&K,S);
    for(int i=0;i<N;++i) G[i].clear();
    memset(seen,0,sizeof(seen));
    memset(C,0,sizeof(C));
    memset(indeg,0,sizeof(indeg));
    memset(outdeg,0,sizeof(outdeg));
    memset(visit,0,sizeof(visit));
    ans = 0;
    L = strlen(S);
    for(int i=1;i<L;++i){
      for(int a=0;a<2;++a)
        for(int b=0;b<2;++b){
          seen[S[i-1]-'a'] = 1;
          seen[S[i]-'a'] = 1;
          t1 = (a)?(S[i-1]-'a'):(P[S[i-1]-'a']);
          t2 = (b)?(S[i]-'a'):(P[S[i]-'a']);
          if(t1 >= 0 && t2 >= 0) C[t1][t2] = 1, G[t1].push_back(t2);
        }
    }
    for(int i=0;i<N;++i)
      for(int j=0;j<N;++j)
        if(C[i][j]) ++outdeg[i], ++indeg[j], ++ans;
  //  for(int i=0;i<N;++i)
  //    if(!visit[i] && seen[i]) ++ans,dfs(i);
    t1 = t2 = 0;
    for(int i=0;i<N;++i)
      if(indeg[i] > outdeg[i]) t1 += indeg[i] - outdeg[i];
      else t2 += outdeg[i] - indeg[i];
    printf("Case #%d: %d\n",TC,ans+max(t1,t2)+(t1==0&&t2==0));
  }
}
