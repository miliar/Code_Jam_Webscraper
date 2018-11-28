#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <cstdlib>


using namespace std;

int player[10005];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);


    int t;
    cin >> t;
    for(int ti = 0; ti < t; ++ti)
    {
        int n, l, h;
        cin >> n >> l >> h;
        for(int i = 0; i < n; ++i)
            cin >> player[i];
        int flag = 1;
        for(int i = l; i <= h && flag; ++i)
        {
            int j;
            for(j = 0; j < n && (player[j] % i == 0 || i % player[j] == 0); ++j);

            if(j == n)
            {
                flag = 0;
                printf("Case #%d: %d\n", ti + 1, i);
            }
        }
        if(flag)
            printf("Case #%d: NO\n", ti + 1);
    }

    return 0;
}
