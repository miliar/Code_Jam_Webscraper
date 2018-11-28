#include <iostream>
#include <map>
#include <cmath>
#include <algorithm>
#include <utility>
using namespace std;

map < pair<int, long long>, long long> dp;
string line;

long long recur(int pos, long long acum) {
	pair <int, long long> p = make_pair(pos, acum);
	if(pos == line.size()) {
		acum = abs(acum);
		if((acum%2 == 0) || (acum%3 == 0) || (acum%5 == 0) || (acum%7 == 0))
			return 1;
		return 0;
	}
	
	if(dp.find(p) != dp.end())
		return dp[p];
	
	dp[p] = 0;
	for(int i = pos; i < line.size(); i++) {
		long long num = 0;
		for(int j = pos; j <= i; j++) {
			num *= 10;
			num += (line[j]-'0');
		}
		dp[p] += recur(i+1, acum+num);
		if(pos != 0)
			dp[p] += recur(i+1, acum-num);
	}
	
	return dp[p];
}

int main() {
	int N;
	cin >> N;
	for(int nacho = 1; nacho <= N; nacho++) {
		cin >> line;
		dp.clear();
		cout << "Case #" << nacho << ": " << recur(0, 0) << endl;
	}
	
	return 0;
}
