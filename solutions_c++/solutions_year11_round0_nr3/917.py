#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)


void Go(){
	int n;
	scanf("%d", &n);
	VI cost(n);
	FOR(i, n)
		scanf("%d", &cost[i]);

	int x = 0;
	int sum = 0;
	FOR(i, n){
		x ^= cost[i];
		sum += cost[i];
	}
	if (x != 0){
		printf("NO");
		return;
	}
	sum -= *min_element(cost.begin(), cost.end());
	printf("%d", sum);
}

int main(){
	const string task = "C";
	const int attempt = -1;
	const bool dbg = false;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		ss << "gcj/2011/qual/";
		if (attempt < 0)
			ss << task << "-large";
		else
			ss << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	int t;
	scanf("%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}