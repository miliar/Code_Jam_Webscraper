#include <iostream>
using namespace std;

#define MAXN 1024

int main() {
    int i, N, e[MAXN], o[MAXN], tmp, t, T;
    double  p[MAXN];
    bool flag;

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> N;
        for (i=0; i<N; i++) cin >> e[i];
        for (i=0; i<N; i++) {cin >> tmp; p[i] = 1.0 - tmp/100.0;}
        
        for (i=0; i<N; i++) o[i] = i;
    
        do {
            flag = false;
            for (i=0; i<N-1; i++) {
                if (e[o[i]] + e[o[i+1]]*p[o[i]] > e[o[i+1]] + e[o[i]]*p[o[i+1]]) {
                    swap(o[i], o[i+1]);
                    flag = true;
                    break;
                }
            }
        } while (flag); 
    
        cout << "Case #" << t << ":";
        for (i=0; i<N; i++) cout << ' ' << o[i];
        cout << endl;
    }

    return 0;
}
