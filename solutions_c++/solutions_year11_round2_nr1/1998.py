#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <ctype.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int Ti = 1; Ti <= T; ++Ti) {
        int A[100][110];
        int N;
        cin >> N;
        {
            for(int i = 0; i < N ; ++i) {
                for(int j = 0; j < N ; ++j) {
                    char x;
                    cin >> x;
                    if( x == '1' || x == '0')
                        A[i][j] = x - '0';
                    else
                        A[i][j] = -1;
                }
            }
        }
        double WP[110];
        int played[110];
        {
            for(int i = 0; i < N; ++i) {
                played[i] = 0;
                WP[i] = 0;
                for(int j = 0; j < N; ++j) {
                    if(A[i][j] != -1 ) {
                        played[i]++;
                    }
                    if(A[i][j] == 1) {
                        WP[i]++;
                    }
                }
                WP[i] /= played[i];
            }
        }
        double OWP[110];
        {
            for(int i = 0; i < N; ++i) {
                OWP[i] = 0;
                for(int j = 0; j < N; ++j) {
                    if(A[i][j] != -1) {
                        OWP[i] += (WP[j] *played[j] - (A[i][j] == 1? 0 : 1) ) / (played[j] - 1);                    }
                }
                OWP[i] /= played[i];
            }
        }

        double OOWP[110];
        {
            for(int i = 0; i < N; ++i) {
                OOWP[i] = 0;
                for(int j = 0; j < N; ++j) {
                    if( i != j && A[i][j] != -1)
                        OOWP[i] += OWP[j];
                }
                OOWP[i] /= played[i];
            }
        }

        double RPI[110];
        {
            for(int i = 0; i < N; ++i) {
                RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
            }
        }


        
        cout << "Case #" << Ti << ": " << /* << result << */ std::endl;
        for (int count = 0; count < N; ++count) {
            cout << RPI[count] << std::endl;
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
