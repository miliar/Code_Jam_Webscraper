#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
int A,B,d,len;
int dig(int x)
{
    int r = 1;
    len = 0;
    while(x != 0)
    {
        len++;
        r *= 10;
        x /= 10;
    }
    return r/10;
}
int cal(int x)
{
    int rem,ret;
    ret = 0;rem = x;
    while(1)
    {
        //s = x/d;
        //x -= s*d;
        //x = x * 10 + s;
        x = (x % 10)*d + x/10;
        if (x > rem && x <= B)
            ret++;
        if (x == rem)   break;
    }
    return ret;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    int ans;
    scanf("%d",&T);
    for (int ca = 1; ca <= T; ca++)
    {
        scanf("%d%d",&A,&B);
        ans = 0;
        d = dig(A);
        for (int i = A; i <= B; ++i)
            ans += cal(i);
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}


