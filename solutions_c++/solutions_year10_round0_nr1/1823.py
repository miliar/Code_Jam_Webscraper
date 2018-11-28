#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int caseNum = 1; caseNum <= t; caseNum++)
    {
        long long n, k;
        cin >> n >> k;

        long long mod = (1 << n);
        cout << "Case #" << caseNum << ": ";
        if (((k + 1) % mod) == 0)
            cout << "ON";
        else
            cout << "OFF";
        cout << endl;
    }

    return 0;
}
