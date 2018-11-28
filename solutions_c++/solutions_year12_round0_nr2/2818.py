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
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

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

void main(int argc, char *argv[]){//GCJTemp
	int Test;
	ifstream ifs("as.in");
	FILE *ofp = fopen("as.out", "w");
	ifs >> Test;
	REP(test, Test){
		int ret = 0;
		int N, S, p;
		int t[100];
		ifs >> N >> S >> p;
		REP(i, N)ifs>>t[i];
		REP(i, N){
			if(t[i] > 3*p-3){
				ret++;
			}else if(t[i] > 3*p-5){
				if(t[i] < 2 || t[i] >28)continue;
				if(S > 0){
					ret++;
					S--;
				}
			}
		}

		fprintf(ofp, "Case #%d: %d\n", test+1, ret);
	}
}
