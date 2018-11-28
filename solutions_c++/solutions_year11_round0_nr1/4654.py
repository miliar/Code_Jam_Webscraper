#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <cstdlib>
#include <cmath>

#define FOR0(i, up) for(decltype(up) i=0; i<up; ++i)
#define FOR1(i, up) for(decltype(up) i=1; i<up; ++i)
#define FORALL(it, container) \
    for(auto it = container.cbegin(); it != container.cend(); ++it)

using namespace std;

typedef vector<int> ivec;
typedef vector<double> dvec;
typedef vector<float> fvec;
typedef vector<string> svec;

struct Action {
    unsigned ID;
    unsigned req;
    unsigned button;

    Action(unsigned id, unsigned r, unsigned b): ID(id), req(r), button(b) {}
};

typedef vector<Action> ActionQueue;

unsigned solve(ActionQueue &blue, ActionQueue &orange)
{
    unsigned time = 0;
    unsigned last = 0, nextlast;
    unsigned op = 1, bp = 1;
    while (!blue.empty() || !orange.empty()) {
        nextlast = last;
        if (!blue.empty()) {
            auto ba = blue.front();
            if (ba.req <= last && bp == ba.button) { // push
                nextlast = ba.ID;
                blue.erase(blue.begin());
            } else if (bp != ba.button) { // move
                bp = bp < ba.button ? bp+1 : bp-1;
            }
        }

        if (!orange.empty()) {
            auto oa = orange.front();
            if (oa.req <= last && op == oa.button) { // push
                nextlast = oa.ID;
                orange.erase(orange.begin());
            } else if (op != oa.button) { // move
                op = op < oa.button ? op+1 : op-1;
            }
        }

        last = nextlast;
        ++time;
    }
    return time;
}

int main(int argc, char** argv)
{
    unsigned T;
    cin >> T;
    FOR0(i, T) {
        unsigned N, Pi;
        unsigned lo = 0, lb = 0;
        char Ri;
        ActionQueue orange, blue;
        cin >> N;
        FOR1(j, N+1) {
            cin >> Ri >> Pi;
            if (Ri == 'O') {
                orange.push_back(Action(j, lb, Pi));
                lo = j;
            } else {
                blue.push_back(Action(j, lo, Pi));
                lb = j;
            }
        }
        unsigned result = solve(blue, orange);
        cout << "Case #" << i+1 << ": " << result << endl;
    }
}
