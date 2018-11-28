//include
//------------------------------------------
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

long long solve(int L, long long time, int N, vector<int>& distance, int C) {
    cerr << L << "/" << time << "/" << N << "/" << C << endl;

    vector< pair<int, int> > distList;
    REP(c, C) distList.push_back(pair<int, int>(distance[c], c));
    SORT(distList);

    long long elapsed = 0;

    int remainDistance = 0;
    int curIndex = 0;
    int processedNum = 0;
    REP(n, N) {
        processedNum ++;
        curIndex = n;
        int timeToNext = distance[n % C] * 2;
        if (timeToNext < time) {
            time -= timeToNext;
            elapsed += timeToNext;
        } else {
            remainDistance = distance[n % C] - time / 2;
            elapsed += time;
            break;
        }
    }

    for (int c = C-1; c >= 0; c--) {
        if (remainDistance > distList[c].first) {
            if (L > 0) {
                L--;
                elapsed += remainDistance;
            } else {
                elapsed += remainDistance * 2;
            }
            remainDistance = 0;
        }
        int numRep = (N / C + ((N % C > distList[c].second) ? 1 : 0)) - 
                    (processedNum / C + ((processedNum % C > distList[c].second) ? 1 : 0));
        if (numRep <= L) {
            elapsed += distList[c].first * numRep;
            L -= numRep;
        } else {
            elapsed += distList[c].first * L + distList[c].first * (numRep - L) * 2;
            L = 0;
        }
    }
    if (remainDistance > 0) {
        if (L > 0) {
            L--;
            elapsed += remainDistance;
        } else {
            elapsed += remainDistance * 2;
        }
        remainDistance = 0;
    }

    return elapsed;
}

int main()
{
    int T, L, N, C;
    long long time;
    cin >> T;
    
    REP(t, T) {
        // input
        cin >> L ;
        cin >> time >> N >> C;
        vector<int> distance(C);
        REP(c, C) cin >> distance[c];

        // solve
        int result = solve(L, time, N, distance, C);

        // output
        cout << "Case #" << t+1 << ": " << result << endl;
    }
}


