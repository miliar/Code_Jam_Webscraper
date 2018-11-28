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

int solve(vector<char>& color, vector<int>& pos) {
    int time = 0;
    int curPos[2]; curPos[0] = curPos[1] = 0;
    int avail[2]; avail[0] = avail[1] = 0; 

    for (int i = 0; i < color.size(); i++) {
        int curRobot = color[i] == 'O' ? 0 : 1;
        int waitingRobot = color[i] == 'O' ? 1 : 0; 

        // time needed to move to next pos
        int timeToMove = abs(pos[i] - curPos[curRobot]) - avail[curRobot];
        if (timeToMove < 0) timeToMove = 0;

        // move current robot
        time += timeToMove + 1;
        curPos[curRobot] = pos[i];
        avail[curRobot] = 0;

        // give avaliable time for waiting robot
        avail[waitingRobot] += timeToMove + 1;
    }

    return time;
}

int main()
{
    int T, N, P;
    char R;
    cin >> T;

    for (int t = 0; t < T; t++) {
        vector<char> color;
        vector<int> pos;
        cin >> N;
        for (int n = 0; n < N; n++) {
            cin >> R >> P;
            color.push_back(R);
            pos.push_back(P-1);
        }
        int result = solve(color, pos);
        cout << "Case #" << t+1 << ": " << result << endl;
    }
}


