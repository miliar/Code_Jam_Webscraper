#include <iostream>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int n, k;
    bool flag;

    for (coden = 1; coden <= t; coden++)
    {
        cin >> n >> k;

        flag = true;
        for (int i = 0; i < n; i++) {
            if (!((1 << i) & k)) {
                flag = false;
                break;
            }
        }

        // output result
        cout << "Case #" << coden << ": " << (flag?"ON":"OFF") << endl;
    }
    return 0;
}

