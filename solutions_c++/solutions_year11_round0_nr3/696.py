#include <iostream>

using namespace std;

int sum;
int minn;
int ans;


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out2","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);

        int n;
        minn=123456789;
        sum=0;
        ans=0;

        scanf("%d",&n);
        for(int j=0;j<n;j++)
        {
            int a;
            scanf("%d",&a);
            sum+=a;
            ans^=a;
            minn=min(minn,a);
        }

        if(ans!=0)
        printf("NO\n");
        else
        {
            printf("%d\n",sum-minn);
        }
    }
    return 0;
}
