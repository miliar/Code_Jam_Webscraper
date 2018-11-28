
#include <iostream>
#include <vector>

using namespace std;

int N;
int C[1000];

void solve() {
    cin >> N;
    int total = 0;
    int sum = 0;
    int smallest = 100000000;
    for(int i = 0; i < N; i++) {
        cin >> C[i];
        total ^= C[i];
        sum += C[i];
        if(C[i] < smallest)
            smallest = C[i];
    }

    if(total != 0) {
        cout << "NO" << endl;
    }
    else {
        cout << sum - smallest << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
