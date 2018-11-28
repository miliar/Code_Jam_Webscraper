#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <vector>

#define FR(i,a) for(int i = 0; i < (a); ++i)

#define FILENAME "A-large"
// #define FILENAME "A-small-attempt1"
// #define FILENAME "test"
static const char* c_pszInFileName = FILENAME ".in";
static const char* c_pszOutFileName = FILENAME ".out";

using namespace std;

template<class T>
void GetLine(ifstream& ifs, T& t) {
    string line;
    getline(ifs, line);
    stringstream(line) >> t;
}

/*int DFS(set<string> const& dict, vector<vector<char> > const& test, int row, int col, string str) {
    // cout << "DFS(" << row << ", " << col << ", " << str << ", " << ")" << endl;
    if (row >= (test.size() - 1)) {
        if (dict.find(str) == dict.end()){
            // cout << "dict.find(" << str << ") == dict.end() " << endl;
            return 0;
        } else {
            // cout << "found!" << endl;
            return 1;
        }            
    } 

    int acc = 0;
    FR(c, test[row].size()) {
        string t = str;
        t += test[row][c];
        // cout << "t: "<< t << endl;
        acc += DFS(dict, test, row + 1, 0, t);
    }
    return acc;
}
*/

int main() {
    ifstream ifs(c_pszInFileName);
    ofstream ofs(c_pszOutFileName);
    int L, D, N;
    string endline;

    ifs >> L >> D >> N;
    cout << "L: "<< L << " D: " << D << " N: " << N << endl;

    vector<string> dict(D);
    FR(i,D) ifs >> dict[i];
    cout << "created dict " << endl;
    getline(ifs, endline);

    FR(t, N) {
        vector<vector<bool> > test(L + 1, vector<bool>(26, false));
        string line;
        getline(ifs, line);
        stringstream ss(line);
        
        cout << "line: " << line << endl;

        char c;
        int i = 0;
        bool fInParen = false;

        while (ss.good()) {
            ss >> c;
            // cout << "read: " << c << " i: "<< i << endl;
            switch(c) {
            case '(':
                fInParen = true;
                break;
            case ')':
                fInParen = false;
                break;
            default:
                test[i][c - 'a'] = true;
            }
            if (!fInParen) ++i;
        }

        int ans = 0;
        FR(d, D) {
            FR(c, dict[d].length()) {
                if(!test[c][dict[d][c] - 'a']) {
                    // cout << "char: " << c << ": " << "of:  " << dict[d] << " = " <<  dict[d][c] << " missing in: " << line << endl;
                    goto Skip;
                }
            }
            ++ans;
        Skip: ;
        }
        string str;


        // FR (j, test[0].size()) {
        //     FR (k, test[1].size()) {
        //         FR (l, test[2].size()) {                    
        //             str = test[0][j];
        //             str += (test[1][k]);
        //             str += (test[2][l]);
        //             cout << "testing: " << str << endl; //test[0][j] << test[1][k] << test[2][l] << endl;
        //             if (dict.find(str) != dict.end()) ++ans;
        //         }
        //     }
        // }

        // int ans = DFS(dict, test, 0, 0, "");
        ofs << "Case #" << (t + 1) << ": " << ans << endl;
    }
}
