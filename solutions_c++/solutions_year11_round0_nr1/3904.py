#include <boost/config.hpp>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <gmp.h>
#include <gmpxx.h>
#include <boost/utility.hpp>

using namespace std;
using namespace boost;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define PI(a,b) make_pair(a,b);



int main() {
    int T;
    cin >> T;
    FOR(i,1,T+1) {
            int N;
            cin >> N; // Number of Orders
            int pos[2] = {1,1};
            int steps = 0;
            int sum = 0;
            char lastbot = 'O'; // steps are 0 anyway

            FOR(j,0,N) {
                    char ch;
                    cin >> ch;
                    int m;
                    cin >> m;
                    int reqsteps = 1; // one step to push the button
                    if (ch == 'O') {
                        reqsteps += abs(pos[0]-m); // Move distance
                        pos[0] = m;
                    }
                    if (ch == 'B') {
                        reqsteps += abs(pos[1]-m);
                        pos[1] = m;
                    }
                    if (lastbot != ch) { // a new bot
                        if (reqsteps  == 1) steps = 1;
                        else steps = max(1,reqsteps-steps);
                        lastbot = ch;
                        sum += steps;
                    } else {
                        sum += reqsteps;
                        steps += reqsteps;
                    }
            }

            cout << "Case #" << i << ": " << sum << endl;

    }
}


