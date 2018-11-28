#include "iostream"
using namespace std;

int main()
{
        freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t = 0;
    scanf("%d",&t);

    for(int ti=1;ti<=t;ti++)
    {
            int n,tmp;
            int m=10000000,sum=0,ysum=0;
            scanf("%d",&n);
            for(int i =0;i<n;i++)
            {
                    scanf("%d",&tmp);
                    if(tmp<m) m = tmp;
                    ysum ^= tmp;
                    sum += tmp;
            }
            printf("Case #%d: ",ti);
            if(ysum!=0)
              printf("NO\n");
            else
              printf("%d\n",sum-m);
            
    }
    return 0;
}
