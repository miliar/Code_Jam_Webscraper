#include <iostream>
#include <bitset>
using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int n, k;
        cin >> n >> k;
        int mask = (1 << n) - 1;
        cout << "Case #" << (test + 1) << ": " << ((k & mask) == mask ? "ON" : "OFF") << endl;
    }
}
