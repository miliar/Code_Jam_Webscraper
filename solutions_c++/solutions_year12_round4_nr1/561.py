#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <cstring>
#include <cstdio>

using namespace std;


int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int N;
        cin >> N;
        int d[10001];
        int l[10001];
        for (int i = 0; i < N; ++i) cin >> d[i] >> l[i];
        int D;
        cin >> D;
        int r[10001] = {0};
        r[0] = d[0];
        for (int i = 1; i < N; ++i)
        {
            r[i] = -1;
            for (int j = 0; j < i; ++j)
            {
                if (r[j] == -1) continue;
                if (d[i] - d[j] <= r[j])
                {
                    int k = min(d[i] - d[j], l[i]);
                    if (r[i] < k)
                        r[i] = k;
                }
            }
        }
        bool poss = false;
        for (int i = 0; i < N; ++i)
        {
            if (r[i] + d[i] >= D) poss = true;
        }
        if (poss) cout << "Case #" << t << ": YES"<< endl;
        else cout << "Case #" << t << ": NO"<< endl;
    }
    return 0;
}