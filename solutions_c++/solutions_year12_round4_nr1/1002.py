#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T;
    int N;
    int D;
    vector<int> l;
    vector<int> d;
    vector<int> lowest;
    bool ans;

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        l.resize(N);
        d.resize(N);
        lowest.resize(N);
        for (int i = 0; i < N; i++)
        {
            cin >> d[i] >> l[i];
            lowest[i] = -1;
        }
        cin >> D;

        lowest[0] = d[0];
        for (int i = 0; i < N - 1; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                if (lowest[i] >= d[j] - d[i])
                {
                    int new_lowest = d[j] - d[i];
                    if (l[j] < new_lowest)
                    {
                        new_lowest = l[j];
                    }
                    // Reach the next vine
                    if (new_lowest > lowest[j])
                    {
                        lowest[j] = new_lowest;
                    }
                }
            }
        }

        ans = false;
        for (int i = 0; i < N; i++)
        {
            if (lowest[i] >= D - d[i])
            {
                ans = true;
                break;
            }
        }
        cout << "Case #" << t << ": " << (ans?"YES":"NO") << endl;
    }

    return 0;
}

