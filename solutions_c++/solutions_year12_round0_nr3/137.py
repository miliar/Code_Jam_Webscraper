#include <iostream>
#include <set>
using namespace std;

int main()
{
    int t, T;
    int A, B;
    int digits;
    int temp;
    int i, j;
    int multiplier;
    long long int ans;
    set<int> counted;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> A >> B;
        ans = 0;
        // number of digits
        temp = A;
        digits = 0;
        multiplier = 1;
        while (temp > 0)
        {
            digits++;
            temp /= 10;
            multiplier *= 10;
        }
        multiplier /= 10;
        for (i = A; i <= B; i++)
        {
            temp = i;
            counted.clear();
            for (j = 0; j < digits - 1; j++)
            {
                // rotate
                temp = (temp % 10) * multiplier + temp / 10;
                if (temp > i && temp <= B)
                {
                    counted.insert(temp);
                }
            }
            ans += counted.size();
        }
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

