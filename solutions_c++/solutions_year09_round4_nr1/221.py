#include <iostream>
#include <vector>
using namespace std;

int n,g[100];

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);   
    int t;
    scanf("%d", &t);
    for (int task=0;task<t;task++)
    {
        scanf("%d", &n);
        for (int i=0;i<n;i++)
        {
            char a[100];
            scanf("%s",a);
            g[i]=0;
            for (int j=0;j<n;j++)
                if (a[j]=='1')  g[i]=j;   
        }
        int ret=0;
        for (int i=0;i<n;i++)
            if (g[i]>i)
                for (int j=i+1;j<n;j++)
                    if (g[j]<=i)
                    {
                        for (int k=j;k>i;k--)
                            g[k]=g[k-1];
                        ret+=j-i;
                        break;   
                    }
        printf("Case #%d: %d\n",task+1,ret);
    }
}
