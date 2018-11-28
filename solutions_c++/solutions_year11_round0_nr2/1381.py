#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <cassert>
#include <vector>
#include <set>
#include <map>

using namespace std;

typedef map<char, set<char> > oppstr;

int betoi(char be) {
    switch (be) {
        case 'Q':
            return 0;
        case 'W':
            return 1;
        case 'E':
            return 2;
        case 'R':
            return 3;
        case 'A':
            return 4;
        case 'S':
            return 5;
        case 'D':
            return 6;
        case 'F':
            return 7;
        default:
            cout << "Got char " << be << endl;
            assert(false);
    }
}

bool isBase(char be) {
    switch (be) {
        case 'Q':
            return true;
        case 'W':
            return true;
        case 'E':
            return true;
        case 'R':
            return true;
        case 'A':
            return true;
        case 'S':
            return true;
        case 'D':
            return true;
        case 'F':
            return true;
        default:
            return false;
    }
}
void addOppsForChar(const oppstr& opps, char c, set<char>& curropps) {
    if (isBase(c)) {
        //const set<char>& nowopps = opps[c];
        oppstr::const_iterator it2 = opps.find(c);
        if (it2 != opps.end()) {
            const set<char>& nowopps = it2->second;;
            curropps.insert(nowopps.begin(), nowopps.end());
        }
    }
}

void buildOppSet(const oppstr& opps, const vector<char>& eles,
        set<char>& curropps) {
    curropps.clear();

    vector<char>::const_iterator it;
    for (it = eles.begin(); it != eles.end(); it++) {
        const char& c = *it;

        addOppsForChar(opps, c, curropps);
        /*
        if (isBase(c)) {
            //const set<char>& nowopps = opps[c];
            oppstr::const_iterator it2 = opps.find(c);
            if (it2 != opps.end()) {
                const set<char>& nowopps = it2->second;;
                curropps.insert(nowopps.begin(), nowopps.end());
            }
        }
        */
    }
}

void doCase(int caseNum) {
    char combs[8][8];
    memset(combs, 0, sizeof(combs));
    oppstr opps;
//    bool opps[8][8];
//    memset(opps, 0, sizeof(opps));

    int C;

    cin >> C;

    for (int i = 0; i < C; i++) {
        string comb;
        cin >> comb;
        char be1 = comb[0], be2 = comb[1], res = comb[2];
        int ind1 = betoi(be1), ind2 = betoi(be2);
        combs[ind1][ind2] = res;
        combs[ind2][ind1] = res;
    }

    int D;

    cin >> D;

    for (int i = 0; i < D; i++) {
        string opp;
        cin >> opp;
        char be1 = opp[0], be2 = opp[1];
        opps[be1].insert(be2);
        opps[be2].insert(be1);
    }

    int N;

    cin >> N;

    string seq;
    cin >> seq;
    vector<char> eles;
    set<char> curropps;
    for (int i = 0; i < N; i++) {
        char c = seq[i];

        char result = 0;
        if (!eles.empty()) {
            if (isBase(eles.back())) {
                int ind1 = betoi(c), ind2 = betoi(eles.back());
                result = combs[ind1][ind2];
            }
        }

        if (result != 0) {
            // A combination
            eles.pop_back();
            eles.push_back(result);
            buildOppSet(opps, eles, curropps);
        } else if (curropps.count(c) > 0) {
            // An opposition
            eles.clear();
            curropps.clear();
        } else {
            // Just add
            eles.push_back(c);
            addOppsForChar(opps, c, curropps);
        }
    }

    cout << "Case #" << caseNum << ": [";

    vector<char>::const_iterator it;
    bool first = true;
    for (it = eles.begin(); it != eles.end(); it++) {
        if (!first) {
            cout << ", ";
        }
        first = false;
        cout << *it;
    }

    cout << "]" << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
