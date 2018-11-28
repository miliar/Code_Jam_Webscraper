#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int sz = 26;

vector<vector<char> > ch;
vector<vector<bool> > depr;
vector<char> ans;
int len ;
char base[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

bool isbase(char c){
	for (int i = 0; i < 8; ++i)
		if (base[i] == c) return true;
	return false;
}

void add(char c){
	if (len == 0 || ch[c- 'A'][ans[len-1] - 'A'] == 0 ){
		ans[len++] = c;
		for (int i = 0; i < len; ++i)
		if (depr[c-'A'][ans[i] - 'A']){
			len = 0;
			break;
		}
	} else {
		//--len;
		//add(ch[c- 'A'][ans[len] - 'A']);
		ans[len - 1] = ch[c- 'A'][ans[len -1] - 'A'];
	}
}

void solve(){
	len = 0;
	ch.resize(sz);
	depr.resize(sz);
	for (int i = 0; i < sz; ++i){
		ch[i].assign(sz, 0);
		depr[i].assign(sz, 0);
	}

	string s;
	int C, i, j;
	cin >> C;
	while (C --> 0){
		cin >> s;
		if (!isbase(s[0]) || !isbase(s[1])) {
			continue;
		}
		i = s[0] - 'A';
		j = s[1] - 'A';
		ch[i][j] = ch[j][i] = s[2];
	}

	cin >> C;
	while (C --> 0){
		cin >> s;
		if (!isbase(s[0]) || !isbase(s[1])) {
			continue;
		}
		i = s[0] - 'A';
		j = s[1] - 'A';
		depr[i][j] = depr[j][i] = true;
	}

	cin >> C;
	ans.assign(C, false);
	cin >> s;
	for (int i = 0; i < C; ++i){
		add(s[i]);
	}

	printf("[");
	for (int i = 0; i < len - 1; ++i)
		printf("%c, ", ans[i]);
	if (len) printf("%c", ans[len-1]);
	printf("]\n");
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}