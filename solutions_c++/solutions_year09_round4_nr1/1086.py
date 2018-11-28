#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
char cmd[44];
string a[44];
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n;
    scanf("%d",&n);
    int i;
    for(i=0;i<n;++i){
      scanf("%s",cmd);
      a[i]=cmd;
    }
    int j,k,ans=0;
    for(i=0;i<n;++i){
      for(j=i+1;j<n;++j)
        if(a[i][j]==49)break;
      if(j<n){
        for(j=i+1;j<n;++j){
          for(k=i+1;k<n;++k)
            if(a[j][k]==49)
              break;
          if(k==n){
            for(k=j;k>i;--k)
              swap(a[k],a[k-1]);
            ans+=j-i;
            break;
          }
        }
      }
    }
    printf("Case #%d: %d\n",testi,ans);
  }
  return 0;
}