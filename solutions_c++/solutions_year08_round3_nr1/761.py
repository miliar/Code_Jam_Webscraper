
#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define PB push_back
#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef pair <int, VI> PIVI;
typedef long long ll;


int main () 
{
    freopen("c:\\input.txt", "r", stdin);
    freopen("c:\\output.txt", "w", stdout);

    int numOfCases = 0;
    cin >> numOfCases;
    REP(i,numOfCases)
    {
        int P;
        int K;
        int L;
        int count = 0;
        VI k;
        cin >> P >> K >> L;
        vector<int> key(K,0);
        REP(j,L)
        {
            int xx;
            cin >> xx;
            k.push_back(xx);
        }
        SORT(k);
        reverse(ALL(k));
        int used = 0;
        int sum = 0;
        REP(j,L)
        {
            if (used == K)
            {
                used = 0;
            }

            while(key[used] >P)
            {
                used ++;
                if (used == K)
                    used = 0;
            }
            key[used]++;
                count += k[j]*key[used];
                used++;
        }




        cout << "Case #" << i+1 <<": " << count << endl;
    }
        fclose(stdout);
    fclose(stdin);
}