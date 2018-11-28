#include"stdio.h"
#include"stdlib.h"
#include"math.h"
int t,T,n,i,j;
double arr[250],brr[250],sum,tmp;
int cmp(const void *a,const void *b)
{
    if(*(double*)b>*(double*)a) return 1;
    else return -1;
}
int main()
{
//    freopen("2.in","r",stdin);
//    freopen("2.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        sum=0;
        for(i=1;i<=n;i++)
        {
            scanf("%lf",&arr[i]);
            brr[i]=arr[i];
            sum+=arr[i];
        }
        tmp=sum;
        sum*=2;
        qsort(&brr[1],n,sizeof(double),cmp);
        for(i=1,j=n;i<=n;i++)
        {
            if(brr[i]>sum/j)
            {
                sum-=brr[i];
                j--;
            }
            else break;
        }
        //printf("%lf %lf\n",sum,j);
        printf("Case #%d: ",t);
        for(i=1;i<=n;i++)
        {
            if(arr[i]>=sum/j) printf("%lf ",0.0);
            else  printf("%lf ",(sum/j-arr[i])/tmp*100);
        }
        printf("\n");
    }
    scanf(" ");
}
