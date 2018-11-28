#include <cstdio>
#define OMAX 10000
using namespace std;
#include <algorithm>
#include <iostream>
#include <string>

#define MAXN 1100
#define MAXD 100

string need = "welcome to code jam";

int res[MAXN][MAXD];

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d\n", &t);
	for (int tt = 1; tt <= t; tt++){
		string s;
		getline(cin, s);
		cerr<<tt<<endl;
//		cerr<<s<<endl;
		for (int i = 0; i < MAXN; i++)
			for (int j = 0; j < MAXD; j++)
				res[i][j] = 0;
		res[0][0] = 1;
		for (int i = 0; i < s.size(); i++)
			for (int j = 0; j <= need.size(); j++){
				res[i + 1][j] = (res[i + 1][j] + res[i][j]) % OMAX;
				if ((j != need.size()) && (need[j] == s[i]))
					res[i + 1][j + 1] = (res[i + 1][j + 1] + res[i][j]) % OMAX;
			}
		printf("Case #%d: %04d\n", tt, res[s.size()][need.size()]);
	}
	return 0;
}
