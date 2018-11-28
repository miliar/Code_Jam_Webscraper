#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<cstdio>
#include<map>
using namespace std;

int main()
{   freopen("Cnow.txt","r",stdin);
    freopen("Cnow1.txt","w",stdout);
    int i,j,m,n,N,L,H,k,flag;
    int ar[500];
    k=1;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d%d%d",&N,&L,&H);

        for(i=0;i<N;i++)
        {
            scanf("%d",&ar[i]);
        }

        int ans;
        for(i=L;i<=H;i++)
        {   flag=1;
            for(j=0;j<N;j++)
            {
                if(ar[j]%i==0 || i%ar[j]==0)continue;
                flag=0;break;


            }
            if(flag)
            {   ans=i;
                goto out;
            }

        }
        out:;
        if(flag==1)
        {
            printf("Case #%d: %d\n",k++,ans);
        }
        else
        {
            printf("Case #%d: NO\n",k++);
        }

    }

    return 0;
}
