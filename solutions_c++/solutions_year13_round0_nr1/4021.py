#include <iostream>
#include <string>
#include <cstdio>
#include <map>

using namespace std;

char win(string s) {
	///printf("$%s$\n", s.c_str());
	int n = s.length();
	map<char, int> h;
	for(int i = 0; i < n; ++i)
		++ h[s[i]];
	if(h['X'] == 4 || (h['X'] == 3 && h['T'] == 1))
		return 'X';
	if(h['O'] == 4 || (h['O'] == 3 && h['T'] == 1))
		return 'O';
	return 0;
}

int main()
{
	//freopen("1.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	int T;
	cin >> T;
	int MAXN = 4;
	for(int n = 0; n < T; ++n) {
		string s[MAXN];
		bool f = true;
		for(int i = 0; i < MAXN; ++i) {
			cin>>s[i];
			
			for(int j = 0; j < s[i].length(); ++j) {
				if(s[i][j] == '.') {
					f = false;
				}
			}
		}
		string blank;
		///getline(cin, blank);
		
		for(int i = 0; i < MAXN; ++i) {
			string t1, t2, t3, t4;
			for(int j = 0; j < MAXN; ++j) {
				t1 += s[i][j];
				t2 += s[j][i];
				t3 += s[j][j];
				t4 += s[MAXN - j - 1][j];
			}
			
			if(win(t1)) {
				printf("Case #%d: %c won\n", n + 1, win(t1));
				goto end;
			}
			if(win(t2)) {
				printf("Case #%d: %c won\n", n + 1, win(t2));
				goto end;
			}
			if(win(t3)) {
				printf("Case #%d: %c won\n", n + 1, win(t3));
				goto end;
			}
			if(win(t4)) {
				printf("Case #%d: %c won\n", n + 1, win(t4));
				goto end;
			}
		}
		if(!f) {
			printf("Case #%d: Game has not completed\n", n + 1);
			goto end;
		}
		printf("Case #%d: Draw\n", n + 1);
	end: ;
	}
	return 0;
}
