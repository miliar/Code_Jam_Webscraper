#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

char a[300];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
    {
        int N,S,p;
        scanf("%d %d %d",&N,&S,&p);
        int ret=0;
        for (int j=0;j<N;j++)
        {
            int x;
            scanf("%d",&x);
            if (p+max(0,p-1)*2<=x)
                ret++;
            else
            if (S>0&&p+max(0,p-2)*2<=x)
            {
                ret++;
                S--;
            }
        }
        printf("Case #%d: %d\n",i,ret);
    }
}
