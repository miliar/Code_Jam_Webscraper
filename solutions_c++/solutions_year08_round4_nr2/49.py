#include <iostream>

using namespace std;

int square2(int x1, int y1, int x2, int y2, int x3, int y3)
{
    return (x2-x1)*(y1+y2) + (x3-x2)*(y2+y3) + (x1-x3)*(y1+y3);
}

void solve(int N, int M, int A)
{
    for (int x1=0; x1 <= N; x1++)
    for (int x2=0; x2 <= N; x2++)
    for (int y1=0; y1 <= M; y1++)
    for (int y2=0; y2 <= M; y2++)
    {
        if (square2(0, 0, x1, y1, x2, y2) == A)
        {
            cout << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
            return;
        }
    }

    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;
    for (int i=1; i <= T; i++)
    {
        int N, M, A;
        cin >> N >> M >> A;
        cout << "Case #" << i << ": ";
        solve(N, M, A);
    }

}
