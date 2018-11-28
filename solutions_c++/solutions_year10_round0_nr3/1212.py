#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long> groups, C;

int main(void) {
    int t, T;
    long R, k, N;
    long i, j;
    long M, P, Q, r;
    vector<long>::iterator a;
    cin >> T;
    for(t=1; t<=T; t++) {
        cin >> R >> k >> N;
        groups.resize(N+1);
        C.resize(N+1);
        for(i=1; i<=N; i++)
            cin >> groups[i];
        C[0] = 0;
        for(i=1; i<=N; i++)
            C[i] = C[i-1] + groups[i];
        M = 0;
        Q = 0;
        for(i=0; i<R; i++) {
            if(k >= C[N])
                M = C[N]*R;
            else {
                P = Q + k;
                if(P > C[N]) {
                    P = P % C[N];
                    a = lower_bound(C.begin(), C.end(), P);
                    if(C[int(a - C.begin())] != P)
                        a--;
                    r = (C[N] - Q) + C[int(a - C.begin())];
                    M = M + (C[N] - Q) + C[int(a - C.begin())];
                    Q = C[int(a - C.begin())];
                }
                else {
                    a = lower_bound(C.begin(), C.end(), P);
                    if(C[int(a - C.begin())] != P)
                        a--;
                    r = (C[int(a - C.begin())] - Q);
                    M = M + (C[int(a - C.begin())] - Q);
                    Q = C[int(a - C.begin())];
                }
                //cout << "Taking " << r << " people." << endl;
            }
        }
        cout << "Case #" << t << ": " << M << endl;
    }
    return 0;
}

