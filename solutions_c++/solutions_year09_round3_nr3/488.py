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

#define FILENAME "C-small-attempt0"
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
    typename vector<T>::const_iterator it;
    for(it = v.begin(); it != v.end(); ++it)
        os << (*it) << " ";
    return os;
}

long long bribe(size_t i, vector<bool>& vp) {
    // cout << "bribe(" << i << ", " << vp << ")" << endl;
    long long C = 0;
    vp[i] = false;
    // cout << "vp[" << i << "] set" << endl; cout.flush();
    for(size_t j = i + 1; j < vp.size() && vp[j]; ++C, ++j);
    // cout << "first for" << endl; cout.flush();
    for(int j = i - 1; j >= 0 && vp[j]; ++C, --j);
    // cout << "2nd for" << endl; cout.flush();
    return C;
}

int main() {
    ifstream ifs(c_pszInFileName);
    ofstream ofs(c_pszOutFileName);
    FILE* pFile = fopen(c_pszOutFileName, "w");

    int T;
    GetLine(ifs, T);

    FR(t, T) {
        cout << "test: " << t << endl; cout.flush();
        int P, Q;
        ifs >> P >> Q;

        cout << "P: " << P << " Q: " << Q << endl; cout.flush();

        Vi vQ(Q);
        FR(i, Q)
            ifs >> vQ[i];
        cout << "vQ: " << vQ << endl; cout.flush();

        long long minC = 0x7FFFF;
        do {
            vector<bool> vP(P, true);
            long long C = 0;
            FR(i, Q) C += bribe(vQ[i] - 1, vP);
            minC = min(C, minC);
        } while(next_permutation(vQ.begin(), vQ.end()));
        
        ofs << "Case #" << (t+1) << ": " << minC << endl;
    }

    cout.flush();
    fclose(pFile);
    return 0;
}
