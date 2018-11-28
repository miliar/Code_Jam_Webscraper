#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

struct
{
    int A,B;
}building[1010];


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int test_case,count_test_case;
    int N,i,j,num;

    scanf("%d",&test_case);
    for(count_test_case=1;count_test_case<=test_case;count_test_case++)
    {
        printf("Case #%d: ",count_test_case);

        //memset(f,0,sizeof(f));
        scanf("%d",&N);

        for(i=0;i<N;i++)
            scanf("%d%d",&building[i].A,&building[i].B);

        num=0;
        for(i=0;i<N;i++)
            for(j=i+1;j<N;j++)
                if((building[i].A-building[j].A)*(building[j].B-building[i].B)>0)
                    num++;

        printf("%d",num);

        printf("\n");
    }
}
