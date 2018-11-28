#include<iostream>
#include<cstring>
#include<cstdio>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
int n,s,p,ta[100];
int pan[100];
bool isPosi(int a,int b,int c,int tt){
  if( a + b + c != tt) return false;
  int s[3];
  s[0] = a;
  s[1] = b;
  s[2] = c;
  sort(s,s+3);
  return s[2] - s[0] <= 2;
}
bool isSurp(int a,int b,int c){
  int s[3];
  s[0] = a;
  s[1] = b;
  s[2] = c;
  sort(s,s+3);
  return s[2]-s[0] == 2;
}

int main(){
  int t,k=1;
  cin>>t;
  while(t--){
    cin>>n>>s>>p;
    for(int i = 0 ; i < n;i++)
      scanf("%d",&ta[i]);
    memset(pan,-1,sizeof pan);
    for(int i = 0 ; i < n;i++){
      //not surprise
      for(int a = 0;a <= 10;a++){
        for(int b = 0; b <= 10;b++){
          for(int c = 0;c <= 10;c++){
            if( !isPosi(a,b,c,ta[i]) ) continue;
            if( isSurp(a,b,c) ) continue;
            int maxi = max(a, max(b,c));
            if( maxi < p) continue;
            pan[i] = maxi;
          }
        }
      }

      for(int a = 0;a <= 10;a++){
        for(int b = 0; b <= 10;b++){
          for(int c = 0;c <= 10;c++){
            int sum = a + b + c;
            if( !isPosi(a,b,c,ta[i]) ) continue;
            if( pan[i] != -1) continue;//before more than p
            if( isSurp(a,b,c) && s > 0 ){
              int maxi = max(a, max(b,c));
              if( maxi >= p){
                pan[i] = maxi;
                s--;
              }
            }
          }
        }
      }
    }
    int ans = 0;
    for(int i = 0 ; i < n;i++){
      if( pan[i] >= p){
        ans++;
      }
    }
    printf("Case #%d: %d\n",k++,ans);
  }
  return 0;
}
