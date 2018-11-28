#include <iostream>

// no input checking seems needed in the contest's context
// assumes ints have 32 bits or more
// no need for the extra bit "unsigned" would provide

using namespace std;

void solve(int i, int n, int k)
{
    int j ((1 << n) - 1);
    k &= j;
    cout << "Case #" << i << ": " << (k == j ? "ON" : "OFF") << endl;
}

int main()
{
    int t, n, k;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cin >> n >> k;
        solve(i, n, k);
    }
}

