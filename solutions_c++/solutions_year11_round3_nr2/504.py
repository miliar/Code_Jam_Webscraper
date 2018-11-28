#include<iostream>
using namespace std;

#define MAXN 1002

int dis[MAXN];
int f[MAXN];
int sum[MAXN];

int main()
{
//    freopen("B.in","r",stdin);
//    freopen("B.out","w",stdout);
    
    int T;
    cin>>T;
    int num=1;
    while(T--){
        int L,N,C;
        long long t;
        scanf("%d%I64d%d%d",&L,&t,&N,&C);
//        cin>>L>>t>>N>>C;
        int i,j;
        double res,tmp,tmp2;
        for(i=0;i<C;i++)
          cin>>f[i];
        for(i=0;i<N;i++)
          dis[i]=f[i%C];
        sum[0]=0;
        for(i=1;i<=N;i++)
          sum[i]=sum[i-1]+dis[i-1]*2;
        if(L==0){
           printf("Case #%d: %d\n",num++,sum[N]);
        }
        else if(L==1){
                 int res1=sum[N];
                 for(i=0;i<N;i++){
                    if(t<sum[i+1]){
                       int t1;
                       if(t>sum[i])
                          t1=(int)t-sum[i];
                       else t1=0;
                       if(t1&1) continue;
                       t1/=2;
                       t1=dis[i]-t1;
                       t1=sum[N]-t1;
                       if(t1<res1) res1=t1;
                    }
                 }  
                 printf("Case #%d: %d\n",num++,res1);
             }
             else{
                  res=sum[N];
                  for(i=0;i<N;i++){
                     if(t<sum[i+1]){
                        if(t>sum[i])
                           tmp=t*1.0-sum[i];
                        else 
                           tmp=0;
                        tmp/=2;
                        tmp=dis[i]*1.0-tmp;
                        for(j=i+1;j<N;j++){
                           if(t<sum[j+1]-tmp){
                              if(t>(sum[j]-tmp))
                                 tmp2=t*1.0-(sum[j]-tmp);
                              else tmp2=0;
                              tmp2/=2;
                              tmp2=dis[j]*1.0-tmp2;
                              tmp2=sum[N]*1.0-tmp-tmp2;
                              if(tmp2<res) res=tmp2;
                           }
                        }
                     }
                  }
                  printf("Case #%d: %.0lf\n",num++,res);
             }
    }
}
