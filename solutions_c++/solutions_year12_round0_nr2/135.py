#include <iostream>
using namespace std;

bool can_get_best_result_without_surprise(int n, int p)
{
    // Minimum total score to get best result p is (p-1) + (p-1) + p
    return n >= 3*p-2;
}

bool can_get_best_result_with_surprise(int n, int p)
{
    if (p < 2)
    {
        // Cannot get surprising result with p = 0 or 1
        return false;
    }
    // Minimum total score to get best result p is (p-2) + (p-2) + p
    return n >= 3*p-4;
}

int main()
{
    int T, t;
    int N;
    int S;
    int p;
    int ans;
    int i;
    int n;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> N >> S >> p;
        ans = 0;
        for (i = 0; i < N; i++)
        {
            cin >> n;
            if (can_get_best_result_without_surprise(n, p))
            {
                ans++;
            }
            else if (S > 0 && can_get_best_result_with_surprise(n, p))
            {
                S--;
                ans++;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

