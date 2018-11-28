#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int test = 0; test < t; ++test)
    {
        int n, k;
        cin >> n >> k;
        string result = ((k % (1 << n)) == (1 << n) - 1) ? "ON" : "OFF";
        cout << "Case #" << test + 1 << ": " << result << endl;
    }

    return 0;
}
