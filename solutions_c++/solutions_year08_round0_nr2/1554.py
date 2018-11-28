#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<sstream>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;
void solve(){
  int t;
  scanf("%d",&t);
  int a,b;
  scanf("%d %d",&a,&b);
  int A[25*60]={};
  int B[25*60]={};
  int h,m,H,M;
  for(int i=0;i<a;i++){
    scanf("%d:%d %d:%d",&h,&m,&H,&M);
    A[h*60+m]--;
    B[H*60+M+t]++;
  }
  for(int i=0;i<b;i++){
    scanf("%d:%d %d:%d",&h,&m,&H,&M);
    B[h*60+m]--;
    A[H*60+M+t]++;
  }
  int sa=0,sb=0;
  a=b=0;
  for(int i=0;i<24*60;i++){
    sa+=A[i];
    a<?=sa;
    sb+=B[i];
    b<?=sb;
  }
  printf("%d %d\n",-a,-b);
}
int main(){
  int n;
  scanf(" %d ",&n);
  for(int t=1;t<=n;t++){
    printf("Case #%d: ",t);
    solve();
  }
}
