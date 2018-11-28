#include <iostream>

using namespace std;

typedef unsigned long u32;

int main()
{
    u32 t;
    cin >> t;

    for(u32 i = 0; i < t; ++i)
    {
        u32 n, k;
        cin >> n >> k;

        u32 pow = 1;
        pow <<= n;

        bool on = (k % pow == pow - 1);
        cout << "Case #" << (i+1) << ": " << (on ? "ON" : "OFF") << endl;
    }

    return 0;
}
