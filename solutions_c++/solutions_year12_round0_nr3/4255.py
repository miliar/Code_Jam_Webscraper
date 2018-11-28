#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int a,b;
int deal(int n)
{
    int re = 0;
    int len = 0;
    int tt = n;
    while(tt)
    {
        len++;tt /= 10;
    }
    int ttt = n;
    int pow = 1;
    for(int i = 1;i < len;i++)
        pow = pow*10;
    for(int i = 0;i < len-1;i++)
    {
        tt = n%10;
        n = n/10+tt*pow;
        if(ttt < n && n <= b && n >= a) re++;
    }
    return re;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin );
    //freopen("in.in","r",stdin );
    freopen("out.out","w",stdout );

    int t;
    cin >> t;
    for(int cas = 1;cas <= t;cas++)
    {

        cin >> a >> b;
        int re = 0;
        for(int i = a;i <= b;i++)
        {
            re += deal(i);
        }
        cout << "Case #" << cas << ": ";
        cout << re << "\n";
    }
    return 0;
}
