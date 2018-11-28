// eddie s.j. du
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <list>
#include <sstream>
#include <map>
#include <queue>

#define ui unsigned int
#define ll long long
#define ul unsigned long
#define ull unsigned long long
#define fore(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define rep(i,a) fore(i,0,a)
#define pb push_back
#define MP make_pair

using namespace std;

//c style
//FILE *fin = fopen("cowxor.in", "r");

//c++ style

    //ofstream fout ("gift1.out");
    ifstream fin ("A-large.in");


int main () {
    // c style
    freopen ("A-large.out","w",stdout);
    // ie int n; fscanf (fin,"%d",&n);
    int L, D, N;
    fin >> L >> D >> N;
    vector<string> words;
    string s;
    rep (i,D) {
        fin >> s;
        words.pb (s);
    }
    rep (asdfds,N) {
        fin >> s;
        bool t [L][30];
        rep (i,L) rep (j,30) t [i][j] = false;
        int c = 0;
        rep (i,L) {
            if (s[c] == '(') {
                c++;
                while (s[c]!=')'){
                    t[i][s[c]-'a'] = true;
                    c++;
                }
                c++;
            } else {
                t[i][s[c]-'a'] = true;
                c++;
            }
        }
        int cnt = 0;
        rep (i,D) rep (k,L) {
            if (!t[k][words[i][k]-'a']) {
                break;
            } else if (k == L-1) {
                cnt++;
            }
        }
        cout << "Case #" << asdfds+1 << ": " << cnt << endl;
    }

    return 0;
}
