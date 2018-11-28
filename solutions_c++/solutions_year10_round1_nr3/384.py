#include<iostream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<utility>
#include<algorithm>
#include<queue>
#include<stack>
#include<list>
#include<vector>
#include<map>
#include<set>
using namespace std;

template<class T>
bool chkmax(T&a,T b){return a<b?a=b,1:0;}
template<class T>
bool chkmin(T&a,T b){return a>b?a=b,1:0;}



bool judge(int a,int b){
  int t;
  double d;
  if(a<b)swap(a,b);

  d=(double)a/b-(double)b/a;
  t=(int)d;

  if(a%b==0 || t)
    return true;
  else
    return false;
}
bool solve(int n,int m){
  if(n<m)swap(n,m);
  if(m%n==0)return false;
  if(n/m>=2)return true;
  return !solve(m,n-m);
}
int main(){
//	freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);

  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int a1,a2,b1,b2;
    scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
    int cnt=0;
    int i,j;
    for(i=a1;i<=a2;++i){
      for(j=b1;j<=b2;++j){
        cnt+=solve(i,j);
      }
    }
    printf("Case #%d: %d\n",++ca,cnt);
  }
  return 0;
}
