#include <iostream>
using namespace std;

int main()
{
    int i;
    int t, T;
    int N;
    int m;
    int ans;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> N;
        ans = 0;
        for (i = 1; i <= N; i++)
        {
            cin >> m;
            if (m != i)
            {
                ans++;
            }
        }
        cout << "Case #" << t << ": " << ans << ".000000" << endl;
    }

    return 0;
}

