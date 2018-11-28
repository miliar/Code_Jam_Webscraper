#include <iostream>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int n;
    int v;
    int d; // how many integers does not on the right place

    for (coden = 1; coden <= t; coden++)
    {
        cin >> n;
        d = 0;
        for (int i = 0; i < n; i++) {
            cin >> v;
            if ((i+1) != v) {
                ++d;
            }
        }

        // output result
        cout << "Case #" << coden << ": " << d << endl;
    }
    return 0;
}

