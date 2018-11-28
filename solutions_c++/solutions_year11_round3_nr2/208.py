#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <algorithm>

using namespace std;

unsigned a[1200000];

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        unsigned long long L, t;
        unsigned N, C;
        cin >> L >> t >> N >> C;
        for (size_t i = 0; i < C; ++i) {
            cin >> a[i];
        }
        
        unsigned long long s = 0;
        unsigned r;
        //vector<unsigned long long> l;
        map<unsigned long long, unsigned long long> m;
        for (size_t i = 0; i < N; s+=r, ++i) {
            r = a[i%C];

            if (t >= 2*(s+r))
                continue;

            if (t <= 2*s) {
                //l.push_back(2*r);
                m[2*r]++;
            }
            else {
                //l.push_back(2*(s+r) - t);
                m[2*(s+r)-t]++;
            }
        }

        unsigned long long save = 0;
        unsigned long long cnt = L;
        //sort(l.begin(), l.end());
        // for (size_t i = l.size() - 1; i >= 0; --i) {
        //     if (++cnt > L)
        //         break;
        //     save += l[i];
        // }
        map<unsigned long long, unsigned long long>::reverse_iterator it;
        for (it = m.rbegin(); it != m.rend(); ++it) {
            unsigned long long num = min(it->second, cnt);
            save += it->first * num;
            
            cnt -= num;
            if (cnt == 0)
                break;
        }

        cout << "Case #" << iCase << ": " << (2*s - (save>>1)) << endl;
    }

    // map<unsigned,unsigned> v;
    // for (size_t i = 0; i < 1000000; ++i)
    //     v[i]++;
}

