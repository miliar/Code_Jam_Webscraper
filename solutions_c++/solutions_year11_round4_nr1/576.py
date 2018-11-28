#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

double X, S, R, t;
int N;
vector<pair<pair<double, double>, double> > v;
vector<pair<double, double> > ints;

int main(void)	{
	int T;
	cin >> T;
	FOR (nc, 1, T+1)	{
        v.clear();
        ints.clear();
        
        cin >> X >> S >> R >> t >> N;
        if (R < S)  R = S;
        FOR (i, 0, N)   {
            int a, b, c;
            cin >> a >> b >> c;
            v.PB(MP(MP(a, b), c));
        }
        SORT(v);
        
        
        FOR (i, 0, N)   {
            if (i == 0) {
                if (v[i].first.first > 0) {
                    ints.PB(MP(0, v[i].first.first));
                }
            }
            else    {
                if (v[i].first.first > v[i-1].first.second)    {
                    ints.PB(MP(0, v[i].first.first - v[i-1].first.second));
                }
            }
            ints.PB(MP(v[i].second, v[i].first.second - v[i].first.first));
        }
        if (v[N - 1].first.second < X)    {
            ints.PB(MP(0, X - v[N - 1].first.second));
        }

        SORT(ints);
/*                
        FOR (i, 0, ints.SZ) {
            cout << ints[i].first << "\t" << ints[i].second << endl;
        }
 */   
        
                
        double tot = 0.;
        FOR (i, 0, ints.SZ) {
            double base = ints[i].first;
            double d = ints[i].second;

            if ((base + R)*t >= d)  {
                t -= d / (base + R);
                tot += d / (base + R);
//                cout << d / (base + R) << endl;
            }
            else    {
                double drem = d - t*(base + R);
                tot += t;
                tot += drem / (base + S);
//                cout << t << "\t" << drem / (base + S) << endl;
                t = 0.;    
            }
        }
        
		cout << "Case #" << nc << ": ";
        printf("%0.9lf\n", tot);
	}
	
	
}
