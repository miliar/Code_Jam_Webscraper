#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        int N, K;
        cin >> N >> K;
        puts((++K % (1<<N) == 0) ? "ON" : "OFF");
    }
}
