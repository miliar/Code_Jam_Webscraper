#include <cstdio>
#include <iostream>
#include <map>
#define LL long long
using namespace std;

int T;
int ten[10];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ten[0] = 1;
    for (int i = 1; i <= 8; ++i) ten[i] = ten[i - 1] * 10;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        LL ans = 0;
        int a, b;
        scanf("%d%d", &a, &b);
        for (int x = a; x <= b; ++x)
        {
            int len = 0, num = x;
            while (num)
            {
                len++;
                num /= 10;
            }
            num = x;
            for (int i = 1; i < len; ++i)
            {
                int tmp1 = num / ten[i], tmp2 = (num % ten[i]);
                if (tmp1 == tmp2) break;
                int tmp = tmp1 + tmp2 * ten[len - i];

                if (tmp > x && tmp <= b)
                {
                    ans++;
                }
            }
        }
        cout << "Case #" << cas << ": " << ans << endl;
    }
    return 0;
}