#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int T,nowCase = 0;
    scanf("%d",&T);
    while (T--)
    {
        int n,maxi = 0x7fffffff,sum = 0,realsum = 0;
        scanf("%d",&n);
        for (int a,i = 0;i < n;++i)
        {
            scanf("%d",&a);
            sum ^= a;
            realsum += a;
            if (a < maxi) maxi = a;
        }
        cout << "Case #" << ++nowCase << ": ";
        if (sum != 0)
            cout << "NO" << endl;
        else
            cout << realsum - maxi << endl;
    }
    return 0;
}
