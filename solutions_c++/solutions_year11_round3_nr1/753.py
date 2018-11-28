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
        char A[100][110];
        int R, C;
        bool possible = true;
        cin >> R >> C;
        {
            for(int i = 0; i < R ; ++i) {
                for(int j = 0; j < C ; ++j) {
                    cin >> A[i][j];
                }
            }
        }
        {
            for(int i = 0; i < R - 1 ; ++i) {
                for(int j = 0; j < C - 1 ; ++j) {
                    if(A[i][j] == '#' &&  A[i+1][j] == '#' && A[i+1][j+1] == '#' && A[i][j+1] == '#') {
                        A[i][j] = '/';
                        A[i][j+1] = '\\';
                        A[i+1][j] = '\\';
                        A[i+1][j+1] = '/';
                    }
                }
            }
        }
        {
            for(int i = 0; i < R ; ++i) {
                for(int j = 0; j < C ; ++j) {
                    if(A[i][j] == '#') { 
                        possible = false;
                    }
                }
            }
        }

        cout << "Case #" << Ti << ": " << /* << result << */ std::endl;
        {
            if(possible) {

                for(int i = 0; i < R ; ++i) {
                    for(int j = 0; j < C ; ++j) {
                        cout << A[i][j];
                    }
                    cout << std::endl;
                }
            }
            else {
                cout << "Impossible" << std::endl;
            }
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
