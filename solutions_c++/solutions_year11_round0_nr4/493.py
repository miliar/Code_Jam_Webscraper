#include<stdio.h>
double f[1010];
int a[1010];
int main(){
    f[0]=f[1]=0;
    double sum=0;
    for(int n=2;n<=1000;n++){
       f[n]=2*sum/(n-1)+1;
       sum+=f[n];   
    }
    int times,n;
    scanf("%d",&times);
    for(int tm=1;tm<=times;tm++){
            scanf("%d",&n);        
            for(int i=1;i<=n;i++)scanf("%d",&a[i]);
            double res=0;
            for(int i=1;i<=n;i++){
                    if(!a[i])continue;
                    int j=i,n=0;
                    do{
                       int t=a[j];
                       a[j]=0;   
                       j=t;
                       n++;
                    }while(j!=i);        
                    if(n>1)res+=f[n]+1;
            }
            printf("Case #%d: %.6lf\n",tm,res);
    }
    return 0;
}
