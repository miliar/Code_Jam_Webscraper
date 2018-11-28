#include <iostream>

using namespace std;

int main()
{
    int Nc; cin >> Nc;
    for (int i = 0; i < Nc; i++) {
        long long N, K;
        cin >> N >> K;
        cout << "Case #" << i+1 << ": " << (K > 0 && (K % (1LL << N)) == (1LL << N) - 1 ? "ON" : "OFF") << endl;
    }
    return 0;
}
