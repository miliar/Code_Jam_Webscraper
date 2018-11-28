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


using namespace std;


#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define debug(x) cout << '>' << #x << ':' << x << endl;

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)


typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;






int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ":" << endl;
        int n;
        cin >> n;
        vector < string > s(n);
        for (int i = 0; i < n; ++i) {
            cin >> s[i];
        }
    
        vector < double > wp(n);
        vector < double > owp(n);
        vector < double > oowp(n);
        for (int i = 0; i < n; ++i) {
            int nw = 0;
            int ng = 0;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                nw += (s[i][j] == '1');
                ng += (s[i][j] != '.');
            }  
            wp[i] = (double) nw / (ng);

            //cout << "wp " << i << " = " << wp[i] << endl; 
        } 
        for (int i = 0; i < n; ++i) {   
            int numop = 0;
            for (int op = 0; op < n; ++op) {
                if (op == i) continue;
                if (s[i][op] == '.') continue;
                int now = 0;
                int nog = 0;
                for (int j = 0; j < n; ++j) {
                    if (j == i) continue;
                    if (j == op) continue;
                    now += (s[op][j] == '1'); 
                    nog += (s[op][j] != '.');
                }
                double wpc =  (double) now / (nog);
                //cout << "wp of " << op << " after for " << i << " is " << wpc << endl; 
                owp[i] += wpc;
                ++numop;
            }
            owp[i] /= numop;


            //cout << "owp " << i << " = " << owp[i] << endl; 
        }

        vector < double > rpi(n);
        for (int i = 0; i < n; ++i) {
            int numop = 0;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (s[i][j] == '.') continue;
                oowp[i] += owp[j];
                ++numop;
            }
            oowp[i] /= (numop);
            rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
            printf("%.9lf\n", rpi[i]);
        }
        
        

    }





    return 0;
}

