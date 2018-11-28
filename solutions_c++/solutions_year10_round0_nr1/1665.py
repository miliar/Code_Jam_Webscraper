#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int N, K;
        cin >> N >> K;
        int nmb = K % (1 << N);
        if (nmb == (1 << N) - 1)
            cout << "Case #" << testCase << ": ON" << endl;
        else
            cout << "Case #" << testCase << ": OFF" << endl;

    }
    return 0;
}
