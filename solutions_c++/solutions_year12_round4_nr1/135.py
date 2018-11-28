#include <iostream>
#include <cstring>
using namespace std;

#define MAXN 16384

int d[MAXN], l[MAXN], m[MAXN], N;

int main() {
    int i, j, dist, D, T, t;
    bool FLAG;

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> N;
    
        d[0] = l[0] = 0;
        for (i=1; i<=N; i++) {
            cin >> d[i];
            cin >> l[i];
        }
        cin >> D;
    
        FLAG = false;
        memset(m, -1, sizeof(m)); m[1] = 0;
        for (i=1; i<=N; i++) {
            if (m[i] == -1) continue;
    
            dist = min(l[i], d[i]-d[m[i]]);
            if (d[i] + dist >= D) FLAG = true;
    
            for (j=i+1; j<=N && d[i]+dist>=d[j]; j++) {
                if (m[j] == -1) m[j] = i;
            }
        }
        cout << "Case #" << t << ": ";
        if (FLAG) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

    return 0;
}
