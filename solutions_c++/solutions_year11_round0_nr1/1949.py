#include <iostream>
#include <stdlib.h>

using namespace std;

#define convert_to_int(c)  ((c) == 'B' ? 1 : 0)
#define counterpart(i)  ((i) == 1 ? 0 : 1)

int main()
{
    int T, t;
    cin >> T;
    for (t = 0; t < T; ++t)
    {
        int N, n;
        cin >> N;
        int cur_rob;
        int cur_pos[2] = {1, 1};
        int prev_moment[2] = {0, 0};
        int cur_moment = 0;
        for (n = 0; n < N; ++n)
        {
            char R;
            int P;
            cin >> R;
            cin >> P;
            cur_rob = convert_to_int(R);
            int diff_moment = cur_moment - prev_moment[cur_rob];
            int diff_pos = abs(P - cur_pos[cur_rob]) + 1;
            if (diff_moment < diff_pos)
            {
                cur_moment += diff_pos - diff_moment;
            }
            else
            {
                ++cur_moment;
            }
            prev_moment[cur_rob] = cur_moment;
            cur_pos[cur_rob] = P;

        }
        cout << "Case #" << t + 1 << ": " << cur_moment << endl;
    }

    return 0;
}
