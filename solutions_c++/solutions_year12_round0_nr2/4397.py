#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
    int T;
    cin >> T;
    ofstream out("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\out.txt");
    for(int i = 1; i <= T; i++) {
        int N, S, P;
        int t[200];
        cin >> N >> S >> P;
        for(int j = 0; j < N; j++) {
            cin >> t[j];
        }
        sort(t, t + N);
        int sum = 0;
        int res = S;
        int v1, v2;
        if(P == 0) {
            v1 = v2 = 0;
        } else if(P == 1) {
            v1 = v2 = 1;
        } else {
            v1 = 3*P - 2;
            v2 = 3*P - 4;
        }
        for(int j = N-1; j >= 0; j--) {
            if(t[j] >= v1) sum++;
            else if(t[j] >= v2 && res > 0) {
                sum++;
                res--;
            }
            else break;
        }
        out << "Case #" << i << ": " << sum << endl;
    }
    return 0;
}
