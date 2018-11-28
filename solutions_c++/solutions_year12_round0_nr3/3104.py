#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
bool flag[2000005];
int main(){
    int T,a,b,c[10],cas=0;
  //  freopen("C-small-attempt0.in","r",stdin);
  //  freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        int ans=0;
        scanf("%d%d",&a,&b);
        for(int i=a;i<b;i++){
            int cnt=0,t=i;
            while(t){
               c[cnt++]=t%10;
               t/=10;
            }
            for(int j=0;j<cnt/2;j++)
               swap(c[j],c[cnt-1-j]);  
            memset(flag,false,sizeof(flag));         
            for(int j=1;j<cnt;j++){
                int sum=0;
              
                for(int k=0;k<cnt;k++)
                    sum=sum*10+c[(j+k)%cnt];
                if(sum>i&&sum<=b&&flag[sum]==false){
          //        printf("%d %d\n",i,sum);
                    flag[sum]=true;
                    ans++;
                }
            }
        } 
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}   
