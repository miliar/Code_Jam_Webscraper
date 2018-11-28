#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

char p[3000];
int f[30][30];
string a[5005],patt,tmp;
int n,d,l,ll,x,j,i,last,len,ans,test,nn,pp;
typedef struct {
  int t[26];
  bool b;
} node;
node t[5000];

void dfs(int k,int pp) {
  if (pp==0) return;
  if (k==len+1) {
    ++ans;
    return;
  }
  for (int j=1; j<=f[k][0]; ++j)
    if (t[pp].t[f[k][j]]) dfs(k+1,t[pp].t[f[k][j]]);
}
int main() {
  freopen("poj.in","r",stdin);
  freopen("poj.out","w",stdout);
  cin>>ll>>d>>n;
  t[0].t[0]=0;
  nn=1;
  for (i=1; i<=d; ++i) {
    cin>>a[i];
    pp=1;
    for (j=0; j!=a[i].size(); ++j) {
      if (t[pp].t[a[i][j]-'a']==0) {
        ++nn;
        t[pp].t[a[i][j]-'a']=nn;
      }
      pp=t[pp].t[a[i][j]-'a'];
    }
    t[pp].b=true;
  }     
  for (test=1; test<=n; ++test) {
    printf("Case #%d: ",test);
    cin>>patt;
    l=patt.size();
    for (i=0; i!=l; ++i)
      p[i+1]=patt[i];
    last=-1; len=0;
    memset(f,0,sizeof(f));
    for (i=1; i<=l; ++i)
      if (p[i]=='(') last=i;
      else if (p[i]==')') {
             ++len;
             f[len][0]=i-last-1;
             for (j=last+1; j<i; ++j)
               f[len][j-last]=p[j]-'a';
             last=-1;
           }
           else if (last==-1) {
                  ++len;
                  f[len][0]=1;
                  f[len][1]=p[i]-'a';
                }
    if (len!=ll) {
      printf("0\n");
      continue;
    }
    ans=0;
    /*
    for (i=1; i<=f[1][0]; ++i) {
      tmp=f[1][i];
      dfs(2,tmp);
    }
    */
    dfs(1,1);
    printf("%d\n",ans);
  }
  return 0;
}
    
        
        
    
    
