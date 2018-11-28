#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long n, a, b, A, B, t, i, j, c=1;
    cin >> t;
    while(t--)
    {
        cin >> n >> a >> b;
        A = B = 1;
        int Num2=0, Num5=0, tmp;
        for(tmp=a; tmp % 2 == 0 && Num2 <= 2; tmp /= 2)
            Num2 ++;
        for(tmp=a; tmp % 5 == 0 && Num5 <= 2; tmp /= 5)
            Num5 ++;
        for(i=Num2; i<2; i++)
            A *= 2;
        for(i=Num5; i<2; i++)
            A *= 5;
        if(A > n || (a != 100 && b == 100) || (b == 0 && a != 0))
            printf("Case #%d: Broken\n", c++);
        else
            printf("Case #%d: Possible\n", c++);
    }
}
