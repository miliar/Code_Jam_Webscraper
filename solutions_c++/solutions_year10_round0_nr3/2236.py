#include <iostream>
#include <deque>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 0; t < T; t++)
    {
        int R, k, N;
        cin >> R >> k >> N;
        deque<int> q;
        int g;
        for(int n = 0; n < N; n++)
        {
            cin >> g;
            q.push_back(g);
        }

        int Tot = 0;
        for(int r = 0; r < R; r++)
        {
            int tot = 0;
            deque<int> qq;
            while(true)
            {
                if(q.empty())
                    break;
                int val = q.front();
                if(tot + val <= k)
                {
                    tot += val;
                    q.pop_front();
                    qq.push_back(val);
                }
                else
                    break;
            }
            Tot += tot;
            q.insert(q.end(), qq.begin(), qq.end());
        }

        cout << "Case #" << t + 1 << ": " << Tot << endl;
    }
    return 0;
}

