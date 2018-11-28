#include<stdio.h>
#include<stdlib.h>
int n,T,t,N,S,p,sum;
int N1[101];

int cmp(const void*a,const void*b)
{
    return *(int *)b-*(int *)a;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    t=1;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d %d %d",&N,&S,&p);
        for(int i=0;i<N;++i)
        {
            scanf("%d",&N1[i]);
        }
        qsort(N1,N,sizeof(N1[0]),cmp);
       // for(int i=0;i<N;++i)printf("%d\n",N1[i]);
        sum=0;
        for(int i=0;i<N;++i)
        {
            if(N1[i]>=p*3-2)sum++;
            else if((N1[i]>=p*3-4)&&(S>0)&&(p*3-4>0)){sum++;S--;}
        }
        printf("Case #%d: %d\n",t++,sum);
    }
    return 0;
}
