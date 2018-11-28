#include<stdio.h>
#include<algorithm>
using namespace std;
int num[110];
int main()
{
    int T;
    int n;
    int p;
    int s,i;
    int cnt=1;
    freopen("B-small-attempt2.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        scanf("%d",&s);
        scanf("%d",&p);
        for(i=0;i<n;i++)
            scanf("%d",&num[i]);
        int res=0;
        sort(num,num+n);
        for(i=n-1;i>=0;i--)
        {
            int a=num[i]/3;
            int b=num[i]%3;
            if((a>=p)||(b&&(a+1)>=p))
                res++;
            else if(s)
            {
                if((!b&&a+1>=p&&a>=1)||(b==2&&a+2>=p&&a>=1))
                {
                    s--;
                    res++;
                }
            }
        }
        printf("Case #%d: %d\n",cnt++,res);
    }
}
