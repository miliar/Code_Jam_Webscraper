#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;

#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define DEB 0
#define all(x) x.begin(), x.end()

int main(){
  int T;
  scanf("%d",&T);
  rep(x,T){
    char r;
    int n,p,pb=0,po=0,tmp;
    int blue=1,orange=1,ret=0;

    scanf("%d ",&n);
    rep(i,n){
      scanf(" %c %d ",&r,&p);
      if( r=='O' ){
	tmp = max(abs(p-orange)-pb,0) + 1;
	po += tmp;
	ret += tmp;
	orange = p;
	pb = 0;
      }else{
	tmp = max(abs(p-blue)-po,0) + 1;
	pb += tmp;
	ret += tmp;
	blue = p;
	po = 0;
      }
#if DEB
      printf("ret:%d orange:%d  blue:%d   po:%d   pb:%d\n",ret,orange,blue,po,pb);
#endif
    }
    printf("Case #%d: %d\n",x+1,ret);
  }
  return 0;
}
