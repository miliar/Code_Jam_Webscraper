#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <map>

using namespace std;

#define REP(i, x) for(int i = 0; i < x; ++ i)
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define ALL(c) (c).begin(), (c).end()
#define MX 80000
#define INF 1000000000

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

int a, b, t;

int Calc(int num){
	int ret = 0;
	map<PII, bool> mapa;
	stringstream ss;
	ss << num;
	string number = ss.str();
	FOR(i, 1, number.size() - 1){
		int x = atoi( string( number.substr(i) + number.substr(0, i)).c_str() );
		if(x > num && x <= b && mapa[ MP(num, x) ] == false){
				mapa[ MP(num, x) ] = true;
				//cout << num << " " << atoi( string( number.substr(i) + number.substr(0, i)).c_str() ) << endl;
				++ret;
		}
	}
	return ret;
}

void Test(int num){
	cout << "Case #" << num << ": ";
	int res = 0;
	cin >> a >> b;
	FOR(i, a, b - 1)
		res += Calc(i);
	cout << res << "\n";
}

int main(){
	cin >> t;
	FOR(i, 1, t) Test(i);
	return 0;
}