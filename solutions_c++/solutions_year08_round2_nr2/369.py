#include <iostream>
#include <math.h>
#include <vector>
#include <set>

using namespace std;

typedef long long int LLI;

bool isprime(LLI n) {
    if (n==2) return true;
    LLI s = (LLI)sqrt(n);
    for (int i=2; i<=s; i++) {
        if( n%i == 0 ) return false;
    }
    return true;
}

bool passes(LLI a, LLI b, LLI p) {
    for (int i=p; i<= b; i++) {
        if (!isprime(i)) continue;
        if (a%i == 0 && b%i == 0) return true;
    }
    return false;
}

main() {
    LLI nc;
    cin >> nc;
    for (LLI ic=1; ic<=nc; ic++) {
        LLI a, b, p;
        cin >> a >> b >> p;

        vector< set<LLI> > vs;
        vector<LLI> bl;
        for (LLI j=a; j<=b; j++) {
            set<LLI> s;
            s.insert(j);
            vs.push_back(s);
            bl.push_back(j);
        }
        for (LLI i=p; i<=b; i++) {
            if (!isprime(i)) continue;
            // cout << "p " << i << endl;
            for (LLI j=a; j<=b; j++) {
                if (j%i != 0) continue;
                LLI bj = bl[j-a];
                set<LLI> &s = vs[bj-a];
                for (LLI k=j+1; k<=b; k++) {
                    if (k%i != 0) continue;
                    LLI bk = bl[k-a];
                    if (bk == bj) continue;
                    // cout << " " << j << " " << k << endl;
                    set<LLI> &t = vs[bk-a];
                    for (set<LLI>::iterator it=t.begin(); it!=t.end(); it++) {
                        LLI tv = *it;
                        bl[tv-a] = bj;
                    }
                    s.insert(t.begin(), t.end());
                    t.clear();
                }
            }
        }
        LLI cnt=0;
        for( LLI i=0; i<vs.size(); i++ ) {
            set<LLI> &s = vs[i];
            if (s.size() > 0) cnt++;
        }
        cout << "Case #" << ic << ": " << cnt << endl;
    }
}
