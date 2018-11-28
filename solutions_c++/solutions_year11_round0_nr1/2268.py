#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        unsigned N;
        cin >> N;

        list<unsigned> o, b;
        vector<char> c;
        for (unsigned i = 0; i < N; ++i) {
            string s;
            unsigned p;
            cin >> s >> p;
            c.push_back(s[0]);
            switch (s[0]) {
            case 'O':
                o.push_back(p);
                break;
            case 'B':
                b.push_back(p);
                break;
            default:
                assert(false);
            }
        }

        unsigned ci = 0;
        unsigned po = 1, pb = 1;
        unsigned t = 0;
        while (!o.empty() || !b.empty())
        {
            ++t;

            bool pushed = false;
            
            // O
            if (!o.empty()) {
                if (po != o.front()) {
                    po += po < o.front() ? 1 : -1;
                } else {
                    if (c[ci] == 'O') {
                        ++ci;
                        o.pop_front();
                        pushed = true;
                    }
                }
            }

            // B 
            if (!b.empty()) {
                if (pb != b.front()) {
                    pb += pb < b.front() ? 1 : -1;
                } else {
                    if (!pushed && c[ci] == 'B') {
                        ++ci;
                        b.pop_front();
                    }
                }
            }
        }

        cout << "Case #" << iCase << ": " << t << endl;
    }
}

