#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int solve() {
    int result = 0;
    int N;
    cin >> N;
    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) { cin >> A[i] >> B[i]; }
    for (int i = 0; i < N; ++i) {
        for (int j = i+1; j < N; ++j) {
            if (B[i] > B[j] && A[i] < A[j]) {
                result++;
            } else if (B[i] < B[j] && A[i] > A[j]){
                result++;
            }
        }
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        cout << "Case #" << times << ": " << solve() << '\r' << endl;
    }
    return 0;
}
