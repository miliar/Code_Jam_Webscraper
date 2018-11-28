#include <iostream>
#include <cassert>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int n;
    int smallest;
    int value;
    int sum;
    int wrongsum;

    for (coden = 1; coden <= t; coden++)
    {
        cin >> n;
        smallest = 2000000; // 2e6
        sum = 0;
        wrongsum = 0;
        for (int i = 0; i < n; i++) {
            cin >> value;
            wrongsum ^= value;
            sum += value;
            if (value < smallest) {
                smallest = value;
            }
        }

        // output result
        cout << "Case #" << coden << ": ";
        if (wrongsum != 0) {
            cout << "NO" << endl;
        } else {
            cout << (sum - smallest) << endl;
        }
    }
    return 0;
}

