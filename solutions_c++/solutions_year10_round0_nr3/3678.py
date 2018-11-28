#include<stdio.h>
int cx[1000];
int yunsuan(int r,int k,int n)
{
    int i,zqr,vb,fun;
    int sum=0;
    zqr=0;
    i=0;
    fun=0;
    while(1){
             vb=zqr;
             zqr+=cx[i];
             if(zqr>k)
             {
                      sum+=vb;
                      i=i-1;
                      fun=i;
                      r=r-1;
                      zqr=0;
                      if(r==0) return sum;
             }
             if((i+1)%n==fun)
             {
                       sum+=zqr;
                       i=i;
                       fun=(i+1)%n;
                       r=r-1;
                       zqr=0;
                       if(r==0) return sum;         
             }
             i++;             
             i=i%n;
    }
}
int main()
{
    freopen("d:\C-small-attempt0.in","r",stdin);
    freopen("d:\zqr.out","w",stdout);
    int t,r,k,n;
    int h,tt=0;
    scanf("%d",&t);
    while(1)
    {
            tt++;
            if(tt==t+1) break;
            scanf("%d %d %d",&r,&k,&n);
            for(h=0;h<n;h++)
            {
                            scanf("%d",&cx[h]);           
            }
            printf("Case #%d: %d\n",tt,yunsuan(r,k,n));
    }
	return 0;
}
