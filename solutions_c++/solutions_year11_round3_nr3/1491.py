#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>
#include <stdint.h>

using namespace std;

struct Instance {
    uint64_t low, high;
    vector<uint64_t> notes;

    Instance(uint64_t num, uint64_t _low, uint64_t _high)
        : low(_low), high(_high), notes(num, 0)
    {}

    int64_t solve();
};


void readInput(vector<Instance>* instances) {
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i) {
        uint64_t n, l, h;
        cin >> n >> l >> h;
        Instance cur(n, l, h);
        for(int note = 0; note < n; ++note) {
            cin >> cur.notes[note];
            cerr << " Instance " << i << " note " << note << " " << cur.notes[note] << endl;
        }
        cerr << "Read instance " << i << " with " << n << " notes" << endl;
        instances->push_back(cur);
    }
}

int64_t Instance::solve() {
    cerr << "SOLVE" << endl;
    for(uint64_t i = low; i <= high; ++i) {
        bool good = true;
        for(uint64_t nn = 0; nn < notes.size(); ++nn) {
            cerr << " Note " << nn << " " << notes[nn] << endl;
            const uint64_t note = notes[nn];
            if((note % i != 0) && (i % note != 0)) {
                cerr << "bad " << i << " " << note << endl;
                good = false;
                break;
            }
        }
        if(good) return i;
    }
    return -1;
}

void output(int n, int64_t s) {
    cout << "Case #" << n + 1 << ": ";
    if(s == -1) {
        cout << "NO" << endl;
    } else {
        cout << s << endl;
    }
}

int main() {
    vector<Instance> instances;
    readInput(&instances);
    for(int i = 0; i < instances.size(); ++i) {
        output(i, instances[i].solve());
    }
}


