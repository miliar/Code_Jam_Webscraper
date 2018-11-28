#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
struct Score
{
    int a,b,c;
}t[50];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int n,m,s,p;
    while(scanf("%d",&n)!=EOF)
    {
        int w = 1;
        while(n--)
        {
            int i,j;
            scanf("%d%d%d",&m,&s,&p);
            for(i=0;i<m;i++)
            {
                int temp;
                scanf("%d",&temp);
                if(temp%3 == 0)
                    t[i].a = t[i].b = t[i].c  = temp/3;
                else if(temp%3 == 1)
                    t[i].a = t[i].b = t[i].c  = temp/3,t[i].a++;
                else if(temp%3 == 2)
                    t[i].a = t[i].b = t[i].c  = temp/3,t[i].a++,t[i].b++;
            }

            for(i=0,j=0;i<m&&j<s;i++)
            {
                if(t[i].a==p-1&&t[i].a==t[i].b&&t[i].a!=0&&t[i].a!=10)
                    t[i].a++,t[i].b--,j++;
            }
            int sum = 0;
            for(i=0;i<m;i++)
                if(t[i].a>=p&&t[i].a<=10)
                    sum++;
            printf("Case #%d: %d\n",w++,sum);
        }
    }
    return 0;
}
