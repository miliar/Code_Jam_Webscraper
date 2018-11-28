#include <iostream>

using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int i = 0; i < T; ++i) {
        long long N, K;

        cin >> N >> K;

        bool result = ((K + 1LL) % (1 << N)) == 0;

        printf("Case #%d: %s\n", i+1, result ? "ON" : "OFF");
    }

    return 0;
}

