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
#include <ctime>
using namespace std;

typedef long long ll;

#define ALL(a)	(a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))

const double EPS = 1e-10;
const double PI  = acos(-1.0);

inline ll toInt(const string& s) {ll v; istringstream sin(s);sin>>v;return v;}
template<class T>inline T gcd(T a,T b){T tmp;while(b){tmp=a%b;a=b;b=tmp;}return a;}
template<class T>inline T lcm(T a,T b){return a / gcd(a,b) * b;}
template<class T>inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T>inline T sqr(T x) {return x*x;}

#define dump(x) cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;


template<class T> void print(int test_case,T answer){
	cout << "Case #" << test_case+1 << ": " << answer << endl;
}


int main(){
	int T;
	cin >> T;
	int r,c;
	string s[100];
	for(int i=0;i<T;++i){
		cin >> r >> c;
			
			
		for(int j=0;j<r;++j){
			cin >> s[j];
		}
		
		bool flag = true;
		
		for(int j=0;j<r;++j){
			for(int k=0;k<c;++k){
				if( s[j][k] == '#' ){
					if( j<r-1 && k < c-1 && s[j+1][k] == '#' &&s[j][k+1] == '#' &&s[j+1][k+1] == '#' ){
						s[j][k]  = '/';
						s[j][k+1] = '\\';
						s[j+1][k] = '\\';
						s[j+1][k+1] = '/';
					}else{
						flag = false;
						goto exit;
					}
				}
			}
		}
		exit:;
		
		cout << "Case #" << i+1 << ":" << endl;
		if( flag ){
			for(int j=0;j<r;++j){
				cout << s[j] << endl;
			}
		}else{
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
