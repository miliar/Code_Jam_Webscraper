#include <iostream>

using namespace std;

int main ()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        cout << "Case #" << t << ": ";
        int N, K;
        cin >> N >> K;
        K++;

        if (K % (1<<N))
            cout << "OFF" << endl;
        else
            cout << "ON" << endl;
    }

    return 0;
}