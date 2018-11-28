#include<iostream>
#include<string>
#include<cstring>
using namespace std;

const char* welcome = "welcome to code jam";
int L;

int N;
string line;

int cc[512][20];
int dp(int at, int m) {
    if(m == L) return 1;
    if(at == line.size()) return 0;
    int& ret = cc[at][m];
    if(ret >= 0) return ret;
    ret = 0;
    if(line[at] == welcome[m]) {
	ret += dp(at + 1, m + 1);
    }
    ret += dp(at + 1, m);
    ret %= 10000;
    return ret;
}

int main() {
    L = strlen(welcome);
    cin >> N;
    getline(cin, line);
    for(int i = 1; i <= N; ++i) {
	getline(cin, line);
	memset(cc, -1, sizeof(cc));
	int ans = dp(0, 0);
	cout << "Case #" << i << ": ";
	if(ans < 1000) cout << 0;
	if(ans < 100) cout << 0;
	if(ans < 10) cout << 0;
	cout << ans;
	cout << endl;
    }
    return 0;
}

