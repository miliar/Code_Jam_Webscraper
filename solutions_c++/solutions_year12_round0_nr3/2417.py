#include<stdio.h>
#include<stdlib.h>
#include<set>

#define pii pair<int,int>

using namespace std;

int p[10];

set<pii> s;

int digit(int x)
{
    int c = 0;
    while(x!=0)
    {
        c++;
        x /= 10;
    }
    return c;
}

int rotate(int x,int d)
{
    return (x%10)*p[d-1]+(x/10);
}

int main()
{
    freopen("C-large.in","rt",stdin);
    freopen("C-large.out","wt",stdout);
    int i,j,k,t,a,b,d,temp;
    p[0] = 1;
    for(i=1;i<8;i++)
        p[i] = p[i-1]*10;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&a,&b);
        s.clear();
        for(j=a;j<=b;j++)
        {
            d = digit(j);
            for(k=1,temp=j;k<d;k++)
            {
                temp = rotate(temp,d);
                if(temp > j && a <= temp && temp <= b)
                    s.insert(pii(j,temp));
            }
        }
        printf("Case #%d: %d\n",i,s.size());
    }
    return 0;
}
