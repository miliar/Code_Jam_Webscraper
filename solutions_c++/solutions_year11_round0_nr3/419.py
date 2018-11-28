#include <iostream>

using namespace std;

int main()
{
    int t, n;
    int candy;
    int wrongSum, correctSum;
    int min;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n;

        wrongSum = correctSum = 0;
        min = 1000001;

        for (int j = 0; j < n; j++)
        {
            cin >> candy;
            wrongSum ^= candy;
            correctSum += candy;
            if (min > candy)
                min = candy;
        }

        cout << "Case #" << i + 1 << ": ";
        if (wrongSum != 0)
            cout << "NO";
        else
            cout << correctSum - min;

        cout << endl;
    }

    return 0;
}
