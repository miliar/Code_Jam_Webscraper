#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,n) FORD(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define MP make_pair
#define FT first
#define SD second
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;
typedef istringstream ISS;
typedef ostringstream OSS;



int main()
{
    int N, ni;
    cin >> N;
    REP(ni, N)
    {
        int keyl, keyn, letn;
        cin >> keyl >> keyn >> letn;

        VI freqs;

        REP(i, letn)
        {
            int f;
            cin >> f;
            freqs.push_back(f);
        }

        sort(ALL(freqs));
        reverse(ALL(freqs));

        int ps = 0;
        int sum = 0;

        REP(i, letn)
        {
            if (i % keyn == 0)
                ++ps;
            sum+= ps * freqs[i];
        }

        cout << "Case #" << ni + 1 << ": " << sum << endl;
    }
}























