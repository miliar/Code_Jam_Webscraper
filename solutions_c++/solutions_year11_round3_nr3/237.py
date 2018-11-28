#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int n,l,h;
int mem[10005];
int c;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    int q=1;
    scanf("%d",&t);
    while(t--)
    {
        int x=-1;
        scanf("%d%d%d",&n,&l,&h);
        int i,j;
        for(i=0;i<n;i++)
        {
            scanf("%d",&mem[i]);
        }
        for(i=l;i<=h;i++)
        {
            c=0;
            x=-1;
            for(j=0;j<n;j++)
            {
                if((i%mem[j]==0)||(mem[j]%i==0))
                {
                    c++;
                }
                if(c==n)
                {
                    x=i;
                }
            }
            if(x!=-1)
            {
                break;
            }
        }
        printf("Case #%d: ",q++);
        if(x==-1)
        {
            printf("NO\n");
        }
        else
        {
            printf("%d\n",x);
        }

    }
    return 0;
}
