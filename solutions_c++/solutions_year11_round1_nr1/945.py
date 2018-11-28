#include<cstdio>

using namespace std;

bool freecall();
int gcd(int,int);

int main()
{
    int T;
    scanf("%d",&T);
    for (int num=1; num<=T; num++)
    {
        if (freecall())
            printf("Case #%d: Possible\n",num);
        else
            printf("Case #%d: Broken\n",num);
    }
    return 0;
}

int gcd(int x,int y)
{
    if (y==0)
        return x;
    else
        return gcd(y, x%y);
}

bool freecall()
{
    int pd,pg;
    double n;
    scanf("%lf %d %d",&n,&pd,&pg);
    int g = gcd(100,pd);
    int p = pd/g, q = 100/g;
    //printf("%f %d",n,g);
    if (q>n+0.5)
        return false;
    else
    {
        if (pg!=0 && pg!=100)
            return true;
        else if (pg==pd)
            return true;
        else
            return false;
    }
}

