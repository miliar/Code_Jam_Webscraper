#include <iostream>
#include <cmath>
using namespace std;

int pows[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int rotate(int a, int pos, int size)
{
    return a / pows[pos] + (a % pows[pos]) * pows[size-pos];
}

int main ()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t += 1)
    {
        int a, b;
        cin >> a >> b;
        int s = int(floor(log10(a)))+1;
        int result = 0;
        for (int n = a; n < b; n += 1)
        {
            for (int j = 1; j < s; j += 1)
            {
                int m = rotate(n, j, s);
                if (n < m && m <= b)
                {
                    bool found = false;
                    for (int k = 1; k < j; k += 1)
                    {
                        if (rotate(n, k, s) == m)
                            found = true;
                    }
                    if (!found)
                        result += 1;
                }
            }
        }
        cout << "Case #" << (t+1) << ": " << result << endl;
    }
}
