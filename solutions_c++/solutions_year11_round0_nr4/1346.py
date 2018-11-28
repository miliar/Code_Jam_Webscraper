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

int a[1010];
int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    int n; scanf("%d",&n);
    FOR(i,0,n) scanf("%d",&a[i]);
    int cnt=0;
    FOR(i,0,n) cnt+=(a[i]!=i+1);
    /*
    int cnt=0;
    FOR(i,0,n){
      FOR(j,i+1,n){
        if (a[j]==i+1){
          swap(a[j],a[i]);
          cnt++;
          break;
        }
      }
    }
    */
    printf("Case #%d: %d.000000\n",ca,cnt);
  }
  return 0;
}
