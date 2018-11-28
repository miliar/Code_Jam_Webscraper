#include <iostream>
using namespace std;

long long N, M, A;

void solve()
{
        bool flag = false;
        int x1, y1, x2, y2;
        for (x1 = 1; x1<=N; x1++)
            for (y1 = 0; y1<=M; y1++)
                for (x2 = 0; x2<=N; x2++)
                    for (y2 = 1; y2<=M; y2++)
                    {
                        if (abs(x1*y2-x2*y1)==A)
                        {
                            flag = true;
                            cout << "0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
                            return;
                        }
                    }
        cout << "IMPOSSIBLE" << endl;
}

int main()
{
        freopen("B-small-attempt0.in", "r", stdin);
    freopen("B1.out", "w", stdout);
    int task;
    cin >> task;
    for (int cc = 1; cc<=task; ++cc)
    {
        cout << "Case #" << cc << ": ";
        cin >> N >> M >> A;
        solve();
    }

}
