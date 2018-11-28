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
	//freopen( "file.txt", "w", stdout );
	ifs >> Test;
	REP(test, Test){
		//printf("case %d\n", test+1);
		int A, B;
		int ret = 0;
		string str;
		ifs >> A >> B;
		for(int i=A; i<=B; i++){
			str = toString(i);
			int n = str.length();
			if(n<7){
				str += str;
				set<int> q;
				for(int j=1; j<n; j++){
					string str2 = str.substr(j, n);
					int p = toInt(str2);
					if(!EXIST(q, p)){
						if(p>i && p<=B){
							//printf("%d %d\n", i, p);
							ret++;
						}
						
					}
					q.insert(p);
				}
			}else{
				str += str;
				set<int> q;
				for(int j=1; j<n; j++){
					if( str[j] > '1')continue;
					string str2 = str.substr(j, n);
					int p = toInt(str2);
					if(!EXIST(q, p)){
						if(p>i && p<=B){
							//printf("%d %d\n", i, p);
							ret++;
						}
						
					}
					q.insert(p);
				}
			}
		}
		fprintf(ofp, "Case #%d: %d\n", test+1, ret);
	}
}
