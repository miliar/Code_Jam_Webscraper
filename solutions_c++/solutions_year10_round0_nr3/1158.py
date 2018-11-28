#include <iostream>
#include <vector>
#include <boost/foreach.hpp>
#include <boost/assert.hpp>

using namespace std;
using namespace boost;

struct State {
    unsigned long long euro;
    int long long step;
    State () : euro(0), step(-1) {
    }
};

struct Next {
    unsigned long long euro;
    unsigned pos;
};

int main (int argc, char *argv[]) {
    unsigned T;
    
    cin >> T;

    for (unsigned t = 1; t <= T; ++t) {

        unsigned long long R, k;
        unsigned N;

        cin >> R >> k >> N;

        vector<unsigned long long> g(N);
        unsigned long long total = 0;

        BOOST_FOREACH(unsigned long long &v, g) {
            cin >> v;
            total += v;
        }


        if (k > total)  k = total;

        vector<Next> next(N);

        cerr << "Next: " << endl;
        {
            unsigned nn = 0;
            unsigned long long ee = 0;

            for (unsigned i = 0; i < N; ++i) {
                while (g[nn] + ee <= k) {
                    ee += g[nn];
                    nn = (nn + 1) % N;
                }
                next[i].pos = nn;
                next[i].euro = ee;
                cerr << next[i].pos << " " << next[i].euro << endl;
                ee -= g[i];
            }
        }

        vector<State> state(N);

        unsigned long long euro = 0;
        unsigned cur = 0;
        unsigned long long step = 0;

        cerr << "State: " << endl;
        // initial
        {
            while ((state[cur].step < 0) && (step < R)) {
                state[cur].step = step;
                state[cur].euro = euro;
                cerr << step << " @" << cur << " $" << euro << endl;

                euro += next[cur].euro;
                cur = next[cur].pos;
                ++step;
            }
        }

        if (step < R) {
            unsigned long long period = step - state[cur].step;
            unsigned long long euro_p = euro - state[cur].euro;
            unsigned long long left = R - step;
            unsigned long long cycle = left / period;

            euro += cycle * euro_p;
            step += cycle * period;

            cerr << "LEFT " << left << endl;;
            cerr << "cycle C= " << cycle << " L=" << period << " E=" << euro_p << endl;
        
            for (; step < R; ++step) {
                cerr << step << " @" << cur << " $" << euro << endl;
                euro += next[cur].euro;
                cur = next[cur].pos;
            }
        }

        cout << "Case #" << t << ": " << euro << endl;
    }

    return 0;
}
