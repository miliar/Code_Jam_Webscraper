#include <iostream>
#include <string>
using namespace std;

string solve(long long n, long long k) {
    if (k%2 == 0) return "OFF";
    long long times = (1 << n) - 1;
    if (k >= times) {
        long long sub = k - times;
        long long mod = sub % (times+1);
        if (mod == 0) return "ON";
    }
    return "OFF";
}

int main() {
    int n;
    cin >> n;
    for (int times = 1; times <= n; ++times) {
        long long N, K;
        cin >> N >> K;
        cout << "Case #" << times << ": " << solve(N, K) << '\r' << endl;
    }
    return 0;
}
