#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

int main()
{
    int Nc; cin >> Nc;
    for (int k = 0; k < Nc; k++) {
        int N, times, maxi;
        cin >> times >> maxi >> N;

        list<int> l;
        vector<int> v;
        map<list<int>, int> m;

        for (int i = 0; i < N; i++) {
            int a; cin >> a;
            l.push_back(a);
        }

        int total = 0;

        bool bEnding = true; //false;
        int cnt = 0;

        while (times != 0) {
            map<list<int>, int>::iterator it = m.find(l);
            if (false && it != m.end() && bEnding == true) {
                bEnding = true;
                int cycle = cnt - it->second;
                int acum = 0;
                for (int i = it->second; i < int(v.size()); i++) {
                    acum += v[i];
                }
                total += (times / cycle) * acum;
                times = times % cycle;
            }
            else {
                list<int> out;
                list<int> lin = l;
                int in = 0;
                while (! l.empty()) {
                    if (l.front() + in > maxi) {
                        break;
                    }
                    else {
                        out.push_back(l.front());
                        in += l.front();
                        l.pop_front();
                    }
                }
                l.insert(l.end(), out.begin(), out.end());
                if (bEnding == false) {
                    m.insert(make_pair(lin, cnt));
                    v.push_back(in);
                }
                times--;
                cnt++;
                total += in;
            }
        }
        cout << "Case #" << k+1 << ": " << total << endl;
    }
    return 0;
}
