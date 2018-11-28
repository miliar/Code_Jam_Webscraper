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

void outdata() {
}

void solve() {
}

int move(int a, int b, int w) {
    int res = abs(a - b) - w;
    return max(res, 0) + 1;
}

vector<double> wpCount(const vector<vector<int> >& a, int exl)
{
	int n = a.size();
    vector<int> g(n, 0), w(n, 0);
    vector<double> wp(n, 0);
    forn(i, n) if (i != exl) {
        forn(j, n) if (a[i][j] != -1 && j != exl) {
            g[i]++;
            if (a[i][j] == 1) w[i]++;
        }
        wp[i] = 1.0 * w[i] / g[i];
    }
    return wp;
}

void readdata() {
    int n;
    cin >> n;
    vector<vector<int> > a(n);
    forn(i, n) {
        string s;
        cin >> s;
        a[i].resize(n);
        forn(j, n) {
            char c = s[j];
            if (c == '.')
                a[i][j] = -1; 
            else if (c == '1')
                a[i][j] = 1;
            else a[i][j] = 0;
        }
    }
    vector<double> wp = wpCount(a, -1), owp(n, 0), oowp(n, 0);
    forn(i, n) {
        vector<double> wpCur = wpCount(a, i);
		int g = 0;
        forn(j, n) if (a[i][j] != -1) {
            owp[i] += wpCur[j];
			++g;
        }
        owp[i] /= g;
    }
    
    forn(i, n) {
		int g = 0;
        forn(j, n) if (a[i][j] != -1) {
            oowp[i] += owp[j];
			++g;
		}
        oowp[i] /= g;
    }
    forn(i, n) printf("%0.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
    
}

int main() {
    int t;          
    cin >> t;
    forn(i, t) {
        cout << "Case #" << i + 1 << ":\n";
    	readdata();
	    solve();
    	outdata();
    }
	return 0;
}


