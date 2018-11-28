#include <iostream>
using namespace std;

int main() {
    
    int T;
    cin >> T;
    for(int c = 1; c <= T; ++c) {
        int N, M;
        cin >> N;
        M = (1 << N);
        int V[1024];
        int k;
        for(int i = 0; i < M; ++i) {
            cin >> V[i];
            V[i] = N - V[i];
        }
        for(int i = 0; i < M - 1; ++i) cin >> k;
        int mx = 0;
        for(int i = 0; i < N; ++i) {
            int step = (1 << (N - i));
    
//cout << "i = " << i << endl;
//cout << "step = " << step << endl;
            for(int j = 0; j < (1<<i); ++j) {
//cout << "j = " << j << endl;
                bool buy = false;
                for(int l = 0; l < step; ++l) {
                    int w = l + j * step;
//cout << "w = " << w << endl;
                    if(V[w] > 0) {
                        buy = true;
                        //break;
                    }
                }
                if(buy) {
                    ++mx;
                    for(int l = 0; l < step; ++l) {
                        int w = l + j * step;
                        if(V[w] > 0) {
                            --V[w];
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n", c, mx * k);
    }
}
