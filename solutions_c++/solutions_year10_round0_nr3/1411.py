#include<stdio.h>
#include<stdlib.h>

int temp[100],temp1[100],arr[100];

int main()
{
    freopen("C_Small.in","r",stdin);
    freopen("C_small_out_2.txt","w",stdout);
    int test,_case=1,i,j,ii,jj,R,K,N,total,rem;

    scanf("%d",&test);

    while(test--)
    {
        scanf("%d %d %d",&R,&K,&N);
        for(i=0;i<N;i++)
            scanf("%d",&arr[i]);

        total=0;
        for(i=0;i<R;i++)
        {
            rem=K;
            ii=jj=0;
            for(j=0;j<N;j++)
            {
                if(arr[j]>rem)
                {
                    for(j;j<N;j++)
                        temp[jj++]=arr[j];
                    break;
                }
                rem=rem-arr[j];
                total+=arr[j];
                temp1[ii++]=arr[j];
            }
            for(j=0;j<ii;j++)
                temp[jj++]=temp1[j];
            for(j=0;j<N;j++)
                arr[j]=temp[j];
        }
        printf("Case #%d: %d\n",_case++,total);
    }


    return 0;
}
