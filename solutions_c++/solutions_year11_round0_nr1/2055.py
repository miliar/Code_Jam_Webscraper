#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int k = 1; k <= T; ++k)
    {
        int n;
        cin >> n;


        int last_pos[2] = {1, 1};
        int last_time[2] = {0, 0};


        for (int i = 0; i < n; ++i)
        {
            char c;
            int pos;
            cin >> c >> pos;
            int rn = (c == 'B');

            last_time[rn] = 1 + max(last_time[rn] + abs(pos - last_pos[rn]), last_time[1-rn]);
            last_pos[rn] = pos;
        }

        cout << "Case #" << k << ": " << max(last_time[0], last_time[1]) << "\n";

    }

    return 0;
}
