#include <iostream>
using namespace std;

int main()
{
    long long int total;
    int the_xor;
    int the_minimum;
    int t, T;
    int c;
    int i;
    int N;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        total = 0;
        the_xor = 0;
        the_minimum = 1000000000;
        cin >> N;
        for (i = 1; i <= N; i++)
        {
            cin >> c;
            total += c;
            the_xor ^= c;
            if (c < the_minimum)
            {
                the_minimum = c;
            }
        }
        cout << "Case #" << t << ": ";
        if (the_xor != 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << total - the_minimum << endl;
        }
    }

    return 0;
}

