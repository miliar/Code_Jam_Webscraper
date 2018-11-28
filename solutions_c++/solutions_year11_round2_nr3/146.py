#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back

int n,m,M;
int ex[20],ey[20];
vector<int> v[100];

int p[300];
int a[200], ans;
bool sol=false;
void run(int x){
  if (sol) return;
  if (x>=n){
    bool b[10]; CLR(b);
    int mx = 0;
    FOR(i,0,n) mx=max(mx,p[i]+1);
    if (ans >= mx) return;

    bool ok=true;
    FOE(i,0,m){
      FOR(j,0,mx) b[j]=0;
      FOR(j,0,v[i].size()) b[p[v[i][j]]]=true;
      int cnt=0; FOR(j,0,mx) cnt+=b[j];
      if (mx != cnt) ok=false;
    }
 //   puts("");
//    FOR(i,0,n) printf("%d ",p[i]); printf(" >>ok=%d\n",ok);;
    if (ok && mx > ans){
      ans = mx;
      FOR(i,0,n) a[i]=p[i];
    }
    if (ans==M) sol=true;
    return;
  }
  FOR(i,0,8){ 
    p[x]=i; 
    run(x+1); 
  }
}

int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    scanf("%d%d",&n,&m);
    FOR(i,0,m) scanf("%d",&ex[i]), ex[i]--;
    FOR(i,0,m) scanf("%d",&ey[i]), ey[i]--;
    FOR(i,0,n) v[0].clear();
    FOR(i,0,n) v[0].PB(i);
    FOR(i,0,m){
      FOE(j,0,i){
        bool b1=0, b2=0;
        FOR(k,0,v[j].size()){
          if (v[j][k]==ex[i]) b1=true;
          if (v[j][k]==ey[i]) b2=true;
        }
        if (!(b1 && b2)) continue;

        vector<int> tmp, tmp2;
        FOR(k,0,v[j].size()){
          if (ex[i]==v[j][k] || v[j][k]==ey[i]){
            tmp2.PB(v[j][k]);
            tmp.PB(v[j][k]);
          }else if (ex[i]<=v[j][k] && v[j][k]<=ey[i]){
            tmp2.PB(v[j][k]);
          }else{
            tmp.PB(v[j][k]);
          }
        }
//        printf(">> %d %d\n",i,j);
        v[i+1] = tmp2;
        v[j] = tmp;
        break;
      }
    }
    M = n;
    FOE(i,0,m) M = min(M, (int)v[i].size());

/*
    printf("M = %d\n",M);
    FOE(i,0,m){
      FOR(j,0,v[i].size()) printf("%d ",v[i][j]); puts("");
    }
    */
    ans = 0;
    sol=false;
    p[0]=0;
    run(1);
    printf("Case #%d: %d\n",ca,ans);
    FOR(i,0,n-1) printf("%d ",a[i]+1); printf("%d\n",a[n-1]+1);
  }
  return 0;
}
