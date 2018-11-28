#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        int R, k, N;

        cin >> R >> k >> N;

        vector<int> g;

        g.reserve(N);

        for(int j = 0; j < N; j++)
        {
            int g_i;

            cin >> g_i;

            g.push_back(g_i);
        }

        int euros = 0;
        int c = 0; // position dans le vector.

        for(int j = 0; j < R; j++)
        {
            int r = k;
            int init = c; // position initiale.

            while(r - g[c] >= 0)
            {
                r -= g[c];
                euros += g[c];

                c++;
                c %= N;

                if(c == init) break;
            }
        }

        cout << "Case #" << (i + 1) << ": " << euros << endl;
    }

    return 0;
}

