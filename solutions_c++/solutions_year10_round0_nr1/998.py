#include <iostream>

using namespace std;

int main() {
    unsigned int T;
    unsigned int N, K;
    int x;

    cin >> T;

    for(unsigned int t = 1; t <= T; t++) {
        cin >> N >> K;
        cout << "Case #" << t << ": ";

        x = K % (1 << N);
        if (x+1 == 1<<N)
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }

    return 0;
}
