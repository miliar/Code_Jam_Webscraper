// BEGIN CUT HERE
// headers begin
// END CUT HERE
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
// BEGIN CUT HERE
// headers end
// END CUT HERE

using namespace std;

// BEGIN CUT HERE
// helper functions begin
// END CUT HERE
// BEGIN CUT HERE
// helper functions end
template<typename T> ostream& operator<<( ostream &os, const vector<T> &v ) { os << "{"; for ( typename vector<T>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " " << *vi; } os << " }"; return os; }
template<> ostream& operator<<( ostream &os, const vector<string> &v ) { os << "{"; for ( vector<string>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " \"" << *vi << "\""; } os << " }"; return os; }
template<typename T, typename U> ostream& operator<<( ostream &os, const pair<T, U> &P ) { return os << "(" << P.first << ", " << P.second << ")"; }
template<typename T> ostream& operator<<( ostream &os, const set<T> &S ) { return os << vector<T>( S.begin(), S.end() ); }
template<typename T, typename U> ostream& operator<<( ostream &os, const map<T, U> &M ) { for ( typename map<T, U>::const_iterator mi=M.begin(); mi!=M.end(); ++mi ) { os << mi->first << " => " << mi->second << endl; } return os; }
// END CUT HERE

const int MOD = 10009;

vector<vector<int> > poly;
int word[100][26];
int cnt[26];
int sum[20];
int n;

int eval() {
    int res = 0;
    for ( int i=0; i<(int)poly.size(); ++i ) {
        int m = 1;
        for ( int j=0; j<(int)poly[i].size(); ++j ) {
            m *= cnt[poly[i][j]] % MOD;
            m %= MOD;
        }
        res += m;
        res %= MOD;
    }
    return res;
}

void parse(const string &s) {
    poly.clear();
    vector<int> limb;
    for ( int i=0; i<(int)s.size(); ++i ) {
        if ( s[i] == '+' ) {
            poly.push_back(limb);
            limb.clear();
        } else {
            limb.push_back(s[i] - 'a');
        }
    }
    poly.push_back(limb);
}

void rek(int pos, int put, int left) {
    if ( left == 0 ) return;
    if ( pos == n ) return;

    rek(pos+1, put, left);
    for ( int i=0; i<26; ++i ) cnt[i] += word[pos][i];

    ++put;
    sum[put] += eval() % MOD;
    sum[put] %= MOD;
    
    rek(0, put, left-1);
    for ( int i=0; i<26; ++i ) cnt[i] -= word[pos][i];
}

int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        memset(word, 0, sizeof word);
        memset(cnt, 0, sizeof cnt);
        memset(sum, 0, sizeof sum);

        int K;
        string poly_s; cin >> poly_s >> K;

        parse(poly_s);
        // cerr << poly << endl;

        cin >> n;
        for ( int i=0; i<n; ++i ) {
            string w; cin >> w;
            for ( int j=0; j<(int)w.size(); ++j ) ++word[i][w[j]-'a'];
        }
        
        rek(0, 0, K);
        cout << "Case #" << tt << ":";
        for ( int i=1; i<=K; ++i ) cout << ' ' << sum[i];
        cout << "\n";
    }

    return 0;
} 
