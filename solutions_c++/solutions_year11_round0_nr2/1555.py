#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <cstring>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

map<string, char> conv;
set<string> er;

void outdata() {
}

void solve() {
    string s, res;
	int n;
	cin >> n;
	cin >> s;
	assert(n == s.length());
    fors(q, s) {
        res += s[q];
        if (res.size() > 1 && conv.count(res.substr(res.size() - 2))) {
            string x = res.substr(res.size() - 2);
            res.erase(res.size() - 2);
            res += conv[x];
        }
        fors(i, res) fors(j, res) if (i != j && er.count(string(1, res[i]) + res[j])) {
            res.clear();
            //cerr << "!!" << endl;
            break;
        }
    }
    cout << "[";
    fors(i, res) {
        if (i > 0) cout << ", ";
        cout << res[i];
    }
    cout << "]" << endl;
}

void readdata() {
    int c;
    cin >> c;
    conv.clear();
    forn(i, c) {
        string s;
        cin >> s;
        conv[string(1, s[0]) + s[1]] = s[2];
        conv[string(1, s[1]) + s[0]] = s[2];
    }
    cin >> c;
    er.clear();
    forn(i, c) {
        string s;
        cin >> s;
        er.insert(string(1, s[0]) + s[1]);
        er.insert(string(1, s[1]) + s[0]);
    }
}

int main() {
    int t;          
    cin >> t;
    forn(i, t) {
        cout << "Case #" << i + 1 << ": ";
    	readdata();
	    solve();
    	outdata();
    }
	return 0;
}
