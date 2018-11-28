#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T, t;
    cin >> T;
    for (t = 0; t < T; ++t)
    {
        int N, n;
        cin >> N;
        vector<uint64_t> val;
        val.reserve(N);
        uint64_t sum_xor = 0;
        for (n = 0; n < N; ++n)
        {
            uint64_t C;
            cin >> C;
            val.push_back(C);
            sum_xor ^= C;
        }
        cout << "Case #" << t + 1 << ": ";
        if (sum_xor != 0)
        {
            cout << "NO" << endl;
            continue;
        }
        sort(val.begin(), val.end());
        uint64_t max_sum = 0;
        int i;
        for (i = 1; i < N; ++i)
        {
            max_sum += val[i];
        }
        cout << max_sum << endl;
    }
    return 0;
}
