#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> V;

int S[31];
int WS[31];
int f (int x, int s) {
    if (s == 1) {
        return S[x];
    } else {
        return WS[x];
    }
}

int main () {
    V v(3);
    for(v[0] = 0; v[0] <= 10; v[0] ++)
    for(v[1] = 0; v[1] <= 10; v[1] ++)
    for(v[2] = 0; v[2] <= 10; v[2] ++) {
        int sum = v[0]+v[1]+v[2];

        V vv(v);
        sort(vv.begin(), vv.end());

        if(vv[2] <= vv[0]+1)
            WS[sum] = max(WS[sum], vv[2]);

        if(vv[2] <= vv[0]+2)
            S[sum] = max(S[sum], vv[2]);
    }


    int T;
    cin >> T;

    int tt = 0;
    while(T --) {
        tt ++;

        int n, s, p;
        cin >> n >> s >> p;

        vector<int> v(n);
        for (int i = 0; i < n ; i ++)
            cin >> v[i];

        sort(v.begin(), v.end());
        int used = 0;
        int r = 0;
        for (int i = 0; i < n; i ++) {
            if(f(v[i], 0) >= p) {
                r ++;
                //cout << v[i] << " is done without using" << endl;
            } else if(used < s && f(v[i], 1) >= p) {
                r ++;
                used ++;
                //cout << v[i] << " used" << endl;
            }
        }

        cout << "Case #" << tt << ": " << r << endl;
    }

    return 0;
}
