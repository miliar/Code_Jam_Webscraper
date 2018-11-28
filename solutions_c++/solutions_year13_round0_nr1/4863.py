#include <cstdio>
#include <string>
#include <map>

using namespace std;

int u[10][4][2] = {
	{{0,0},{0,1},{0,2},{0,3}},
	{{1,0},{1,1},{1,2},{1,3}},
	{{2,0},{2,1},{2,2},{2,3}},
	{{3,0},{3,1},{3,2},{3,3}},
	{{0,0},{1,0},{2,0},{3,0}},
	{{0,1},{1,1},{2,1},{3,1}},
	{{0,2},{1,2},{2,2},{3,2}},
	{{0,3},{1,3},{2,3},{3,3}},
	{{0,3},{1,2},{2,1},{3,0}},	
	{{0,0},{1,1},{2,2},{3,3}},
	};

int work() {
	bool empty = false;
	char s[4][5];
	for (int i = 0; i < 4; ++i) {
		scanf("%s", s[i]);
		for (int j = 0; j < 4; ++j)
			if (s[i][j] == '.') empty = true;
	}
	for (int i = 0; i < 10; ++i) {
		map<char,int> count;
		for (int j = 0; j < 4; ++j) count[s[u[i][j][0]][u[i][j][1]]]++;
		if (count['X'] + count['T'] >= 4) return 0;
		if (count['O'] + count['T'] >= 4) return 1;
	}
	return empty ? 3 : 2;
}

int main(int argc, char const *argv[])
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		int ret = work();
		printf("Case #%d: ", i + 1); 
		if (ret == 0) printf("X won\n");
		else if (ret == 1) printf("O won\n");
		else if (ret == 2) printf("Draw\n");
		else printf("Game has not completed\n");
	}	
	return 0;
}