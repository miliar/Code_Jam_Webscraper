#include<stdio.h>
int main()
{
    int t,temp;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int N;
        scanf("%d",&N);
        int S;
        scanf("%d",&S);
        int p;
        scanf("%d",&p);
        int t_p=0,s_t_p=0;
        int t1,t2;
        for(int j=0;j<N;j++)
        {
            scanf("%d",&temp);
            t1=temp%3;
            t2=temp/3;
            if((t2)>=p)
            {
                t_p++;
            }
            else
            {
                if(((t2)==(p-1)))
                {
                    if(t1==0 && s_t_p<S && (t2)-1>=0)
                    {
                        s_t_p++;
                        t_p++;
                    }
                    else if(t1>0)
                        t_p++;

                }
                else
                {
                    if((((t2)==(p-2)) && (t1==2)) && (s_t_p<S))
                    {
                        s_t_p++;
                        t_p++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",i+1,t_p);
    }
    return 0;
}
