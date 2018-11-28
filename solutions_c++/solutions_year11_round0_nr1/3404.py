#include <iostream>
using namespace std;

int Pos(int k)
{
    if (k <= 0)
        return 1;
    if (k == 0)
        return 1;
    return k;
}

int Abs(int k)
{
    if (k < 0)
        return -k;
    return k;
}

int main()
{
    int t;
    cin >> t;
    for (int c = 1; c <= t; c++)
    {
        int n;
        cin >> n;
        int res = 0;
        int last_b = 0, last_o = 0;
        int now_b = 1, now_o = 1;
        while(n--)
        {
            char c;
            int p;
            cin >> c >> p;
            //cout << c << " " << p << endl;
            if (c == 'B')
            {
                int time = Pos(Abs(now_b - p) + 1 - last_b);
                res += time; 
                last_o += time;
                last_b = 0;
                now_b = p;
            }
            else
            {
                int time = Pos(Abs(now_o - p) + 1 - last_o);
                res += time;
                last_b += time;
                last_o = 0;
                now_o = p;
            }
            //cout << res << endl;
        }
        cout << "Case #" << c << ": " << res << endl;
    }
}


