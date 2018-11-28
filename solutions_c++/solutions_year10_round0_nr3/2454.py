#include<stdio.h>
using namespace std;
int value[1000];
int que[100000],que2[10000];
int main()
{
    int t;
    scanf("%d",&t);
    int Case=0;
    while(t--)
    {
        int r,k,n;
        scanf("%d%d%d",&r,&k,&n);
        int head,tail;
        head=tail=0;
        for(int i=1;i<=n;++i) 
        {
            scanf("%d",&value[i]);
            que[++tail]=value[i];
        }
        int ans=0;
        for(int i=1;i<=r;++i)
        {
            int temp=0;
            int num=0;
            while(1)
            {
                int t=que[++head];
                num++;
                temp+=t;
                if(temp>k||num>n)
                {
                    --head;
                    break;
                }
                ans+=t;
                que[++tail]=t;
            }
        }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
