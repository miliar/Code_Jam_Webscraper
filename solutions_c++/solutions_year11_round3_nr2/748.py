#include <iostream>
#include <string>
#include <limits.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int Ti = 1; Ti <= T; ++Ti) {
        long long A[1000];
        long long L, t, N, C;
        cin >> L >> t >> N >> C;
        for(int Ci = 0; Ci < C; ++Ci) {
            cin >> A[Ci];
        }
        float min_time = LLONG_MAX;
        if(L == 0) {
            float time = 0;
            for(int k = 0; k < N; ++k) {
                time += A[k%C] * 2;
            }
            min_time = time;
        } else if (L == 1) {
            for(int i = 0; i < N; ++i) {
                float time = 0;
                for(int k = 0; k < N; ++k) {
                    if(k == i) {
                        if(t < time) {
                            time += A[k%C];
                        }
                        else if( t >= time && t < time + A[k%C]*2) {
                            time = t + (time + A[k%C]*2 - t)/2;
                        } else {
                            time += A[k%C]*2;
                        }
                    }
                    else {
                        time += A[k%C] * 2;
                    }
                }
                if(min_time > time) {
                    min_time = time;
                }
            }
        } else {
            for(int i = 0; i < N - 1; ++i) {
                for(int j = i + 1; j < N; ++j) {
                    float time = 0;
                    for(int k = 0; k < N; ++k) {
                        if(k == i || k == j) {
                            if(t < time) {
                                time += A[k%C];
                            }
                            else if( t >= time && t < time + A[k%C]*2) {
                                time = t + (time + A[k%C]*2 - t)/2;
                            } else {
                                time += A[k%C]*2;
                            }
                        }
                        else { 
                            time += A[k%C]*2;
                        }
                    }
                    if(min_time > time) {
                        min_time = time;
                    }
                }
            }
        }
        cout << "Case #" << Ti << ": " << (long long)min_time << std::endl;
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
