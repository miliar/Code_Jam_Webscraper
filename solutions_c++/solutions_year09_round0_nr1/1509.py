#include<algorithm>
#include<cmath>
#include<iostream>
#include<list>
#include<cstring>
#include<climits>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<vector>
using namespace std;

template<class A, class B> void conv_(A& x, B& y) { stringstream s; s << x; s >> y; }

typedef unsigned int uint;
typedef unsigned long long int ullong;
#define for_(i, a, b) for(int i=(a);i<(b);++i)
#define set_(a, n) memset(a, n, sizeof a)

int main(void) {
    int l, d, n;
    cin >> l >> d >> n;

    string dic[d];

    for_(i, 0, d)
        cin >> dic[i];

    for_(t, 1, n+1) {
        string pat;
        cin >> pat;

        int res = 0, p = 0;

        for_(di, 0, d) {
            string& dw = dic[di];
            bool match = true;

            for (int i = 0, dwi = 0; i < pat.length() && match; ++i, ++dwi) {
                if (pat[i] != '(') {
                    if (pat[i] != dw[dwi]) match = false;
                }
                else {
                    bool found = false; int j;
                    for (j = i+1; pat[j] != ')'; ++j) {
                        if (pat[j] == dw[dwi])
                            found = true;
                    }
                    i = j;
                    if (!found) match = false;
                }
            }

            if (match) ++res;
        }

        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
