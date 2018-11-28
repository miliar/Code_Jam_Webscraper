#include<cstdio>

typedef struct {
    int size;   ///size of group
    int next;   ///how many next should be summed up
    long long int sum;    ///and what is the sum
}group;

group groups[1001];

void print_groups(int N)
{
    for(int i=0;i<N;i++)
        printf("%d %d %d\n",groups[i].size,groups[i].next,groups[i].sum);
    printf("\n");
}

int main()
{
    int T;
    FILE *ptr = fopen("C-large.in","r");
    fscanf(ptr,"%d",&T);
    FILE *out = fopen ("3-large.out","w");
    int caseno=1;
    while(T--)
    {
        int R,k,N;
        fscanf(ptr,"%d %d %d",&R,&k,&N);
        for(int i=0;i<N;i++)
            fscanf(ptr,"%d",&groups[i].size);
        ///construct the circular array
        for(int i=0;i<N;i++)
        {
            long long tempsum = 0;
            int j = i,cntr2;
            for(cntr2=0;cntr2<N;cntr2++)
            {
                if(tempsum+groups[j%N].size > k)
                    break;
                tempsum += groups[j%N].size;
                j++;
            }
            groups[i].sum = tempsum;
            groups[i].next = cntr2;
        }

        unsigned long long ans=0;
        int j=0;
        if(N==1)
            ans = R*groups[0].size;
        else
        {
            for(int i=0;i<R;i++)
            {
                ans+=groups[j].sum;
                j+=groups[j].next;
                j%=N;
            }
        }
        fprintf(out,"Case #%d: %llu\n",caseno++,ans);
    }
    return 0;
}
