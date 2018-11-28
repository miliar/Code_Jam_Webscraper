#include <iostream>
#include <vector>
#include <iterator>
#include <map>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> mi;
typedef vector<char> vc;
typedef vector<vc> mc;

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        int H, W;
        cin >> H >> W;
        mi m(H, vi(W));
        for (int j=0; j<H; ++j) {
            for (int k=0; k<W; ++k)
                cin >> m[j][k];
        }

        int S = H*W;
        vi l(S);
        for (int j=0; j<S; ++j)
            l[j] = j;

        for (int j=0; j<H; ++j) {
            for (int k=0; k<W; ++k) {
                int maxdiff = 0;
                int diff;
                int ind = j*W + k;
                if (j>0 && maxdiff < (diff = m[j][k] - m[j-1][k])) {
                    maxdiff = diff;
                    l[ind] = ind-W;
                }
                if (k>0 && maxdiff < (diff = m[j][k] - m[j][k-1])) {
                    maxdiff = diff;
                    l[ind] = ind-1;
                }
                if (k<W-1 && maxdiff < (diff = m[j][k] - m[j][k+1])) {
                    maxdiff = diff;
                    l[ind] = ind+1;
                }
                if (j<H-1 && maxdiff < (diff = m[j][k] - m[j+1][k])) {
                    maxdiff = diff;
                    l[ind] = ind+W;
                }
            }
        }

        for (int j=0; j<S; ++j) {
            vi t;
            int k;
            for (k=j; k != l[k]; k = l[k])
                t.push_back(k);
            for (vi::const_iterator it=t.begin(); it!=t.end(); ++it)
                l[*it] = k;
        }

        map<int, char> mic;
        char c = 'a';
        for (int j=0; j<S; ++j)
            if (mic.find(l[j]) == mic.end())
                mic[l[j]] = c++;

        int ind = 0;
        cout << "Case #" << i+1 << ":\n";
        for (int j=0; j<H; ++j) {
            for (int k=0; k<W; ++k) {
                cout << mic[l[ind++]] << " ";
            }
            cout << "\n";
        }
    }
}
