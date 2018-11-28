#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;

    for(int number = 1; number <= T; number++)
    {
        int N, S, P;
        cin >> N >> S >> P;

        int count[31];
        for(int c = 0; c <= 30; c++)
        {
            count[c] = 0;
        }

        for(int c = 0; c < N; c++)
        {
            int i;
            cin >> i;
            count[i]++;
        }

        int ans = 0;

        // Enough without surprise
        for(int c = max(0, 3*P-2); c <= 30; c++)
        {
            ans += count[c];
        }

        int temp = 0;
        for(int c = max(2, 3*P-4); c < 3*P-2; c++)
        {
            temp += count[c];
        }

        ans += min(temp, S);

        cout << "Case #" << number << ": " << ans << "\n";
    }
}
