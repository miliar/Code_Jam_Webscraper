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
#include <queue>
#include <climits>
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
typedef pair<int, int> P;
typedef long long ll;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
#define fi first
#define se second

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  FOR(i,0,n)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);
const int dx[] = {-1,1,0,0};
const int dy[] = {0,0,1,-1};

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int t, aki, a, b;
string s[4];
bool o, x;

int main(){
    cin >> t;
    rep(now, t){
	o = x = false;
	aki = 0;
	cout << "Case #" << now + 1 << ": ";
	rep(i, 4) cin >> s[i];
	rep(i, 4) rep(j, 4) aki += (s[i][j] != '.');
	rep(i, 4){
	    a = b = 0;
	    rep(j, 4){
		if(s[i][j] == 'X') ++a;
		else if(s[i][j] == 'O') ++b;
		else if(s[i][j] == 'T'){
		    ++a; ++b;
		}
	    }
	    if(a == 4){
		o = true;
	    }else if(b == 4){
		x = true;
	    }
	}
	rep(i, 4){
	    a = b = 0;
	    rep(j, 4){
		if(s[j][i] == 'X') ++a;
		else if(s[j][i] == 'O') ++b;
		else if(s[j][i] == 'T'){
		    ++a; ++b;
		}
	    }
	    if(a == 4){
		o = true;
	    }else if(b == 4){
		x = true;
	    }
	}
	a = b = 0;
	rep(i, 4){
	    if(s[i][i] == 'X') ++a;
	    else if(s[i][i] == 'O') ++b;
	    else if(s[i][i] == 'T'){
		++a; ++b;
	    }
	}
	if(a == 4){
	    o = true;
	}else if(b == 4){
	    x = true;
	}
	a = b = 0;
	rep(i, 4){
	    if(s[i][3 - i] == 'X') ++a;
	    else if(s[i][3 - i] == 'O') ++b;
	    else if(s[i][3 - i] == 'T'){
		++a; ++b;
	    }
	}
	if(a == 4){
	    o = true;
	}else if(b == 4){
	    x = true;
	}
	if(x){
	    cout << "O won";
	}else if(o){
	    cout << "X won";
	}else if(aki != 16){
	    cout << "Game has not completed";
	}else{
	    cout << "Draw";
	}
	cout << "\n";
    }
    return 0;
}
