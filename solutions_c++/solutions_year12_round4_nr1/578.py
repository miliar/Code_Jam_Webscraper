#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int f[15000],l[15000],d[15000];
int T;
int n;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for (int ttt=1;ttt<=T;ttt++)
    {
        cin>>n;
        for (int k=1;k<=n;k++)
           scanf("%d%d",&d[k],&l[k]);
        int now=0;
        int nx=d[1];
        cin>>d[n+1];
        int num=1;
        int flag=0;
        while (nx<d[n+1])
        {
            int temp=nx;
            flag=0;
            for (int k=num+1;k<=n+1;k++)
            {
                if (temp-now>=d[k]-temp)
                {
                    nx=d[k];
                    num=k;
                    flag=1;
                }
                else break;
            }
            now=max(temp,nx-l[num]);
            if (!flag) break;
        }
        if (!flag) printf("Case #%d: NO\n",ttt);
        else printf("Case #%d: YES\n",ttt);
    }
    return 0;
}
