#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>

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

char mapping[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int t;
string line;

void Test(int num){
	cout << "Case #" << num << ": ";
	getline(cin, line);
	REP(i, line.length()){
		if(line[i] == ' ') cout << " ";
		else cout << mapping[line[i] - 'a'];
	}
	cout << endl;
}

int main(){
	cin >> t;
	getline(cin, line);
	FOR(i, 1, t) Test(i);
	return 0;
}