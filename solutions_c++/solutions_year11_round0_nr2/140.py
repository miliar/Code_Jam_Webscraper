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

vector<char> solve(vector<string>& combinations, vector<string>& opposites, string& list)
{
    vector<char> result;
    for (int i = 0; i < list.size(); i++) {
        if (result.size() == 0) {
            result.push_back(list[i]);
            continue;
        }
        // check combination
        bool combined = false;
        for (int j = 0; j < combinations.size(); j++) {
            if ((result.back() == combinations[j][0] && list[i] == combinations[j][1])
                    || result.back() == combinations[j][1] && list[i] == combinations[j][0]) {
                combined = true;
                result.pop_back();
                result.push_back(combinations[j][2]);
                break;
            }
        }
        if (!combined) result.push_back(list[i]);

        // check clearance
        for (int j = 0; j < opposites.size(); j++) {
            if (find(result.begin(), result.end(), opposites[j][0]) != result.end()
                    && find(result.begin(), result.end(), opposites[j][1]) != result.end()) {
                result.clear();
                break;
            }
        }
    }
    
    return result;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int C, D;
        string temp;
        vector<string> combinations;
        vector<string> opposites;
        cin >> C;
        for (int c = 0; c < C; c++) {
            cin >> temp;
            combinations.push_back(temp);
        }
        cin >> D;
        for (int d = 0; d < D; d++) {
            cin >> temp;
            opposites.push_back(temp);
        }
        cin >> temp;
        cin >> temp;
        vector<char> result = solve(combinations, opposites, temp);
        cout << "Case #" << t+1 << ": [";
        for (int i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i != result.size() - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
}


