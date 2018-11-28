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

int combi[26][26];
bool opposed[26][26];

void setNull() {
    FOR(i,0,26) {
        FOR(j,0,26) {
                combi[i][j] = -1;
                opposed[i][j] = false;
        }
    }
}
char getCombi(string str) {
    int val = combi[str[0]-'A'][str[1]-'A'];
    if (val == -1) return '0';
    return (char)(val + 'A');
}
bool getOpposed(string str) {
    return opposed[str[0] - 'A'][str[1] - 'A'];
}
void setCombi(string str) {
        combi[str[0] - 'A'][str[1] - 'A'] = str[2] - 'A';
        combi[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
}
void setOpposed(string str) {
        opposed[str[0] - 'A'][str[1] - 'A'] = true;
        opposed[str[1] - 'A'][str[0] - 'A'] = true;
}

void checkList(string& str) {
    if (str.length() > 1) { // Check for Combinations
        string end = str.substr(str.length()-2,2);
        char ch = getCombi(end);
        if (ch != '0') {
            str = str.substr(0,str.length()-2) + ch;
            checkList(str);
            return;
        }
        // No Combinations found
        ch = str[str.length()-1];
        FOR(i,0,str.length()-1) {
            if (getOpposed( str.substr(i,1) + ch)) {
                    str.clear();
                    return;
            }
        }
    }

}
int main() {
    int T;
    cin >> T;
    FOR(i,1,T+1) {
            setNull();
            int C;
            cin >> C;

            FOR(j,0,C) {
                string str;
                cin >> str;
                setCombi(str);
            }

            int D;
            cin >> D;

            FOR(j,0,D) {
                string str;
                cin >> str;
                setOpposed(str);
            }

            int N;
            cin >> N;
            string input;
            cin >> input;

            string list;
            FOR (j,0,N){
                list += input[j];
                checkList(list);
            }


            cout << "Case #" << i << ": [";
            // this can be done far more elegant with methods of the STL, forgot how to do it though
            FOR (j,0,list.length()) {
                cout << list[j];
                if (j < list.length()-1) cout << ", ";

            }
            cout << "]" << endl;

    }
}


