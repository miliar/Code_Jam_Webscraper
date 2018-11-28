#include <iostream>
#include <string>

using namespace std;

int main ()
{
    int T, N, S, p;
    int t;
    cin >> T;
    for (int i =0; i < T; i++)
    {
        cin >> N >> S >> p;
        int upper = p * 3 - 2;
        int lower = p > 1 ? upper - 2 : upper;
        int c = 0;
        for (int j = 0; j < N; j++)
        {
            cin >> t;
            if ( t >= upper)
            {
               ++c;
            }
            else if ( t >= lower && S > 0)
            {
                --S;
                ++c;
            }
        }

        cout << "Case #" << i+1 << ": " << c << endl;
    }
}
