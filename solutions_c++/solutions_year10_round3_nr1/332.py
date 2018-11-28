#include <boost/config.hpp>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>
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
#define PI(a,b) (make_pair(a,b));


bool greaterpair(pair<int,int> a, pair<int,int> b) {
        return a.first < b.first;
}
int sum = 0;


int main() {
    int T;
    cin >> T;
    FOR(i,1,T+1) {
            int N; cin >> N;
            vector<pair<int,int> > windows;
            FOR(j,0,N) {
                    int a,b;
                    cin >> a >> b;
                    windows.push_back(make_pair(a,b));
            }
            sort(windows.begin(),windows.end(),greaterpair);
            sum = 0;
            for(vector<pair<int,int> >::iterator it = windows.begin(); it != windows.end(); it++) {
                for (vector<pair<int,int> >::iterator it2 = it+1; it2 != windows.end(); it2++) {
                    if (it2->second < it->second) sum++;
                }
            }
            cout << "Case #" << i << ": "  << sum <<  endl;

    }
}


