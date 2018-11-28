#include <iostream>

using namespace std;

#define fin "a.in"

int T, N, K;

int main()
{
        freopen(fin,"r",stdin);
        freopen("output.txt", "w", stdout);

        cin >> T;

        for (int t = 1; t <= T; ++t)
        {
            cin >> N >> K;

            cout << "Case #" << t << ": ";

            if (( K % (1 << N) ) == ((1 << N) - 1) )
                    cout << "ON\n";
            else
                    cout << "OFF\n";
        }

        return 0;
}
