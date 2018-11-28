#include <iostream>

using namespace std;

const int maxn = 1000;

int a[maxn], b[maxn];

bool intersects(int i, int j)
{
    return  (((a[i] < a[j]) && (b[i] > b[j])) ||
             ((a[i] > a[j]) && (b[i] < b[j])));
}

int solve()
{
    int answer = 0;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> a[i] >> b[i];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            if (intersects(i, j)) answer++;
    return answer;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int answer = solve();
        cout << "Case #" << t << ": " << answer << endl;
    }
    return 0;
}
