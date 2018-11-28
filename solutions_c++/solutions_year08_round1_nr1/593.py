#include <iostream>
#include <algorithm>
using namespace std;
long long ans[2][801];
int N;
long long solve() {
    sort(ans[0], ans[0]+N);
    sort(ans[1], ans[1]+N);
    long long an = 0;
    for (int i=0; i<N; i++) {
        an += (ans[0][i]*ans[1][N-1-i]);
    }
    return an;
}
int main() {
    int T;
    cin >> T;
    for (int j=0; j<T; j++) {
        cin >> N;
        for (int i=0; i<N; i++) {
               cin >> ans[0][i];
        }
        for (int i=0; i<N; i++) {
                cin >> ans[1][i];
        }
        cout << "Case #" << j+1 << ": " << solve() << endl;
    }
    return 0;
}
