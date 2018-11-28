#include <iostream>
#include <algorithm>
using namespace std;

int v[100];

int main ()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t += 1)
    {
        int N, S, p;
        cin >> N >> S >> p;
        for (int i = 0; i < N; i += 1)
        {
            cin >> v[i];
        }

        if (p == 0)
        {
            cout << "Case #" << (t+1) << ": " << N << endl;
            continue;
        }

        sort(v, v+N);

        int result = 0;

        for (int i = N-1; i >= 0; i -= 1)
        {
            v[i] -= p;
            if (v[i] >= 2*(p-1))
                result += 1;
            else if (S > 0 && p >= 2 && v[i] >= 2*(p-2))
            {
                result += 1;
                S -= 1;
            }
        }

        cout << "Case #" << (t+1) << ": " << result << endl;
    }
}
