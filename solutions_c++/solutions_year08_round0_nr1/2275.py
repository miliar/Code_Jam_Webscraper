#include <iostream>
#include <sstream>
#include <fstream>

#include <string>
#include <vector>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;

#define TESTING

int getNum() {
    string s;
    getline(cin, s);

    int result;
    stringstream ss(s);
    ss >> result;

    return result;
}

vector<vi> calcPos(const vs& names, const vs& queries) {
    vector<vi> result(names.size());
    for (int i=0; i<names.size(); ++i) {
        for (int j=0; j<queries.size(); ++j) {
            if (names[i] == queries[j]) {
                result[i].push_back(j);
            }
        }

        result[i].push_back(1000000);
    }

    return result;
}

int solve(const vs& names, const vs& queries) {
    int result = 0;

    vector<vi> pos = calcPos(names, queries);

    vi lastPos(names.size(), 0);
    int curPos = 0;
    int lastM = -1;
    while (curPos != 1000000) {
        int maxPos = -1;
        int maxM = -1;
        for (int i=0; i<lastPos.size(); ++i) {
            if (i != lastM && pos[i][lastPos[i]] > maxPos) {
                maxPos = pos[i][lastPos[i]];
                maxM = i;
            }
        }

        curPos = maxPos;
        lastM = maxM;
        ++result;

        for (int i=0; i<lastPos.size(); ++i) {
            while (lastPos[i] < pos[i].size() && pos[i][lastPos[i]] <= curPos) {
                ++lastPos[i];
            }
        }
    }

    return result - 1;
}

int main(int argc, char* argv[]) {
    int testsNum = getNum();
    for (int test = 0; test < testsNum; ++test) {

#ifdef TESTING
        stringstream ss;
        ss << "test" << test;
        ofstream fout(ss.str().c_str());
        fout << 1 << endl;
#endif

        int namesNum = getNum();
        vs names(namesNum);

#ifdef TESTING
        fout << namesNum << endl;
#endif
        
        for (int i = 0; i < namesNum; ++i) {
            getline(cin, names[i]);

#ifdef TESTING
            fout << names[i] << endl;
#endif
        }

        int queriesNum = getNum();
        vs queries(queriesNum);

#ifdef TESTING
        fout << queriesNum << endl;
#endif

        for (int i = 0; i < queriesNum; ++i) {
            getline(cin, queries[i]);

#ifdef TESTING
            fout << queries[i] << endl;
#endif
        }

        cout << "Case #" << test + 1 << ": " << solve(names, queries) << endl;

#ifdef TESTING
        fout.close();
#endif
    }

    return 0;
}

