#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;

char ts[100];

void huan(int a,int b){
      int i,mini,k,j;
      char ch;
      if(a>=b) return;
      for(i=b-1;i>=a;i--){
            mini=2000;
            for(j=i+1;j<=b;j++)
                  if(ts[i]<ts[j] && mini>ts[j]){
                        mini=ts[j];
                        k=j;
                  }
            if(mini!=2000){
                  ch=ts[i];ts[i]=ts[k];ts[k]=ch;
                  huan(i+1,b);
            }
            //if(flag) break;
      }
}
int main() {
      //unsigned long long x;
      int cases,ca,i,j,k,mini;
      char ch;
      bool flag;
      freopen("B-large.in","r",stdin);
      freopen("B-large.out","w",stdout);
      scanf("%d",&cases);
      for(ca=1;ca<=cases;ca++){
            //scanf("%lld",x);
            scanf("%s",ts);
            flag=false;
            while(!flag){
                  for(i=strlen(ts)-2;i>=0;i--){
                        mini=2000;
                        for(j=i+1;j<=strlen(ts)-1;j++)
                              if(ts[i]<ts[j] && mini>ts[j]){
                                    mini=ts[j];
                                    k=j;
                              }
                        if(mini!=2000){
                              ch=ts[i];ts[i]=ts[k];ts[k]=ch;
                              sort(ts+i+1,ts+strlen(ts));
                              //huan(i+1,strlen(ts)-1);
                              flag=true;
                              break;
                        }
                        //if(flag) break;
                  }
                  if(flag) break;
                  for(i=strlen(ts)+1;i>=1;i--) ts[i]=ts[i-1];
                  ts[0]='0';
            }
            printf("Case #%d: %s\n",ca,ts);
      }
      return 0;
}