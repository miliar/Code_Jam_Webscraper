#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-8; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-8; }

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    int n;
    scanf("%d",&n);
    int a[n];
    char s[1000];
    for (int i=0;i<n;i++){
      scanf("%s",s);
      a[i]=0;
      for (int j=0;j<n;j++){
        if (s[j]=='1')a[i]=j;
      }
    }

    int ans=0;
    //for (int j=0;j<n;j++)printf("%d ",a[j]); puts("");
    for (int i=0;i<n;i++){
      if (a[i]>i){
        //find a a[j]<=i
        int j;
        for (j=i+1;j<n && a[j]>i;j++);
        int x = a[j];
        for (int k=j;k>i;k--){
          a[k]=a[k-1];
          ans++;
        }
        a[i]=x;
      }
     // for (int j=0;j<n;j++)printf("%d ",a[j]); puts("");
    }

    printf("Case #%d: %d\n",ti,ans);
  }

  return 0;
}
