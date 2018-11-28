#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define x first
#define y second


#define debug(x) cout << '>' << #x << ':' << x << endl;



typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;



const int nx = 30;

int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);


    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int c;
        cin >> c;
        vector < vector < int > > f(nx, vector < int > (nx, -1));
        for (int i = 0; i < c; ++i) {
            string s;
            cin >> s;
            int a = s[0] - 'A';
            int b = s[1] - 'A';
            int c = s[2] - 'A';
            f[a][b] = c;
            f[b][a] = c;
        }
        vector < vector < bool > > p(nx, vector < bool> (nx, false));
        int d;
        cin >> d;
        for (int i = 0; i < d; ++i) {
            string s;
            cin >> s;
            int a = s[0] - 'A';
            int b = s[1] - 'A';
            p[a][b] = true;
            p[b][a] = true;
        }
        int k;
        cin >> k;

        string s;
        cin >> s;
        
        vector < int > l;
        for (int i = 0; i < sz(s); ++i) {
            int c = s[i] - 'A';
            l.pb(c);
            while (true) {
                int num = sz(l);
                if (num <= 1) break;
                int a = l[num - 1];
                int b = l[num - 2];
                int cc = f[a][b];
                if (cc > 0) {
                    l.pop_back();
                    l.pop_back();
                    l.push_back(cc);
                } else {
                    break;
                }
            }
            for (int j = 0; j < sz(l) - 1; ++j) {
                int c = l[sz(l) - 1];
                if (p[l[j]][c] == true) {
                    l.clear();
                }
            }
        }

        cout << "Case #" << t + 1 << ": ";
        cout << "[";
        for (int i = 0; i < sz(l); ++i) {
            if (i > 0) {
                cout << ", ";
            }
            printf("%c", l[i] + 'A');
            
        }
        cout << "]" << endl;
    }


    return 0;
}

