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

int n,a[2000];
int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    scanf("%d",&n);
    FOR(i,0,n) scanf("%d",&a[i]);
    int xx = 0;
    FOR(i,0,n) xx ^= a[i];
    printf("Case #%d: ",ca);
    if (xx != 0) printf("NO\n");
    else{
      sort(a,a+n);
      long long ans = 0;
      FOR(i,1,n) ans += a[i];
      printf("%lld\n",ans);
    }
  }
  return 0;
}
