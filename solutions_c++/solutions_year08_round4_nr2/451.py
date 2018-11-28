#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int c = 1; c <= n; c++)
    {
        int n, m, a;
        cin >> n >> m >> a;
        bool done = false;
        if (a != 0)
        {
            for (int x0 = 0; x0 <= 0; x0++)
                for (int y0 = 0; y0 <= 0; y0++)
                    for (int x = 0; x <= n; x++)
                    {
                        if (x == x0)
                            continue;
                        for (int y = 0; y <= m; y++)
                            for (int x2 = 0; x2 <= n; x2++)
                            {
                                int y2 = (a + (x2 - x0) * (y - y0)) / (x - x0) + y0;
                                if ((y2 >= 0 && y2 <= m) && (a == ((x - x0) * (y2 - y0) - (x2 - x0) * (y - y0))))
                                {
                                    cout << "Case #" << c << ": " << x0 << " " << y0 << " " << x << " " << y << " " << x2 << " " << y2 << endl;
                                    done = true;
                                    goto done;
                                }
                            }
                    }
        done:;
        if (!done)
            cout << "Case #" << c << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << c << ": 0 0 0 0 0 0" << endl;
        }
        //cerr << c << endl;
    }
    return 0;
}
