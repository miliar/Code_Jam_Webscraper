#include <iostream>
#include <vector>
using namespace std;

int dist(int a, int b)
{
    if (a > b)
    {
        return a - b;
    }
    return b - a;
}

int main()
{
    int T, t;
    int N;
    vector<int> orange;
    vector<int> blue;
    vector<char> next2push;
    char c;
    int b;
    int i, j, k;
    int op, bp;
    int ans;
    int d;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> N;
        orange.clear();
        blue.clear();
        next2push.clear();
        for (i = 0; i < N; i++)
        {
            cin >> c >> b;
            if (c == 'O')
            {
                orange.push_back(b);
            }
            else if (c == 'B')
            {
                blue.push_back(b);
            }
            next2push.push_back(c);
        }

        ans = 0;
        op = 1;
        bp = 1;
        i = 0;
        j = 0;
        for (k = 0; k < (int) next2push.size(); k++)
        {
            if (next2push[k] == 'O')
            {
                d = dist(op, orange[i]);
                op = orange[i];
                i++;
                ans += d + 1;
                if (j < (int) blue.size())
                {
                    if (dist(bp, blue[j]) <= d + 1)
                    {
                        bp = blue[j];
                    }
                    else
                    {
                        if (bp < blue[j])
                        {
                            bp += d + 1;
                        }
                        else
                        {
                            bp -= d + 1;
                        }
                    }
                }
            }
            else
            {
                d = dist(bp, blue[j]);
                bp = blue[j];
                j++;
                ans += d + 1;
                if (i < (int) orange.size())
                {
                    if (dist(op, orange[i]) <= d + 1)
                    {
                        op = orange[i];
                    }
                    else
                    {
                        if (op < orange[i])
                        {
                            op += d + 1;
                        }
                        else
                        {
                            op -= d + 1;
                        }
                    }
                }
            }
        }

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

