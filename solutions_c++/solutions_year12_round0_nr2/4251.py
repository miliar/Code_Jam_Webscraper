#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>

using namespace std;

int dfs(int sum, int &sup, int p)
{
    //驚かない場合
    for (int i = 10; i >= 0; i--)
    {
        for (int j = i; j >= i - 1 && j >= 0; j--)
        {
            for (int k = i; k >= i - 1 && k >= 0; k--)
            {
                //cout << i << ' ' << j << ' ' << k << endl;
                if (i+j+k==sum)
                {
                    //cout << i << ' ' << j << ' ' << k << endl;
                    if (i >= p) return 1;
                }
            }
        }
    }
    //もしも驚いた人がいなかったら0をreturn
    if (sup == 0) return 0;

    //驚く場合
    for (int i = 10; i >= 0; i--)
    {
        for (int j = i; j >= i - 2 && j >= 0; j--)
        {
            for (int k = i; k >= i - 2 && k >= 0; k--)
            {
                if (i+j+k==sum)
                {
                    if(i >= p)
                    {
                        sup--;
                        return 1;
                    }
                }
            }
        }
    }
    return 0;
}

int main()
{
    int T, N, S, p, a;
    cin >> T;

    for(int t = 0; t < T; t++)
    {
        cin >> N >> S >> p;

        int c = 0;
        int s = S;
        for(int b = 0; b < N; b++)
        {
            cin >> a;
            c += dfs(a, s, p);
        }

        printf("Case #%d: %d\n", t + 1, c);
    }
}
