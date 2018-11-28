#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int N, S, p;
        cin >> N >> S >> p;
        int ans = 0;
        for (int i = 0; i < N; ++i)
        {
            int l;
            cin >> l;
            if (l / 3 >= p)
            {
                ans++;
                continue;
            }
            if (l == 0) continue;
            if ((l % 3 != 0) && (l / 3 + 1 >= p))
            {
                ans++;
                continue;
            }
            if ((((l % 3 == 2) && (l / 3 + 2 >= p)) || ((l % 3 == 0) && (l / 3 + 1 >= p))) && (S > 0))
            {
                ans++;
                --S;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}