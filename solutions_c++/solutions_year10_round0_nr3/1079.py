#include<cstdio>
long long int t,r,n,k,a[2005],p,sum,b[2005],c[2005],ind,u,ac,tmp,j;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-output-large.out","w",stdout);
    scanf("%I64d",&t);
    for (long long tt=1; tt<=t; tt++){
        scanf("%I64d%I64d%I64d",&r,&k,&n);
        for (long long i=1; i<=n; i++){
            scanf("%d",&a[i]);
            a[n+i]=a[i];
            b[i]=0;    
        }
        p=0; a[0]=0; sum=0;
        for (long long i=1; i<=n; i++){
            while (p<n+i-1&&sum+a[p+1]<=k)
                  sum+=a[++p];
            a[i]=sum;
            sum-=a[n+i];
            c[i]=p+1>n?p+1-n:p+1;
        }
        ind=1; sum=0;u=1;
        while (b[u]==0){
            sum+=a[u];
            b[u]=ind++;
            u=c[u];
        }
        --ind; ac=0;
        if (r<=ind){
           ind=1;
           for (long long i=1; i<=r; i++){
               ac+=a[ind];
               ind=c[ind];
           }            
        }
        else{
             j=1;
             for (long long i=1; i<b[u]; i++){
                 ac+=a[j];
                 j=c[j];
             }
             r-=(b[u]-1);
             tmp=ind-b[u]+1;
             tmp=(r%tmp);
             sum=0; j=u;
             for (long long i=b[u]; i<=ind; i++){
                 sum+=a[j];
                 if (i-b[u]+1==tmp) ac+=sum;
                 j=c[j];
             }
             ac+=r/(ind-b[u]+1) * sum;
        }
        printf("Case #%I64d: %I64d\n",tt,ac);
    }
    return 0;    
}
