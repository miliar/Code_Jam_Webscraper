#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1010;

int a[maxn];
int n, k, r;

void Solve()
{
    long long ret = 0;
    int pos = 0;
    for(int i = 0; i < r; i ++)
    {
        int tmp = 0;
        int cnt = 0;
        for(int j = pos;; j ++)
        {
            if(j == n)
                j = 0;
            cnt ++;
            tmp += a[j];
            if(tmp > k)
            {
                tmp -= a[j];
                pos = j;
                break;
            }
            if(cnt == n)
            {
                pos = j;
                break;
            }
        }
        ret += tmp;
//        cout << "tmp: " << tmp << endl;
//        cout << ret << endl;
    }

    printf("%I64d\n", ret);
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t ++)
    {
        printf("Case #%d: ", t);
        scanf("%d %d %d", &r, &k, &n);
        for(int i = 0; i < n; i ++)
            scanf("%d", &a[i]);

        Solve();
    }
}
