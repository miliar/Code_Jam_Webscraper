#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int r = 0; r < T; r++){
        int N, L, H;
        int n[10001] = {0};
        cin >> N >> L >> H;
        for (int i = 0; i < N; i++) cin >> n[i];
        cout << "Case #" << r+1 << ": ";
        bool flag2 = false;
        for (int i = L; i <= H; i++){
            bool flag = true;
            for (int m = 0; m < N; m++){
                if (n[m] % i != 0 && i % n[m] != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cout << i << endl;
                flag2 = true;
                break;
            }
        }
        if (!flag2) cout << "NO" << endl;
    }
    return 0;
}
