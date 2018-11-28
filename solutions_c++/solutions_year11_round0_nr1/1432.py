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

int pos[2];
int P[128], R[128];

int main(void)	{
	int C, n;
	cin >> C;
	FOR (nc, 1, C+1)	{
        cin >> n;
        FOR (i, 0, n)   {
            char c;
            cin >> c >> P[i];
            R[i] = (c == 'B' ? 0 : 1);
        }
        
        int i = 0;

        int elapse = 0;
        pos[0] = 1;
        pos[1] = 1;
        FOR (i, 0, n)   {
            //cout << R[i] << ", " << P[i] << endl;
            int t = abs(pos[R[i]] - P[i]) + 1;
            
            //find next position of the one who isn't pressing a button
            int j = i;
            while (j < n && R[j] == R[i])   j++;
            int togo2, t2;
            if (j >= n) {
                togo2 = pos[1-R[i]];
                t2 = 0;
            }
            else    {
                togo2 = P[j];
                t2 = abs(P[j] - pos[1-R[i]]);
            }

            elapse += t;
            pos[R[i]] = P[i];
            if (t >= t2) {
                pos[1-R[i]] = togo2;
            }
            else {
                int sgn = (P[j] > pos[1-R[i]] ? 1 : -1);
                pos[1-R[i]] += sgn*t;
            }
            //cout << elapse << endl;
        }
        
		cout << "Case #" << nc << ": " << elapse << endl;
	}
	
	
}
