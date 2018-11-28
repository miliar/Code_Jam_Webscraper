#include <iostream>
#define N 500
#define M 100003
using namespace std;

int t, tt;
int T[N][N];
int C[N][N];
int main() {

    for(int i=0; i<N; i++) {
        T[i][i] = 0;
        T[i][i-1] = 1;
        T[i][1] = 1;
        T[i][0] = 0;
        C[i][i] = 1;
    }

    for(int i=1; i<N; i++) {
        for(int j=0; j<=i; j++) {
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % M;
//            cout << C[i][j] << " ";
        }
 //       cout << endl;
    }

    for(int i=2; i<N; i++) {
        for(int j=1; j<i-1; j++) {
            for(int k=1; k<=j; k++) {
                T[i][j] += (T[j][k] * C[i-j-1][j-k-1]) % M;
            }
        }
    }

    cin >> t;


    for(int tt=1; tt<=t; tt++) {
        int n;
        cin >> n;
        int cnt = 0;
        for(int i=1; i<n; i++) {
            cnt = (cnt + T[n][i]) % M;
          //  cout << T[n][i] << " ";
        }
        //cout << endl;

        cout << "Case #" << tt << ": " << cnt << endl;
    }
}
