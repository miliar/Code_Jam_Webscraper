#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int N, K;
		cin >> N >> K;
		
		printf("Case #%d: %s\n", t + 1, ((1 << N) & (K ^ (K + 1))) != 0 ? "ON" : "OFF");
	}
	
	return 0;
}
