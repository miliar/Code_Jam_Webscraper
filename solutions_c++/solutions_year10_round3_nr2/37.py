#include <iostream>

using namespace std;

int solve()
{
    long long L, P, C, K = 0, answer = 0;
    cin >> L >> P >> C;
    for (long long i = L; i*C < P; i *= C)
        K++;
    if (K == 0)
        return 0;
    answer = 1;
    for (long long i = 1; i*2 <= K; i *= 2)
        answer++;
    return answer;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long long answer = solve();
        cout << "Case #" << t << ": " << answer << endl;
    }
    return 0;
}
