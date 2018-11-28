#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int fun(int n, int l, int r)
{
    int t = 1, a = 0;;
    while(n >= t)
        t *= 10, a++;
    t /= 10;

    int ans = 0;
    int tmp = n;
    do
    {
        int b = tmp%10;
        tmp /= 10;
        if(b == 0)continue;
        tmp += b*t;
        if(tmp > n && tmp >= l && tmp <= r)
            ans ++;
    }while(tmp != n);

//    if(ans != 0)
//        cout << n << endl;


    return ans;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int cas; cin >> cas;
    for(int i = 1; i <= cas; i++)
    {
        int a, b;cin >> a >> b;
        int ans = 0;
        for(int j = a; j <= b; j++)
        {
            ans += fun(j, a, b);
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}











