#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <vector>
#define fl(var, start, limit) for(var = (start); var < (limit); ++var)
#define fd(var, start, limit) for(unsigned int var = (start); var < (limit); ++var)
#define flz(var, limit) for(var = 0; var < (limit); ++var)
#define fdz(var, limit) for(unsigned int var = 0; var < (limit); ++var)
#define rl(limitVar) unsigned int limitVar; cin >> limitVar;
#define frl(var, limitVar) rl(limitVar); fdz(var, limitVar)
#define sp << " " <<
using namespace std;
typedef vector<unsigned int> vui;
typedef vector<int> vi;
typedef vector<char> vc;
#define next a; cin >> a; return a;
unsigned int nui() { unsigned int next; }
int ni() { int next; }
float nf() { float next; }
double nd() { double next; }

void initTestcase() {
}

void cleanTestcase() {
}

class IsGreater {
    public:
        bool operator()(const int &l, const int &r) {
            return l > r;
        }
};

void doTestcase() {
    rl(C);
    rl(D);

    priority_queue<int, vi, IsGreater> vendors;

    fdz(i, C) {
        int p = ni();
        unsigned int v = nui();
        fdz(j, v) {
            vendors.push(p);
        }
    }

    float time = 0;
    float bonus = 0;
    while (!vendors.empty()) {
        float pos = vendors.top() - bonus;
        bonus = 0;
        vendors.pop();
        if (vendors.empty()) {
            break;
        }

        float npos = vendors.top();
        //if (pos - prevPos > D) {
            //float a = prevPos + D;
            //float b = pos - time;
            //pos = (a > b) ? a : b;
        //}

        if (npos - pos <= D) {
            time += (D - (npos - pos)) / 2.0;
        } else {
            bonus = 2 * time;
            float a = npos - bonus;
            if (a < pos + D) {
                bonus = npos - pos - D;
            }
        }
    }

    cout << time;
}

int main(int argc, char *argv[]) {
    frl(t, tt) {
        cout << "Case #" << t + 1 << ": ";
        initTestcase();
        doTestcase();
        cleanTestcase();
        cout << endl;
    }
    return EXIT_SUCCESS;
}

