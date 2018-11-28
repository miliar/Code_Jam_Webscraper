#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
using namespace std;

int a[100];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
    {
        int A,B,ret=0;
        scanf("%d%d",&A,&B);
        for (int i=max(A,12);i<=B;i++)
        {
            int j;
            for (j=1000000;j>A;j/=10);
            int cnt=0;
            for (int k=10;j>0;j/=10,k*=10)
            {
                int t=i%j*k+i/j;
                bool dup=false;
                for (int z=0;z<cnt;z++)
                {
                    if (a[z]==t)
                    {
                        dup=true;
                        break;
                    }
                }
                if (!dup&&t>i&&t<=B)
                {
                    a[cnt++]=t;
                    ret++;
                }
            }
        }
        printf("Case #%d: %d\n",i,ret);
    }
}
