#include <iostream>
#include <string>
#include <list>
#include <map>


using namespace std;

const char base[] = "QWERASDF";

char c[512][512];
bool d[512][512];

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {
        memset(c, ' ', sizeof(c));
        memset(d, false, sizeof(d));

        unsigned C, D, N;

        cin >> C;
        for (unsigned i = 0; i < C; ++i) {
            string s;
            cin >> s;
            c[static_cast<int>(s[0])][static_cast<int>(s[1])] = s[2];
            c[static_cast<int>(s[1])][static_cast<int>(s[0])] = s[2];
        }

        cin >> D;
        for (unsigned i = 0; i < D; ++i) {
            string s;
            cin >> s;
            d[static_cast<int>(s[0])][static_cast<int>(s[1])] = true;
            d[static_cast<int>(s[1])][static_cast<int>(s[0])] = true;
        }

        cin >> N;
        string s;
        cin >> s;
        assert(N == s.size());

        list<char> l;
        map<char, unsigned> m;
        for (unsigned i = 0; i < N; ++i) {

            if (!l.size()) {
                m[s[i]]++;
                l.push_back(s[i]);
                continue;
            }

            char lc = l.back();

            if (l.size() && c[static_cast<int>(lc)][static_cast<int>(s[i])] != ' ') {
                char nc = c[static_cast<int>(lc)][static_cast<int>(s[i])];
                m[lc]--;
                m[nc]++;
                l.back() = nc;
            } else {
                bool clear = false;
                for (unsigned j = 0; j < 8; ++j) {
                    char b = base[j];
                    if (d[static_cast<int>(b)][static_cast<int>(s[i])] && m[b] > 0) {
                        clear = true;
                        break;
                    }
                }
                if (clear) {
                    l.clear();
                    m.clear();
                } else {
                    m[s[i]]++;
                    l.push_back(s[i]);
                }
            }
        }

        cout << "Case #" << iCase;
        cout << ": [";
        list<char>::iterator it = l.begin(), eit = l.end();
        bool first = true;
        for (; it != eit; ++it) {
            if (first) {
                first = false;
                cout << *it;
            } else {
                cout << ", " << *it;
            }
        }
        cout << "]" << endl;
    }
}

