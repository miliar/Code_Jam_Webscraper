#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
using namespace std;
const string S = "-welcome to code jam";
const int MAXN = 510;
const int MODS = 10000;
int f[MAXN][20 + 1];
int main(){
	int cases;
	cin >> cases;
	getchar();
	for (int tt = 0; tt < cases; ++tt){
		string str;
		getline(cin, str);
		str = '-' + str;
		memset(f, 0, sizeof(f));
		f[0][0] = 1;
		for (int i = 0; i < str.size(); ++i){
			for (int j = 0; j < S.size(); ++j){
				if (str[i] != S[j]) continue;
				for (int k = 0; k < i; ++k){
					f[i][j] += f[k][j - 1];
					f[i][j] %= MODS;
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < str.size(); ++i){
			ans += f[i][S.size() - 1];
			ans %= MODS;
		}
		ostringstream out;
		out << ans;
		string output = "0000" + out.str();
		printf("Case #%d: %s\n", tt + 1, output.substr(output.size() - 4, 4).c_str());
	}
	return 0;
}