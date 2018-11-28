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

        int m = -1;
        int sum = 0;
        int xsum = 0;
        for (int i = 0; i < n; ++i)
        {
            int c;
            cin >> c;

            if ((i == 0) || (c < m))
            {
                m = c;
            }

            sum += c;
            xsum ^= c;
        }


        cout << "Case #" << k << ": ";

        if (xsum != 0)
        {
            cout << "NO";
        } 
        else
        {
            cout << (sum - m);
        }

        cout << "\n";
         
    }
    return 0;
}
