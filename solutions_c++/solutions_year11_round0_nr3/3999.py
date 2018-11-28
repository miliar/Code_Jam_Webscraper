#include<iostream>

using namespace std;

#define max(a,b) (a<b?b:a)

int T,n;
long a[20],m;

int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> a[i];
        
        m = 0;
        for (long i = 1, N = ((1<<n)-1); i < N; i++) {
            long ta = 0, tA = 0, tb = 0, tB = 0;
            for (int j = 0; j < n; j++) {
                if (((i>>j)&1)==1) {
                                   ta ^= a[j];
                                   tA += a[j];
                                   }
                else {
                     tb ^= a[j];
                     tB += a[j];
                     }
            }
            if (tb == ta && m < max(tA,tB)) m = max(tA,tB);
        }
        cout << "Case #" << t << ": ";
        if (m == 0) cout << "NO";
        else cout << m;
        if (t < T) cout << endl; 
    }
    fclose(stdout);
    return 0;
}
