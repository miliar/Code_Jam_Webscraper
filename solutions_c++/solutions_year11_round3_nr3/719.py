#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int Ti = 1; Ti <= T; ++Ti) {
        int A[1000];
        int result = 0;
        int N, L, H;
        bool possible = false;
        cin >> N >> L >> H;
        for(int Ni = 0; Ni < N; ++Ni) {
            cin >> A[Ni];
        }

        for (int i = L; i <= H; ++i) {
            bool flag = true;
            for(int j = 0; j < N; ++j) {
                if(A[j] % i != 0 && i % A[j] != 0) {
                    flag = false;
                    break;
                }
            }
            if(flag == true) {
                result = i;
                possible = true;
                break;
            }
        }
    
        if(possible) {
            cout << "Case #" << Ti << ": " << result << std::endl;
        }
        else {
            cout << "Case #" << Ti << ": " << "NO" << std::endl;
        }
    }

    return 0;
}

/* For 2D arrays, if need
for(int i = 0; i < x; ++i) {
    for(int j = 0; j < x; ++j) {
        cin >> A[i][j];
    }
}
*/
