#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <vector>

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define FR(i,a) for(int i = 0; i < (a); ++i)

#define FILENAME "A-large"
static const char* c_pszInFileName = FILENAME ".in";
static const char* c_pszOutFileName = FILENAME ".out";

using namespace std;

typedef vector<int> Vi;
typedef vector<string> Vs;

template<class T>
void GetLine(ifstream& ifs, T& t) {
    string line;
    getline(ifs, line);
    stringstream(line) >> t;
}

template<class T>
ostream& operator<< (ostream& os, vector<T> const& v) {
    for(Vi::iterator it = v.begin(); it != v.end(); ++it)
        os << (*it);
    return os;
}

int main() {
    ifstream ifs(c_pszInFileName);
    ofstream ofs(c_pszOutFileName);
    FILE* pFile = fopen(c_pszOutFileName, "w");

    int T;
    GetLine(ifs, T);
    long long test = 1000000000000000000;
    cout << "test: " << test << endl;

    FR(t, T) {
        string line;
        getline(ifs, line);
        set<char> sc;
        FR(i, line.length())
            sc.insert(line[i]);
        int nMinBase = max(2, int(sc.size()));
        cout << (t + 1) << ": min base: " << nMinBase << endl;
        
        
        map<char, int> used;
        used.insert(make_pair(line[0], 1));
        int i;
        for(i = 1; i < line.length() && line[i] == line[0]; ++i);
        if (i < line.length())
            used.insert(make_pair(line[i], 0));

        int curNum = 2;
        for(; i < line.length(); ++i) {
            if (used.find(line[i]) == used.end()) {
                used.insert(make_pair(line[i], curNum++));
            }
        }
        if (curNum > (nMinBase + 1))
            cout << "!!!!!!!!!" << endl;

        long long ans = 0;        
        for(int j = 0; j < line.length(); ++j) {
            ans *= nMinBase;
            ans += used[line[j]];
        }
    
        
        ofs << "Case #" << (t+1) << ": ";

        ofs << ans << endl;
    }

    cout.flush();
    fclose(pFile);
    return 0;
}
