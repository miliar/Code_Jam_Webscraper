#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <list>
#include <map>
#include <cmath>

using namespace std;

const char* welcome = "welcome to code jam";
const int len = 19;
char line[512];
int lineSize;

int memo[512][32];

int f(int x, int y) {	
	if(y == len) return 1;
	if(x == lineSize) return 0;
	int &result = memo[x][y];
	if(result == -1) result = (f(x+1, y) + ((line[x] == welcome[y])?f(x+1, y+1):0))%10000;
	return result;
}


void solve() {
	cin.getline(line, 512);
	lineSize = strlen(line);	
	memset(memo, -1, sizeof(memo));

	int result = f(0, 0);
	for(int i = 10; i <= 1000; i*=10) if(result < i) cout << "0";
	cout << result;
}


int main() {		
	int C;
	cin >> C;
	cin.getline(line, 512);
	for(int i = 1; i <= C; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}