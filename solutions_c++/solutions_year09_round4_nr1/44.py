#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
using namespace std;
int n;
char a[110][110];
main(){
  int t;scanf("%d",&t);for(int tt=1;tt<=t;tt++){
    int ans=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf(" %s",a[i]);
    for(int i=0;i<n;i++){
      int first=-1;
      for(int k=i;k<n;k++){
        bool ok=1;
        for(int z=i+1;z<n;z++)ok&=a[k][z]=='0';
        if(ok){first=k;break;}
      }
      assert(first>-1);
      for(int j=first;j>i;j--)for(int k=0;k<n;k++)a[j][k]=a[j-1][k];
      ans+=first-i;
    }
    printf("Case #%d: %d\n",tt,ans);
  }
}

