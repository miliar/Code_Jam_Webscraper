#include <cstdio>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

int t, c, d, n, m, have[256];
vector <char> ban[256];
char s[200], g[256][256], a[200];

void clean(){
	for (int i = 0; i < 256; i++){
		for (int j = 0; j < 256; j++)
			g[i][j] = 0;
		ban[i].clear();
	}
	memset(have, 0, sizeof have);
	m = c = d = n = 0;
}

void solve (){
	scanf("%d", &c);
	for (int i = 0; i < c; i++){
		scanf("%s", s);
		g[s[0]][s[1]] = g[s[1]][s[0]] = s[2];
	}
	scanf("%d", &d);
	for (int i = 0; i < d; i++){
		scanf("%s", s);
		ban[s[0]].push_back(s[1]);
		ban[s[1]].push_back(s[0]);
	}
	scanf("%d%s", &n, s);
	for (int i = 0; i < n; i++){
		a[m] = s[i];
		if (m && g[a[m]][a[m - 1]] != 0){
			have[a[m - 1]]--;
			a[m - 1] = g[a[m]][a[m - 1]];
		}
		else{
			have[a[m]]++;
			m++;
			for (int j = 0; j < ban[a[m - 1]].size(); j++)
				if (have[ban[a[m - 1]][j]]){
					m = 0; memset(have, 0, sizeof have);
					break;
				}
		}
	}
	printf("[");
	for (int i = 0; i < m - 1; i++)
		printf("%c, ", a[i]);
	if(m)printf("%c", a[m - 1]);
	printf("]\n");
	clean();
}

int main (){
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}


