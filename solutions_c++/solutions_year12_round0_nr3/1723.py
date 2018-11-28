#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int ans = 0;
        int A, B;
        cin >> A >> B;
        char *w = new char[20000001];
        for (int i = A; i <= B; ++i)
        {
            if (w[i] == 1) continue;
            w[i] = 1;
            int j = i;   
            int k = 0;
            int rt[10];
            int r = 1;
            while (j != 0)
            {
                rt[k] = j % 10;
                j /= 10;
                ++k;
            }
            for (int j = 0; j < k - 1; ++j)
            {
                if (rt[j] == 0)continue;
                int l = j;
                int ni = 0;
                for (int o = 0; o < k; ++o)
                {
                    ni = ni * 10 + rt[l];
                    --l;
                    if (l < 0) l = k - 1;
                }
                if ((ni > B) || (ni < A)) continue;
                if (w[ni] == 0)
                {
                    w[ni] = 1;
                    ++r;
                }
            }
            ans += r * (r - 1) / 2;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}