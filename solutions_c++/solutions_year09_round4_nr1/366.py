#include <iostream>
#include <cassert>

using namespace std;

int main()
{
    int minRow[100];
    int t;
    cin >> t;
    for (int caseNum = 1; caseNum <= t; caseNum++)
    {
        int n;
        cin >> n;

        //cerr << "Case " << caseNum << endl;

        for (int i = 0; i < n; i++)
        {
            int min = 0;
            cin >> ws;
            for (int j = 0; j < n; j++)
            {
                char x;
                cin >> x;
                if (x == '1')
                    min = j;
            }
            minRow[i] = min;
            //cerr << minRow[i] << endl;
        }

        int moves = 0;

        for (int i = 0; i < n; i++)
        {
            int j;
            for (j = i; j < n; j++)
                if (minRow[j] <= i)
                    break;
            assert(j <= n);
            moves += j - i;
            while (j != i)
            {
                swap(minRow[j], minRow[j - 1]);
                j--;
            }
        }

        cout << "Case #" << caseNum << ": " << moves << endl;
    }

    return 0;
}
