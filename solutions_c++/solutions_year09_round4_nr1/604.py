#include <iostream>
#include <string>
using namespace std;

int T;
int N;
string m[50];
int r[50];
int ans;

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> m[i];
            r[i] = -1;
            for (int j = N-1; j >= 0; j--)
                if (m[i][j] == '1') {
                    r[i] = j;
                    break;
                }
        }
        
        ans = 0;
        for (int i = 0; i < N; i++)
            for (int j = i; j < N; j++)
                if (r[j] <= i) {
                    int tmp = r[j];
                    for (int k = j; k > i; k--) {
                        r[k] = r[k-1];
                        ans++;
                    }
                    r[i] = tmp;
                    break;
                }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
