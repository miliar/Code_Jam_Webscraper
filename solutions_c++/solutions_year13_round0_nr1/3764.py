#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;


char b[4][10];

int check(char c){
	for(int i = 0; i < 4; i++){
		int j;
		for(j = 0; j < 4; j++)
			if(b[i][j] != c && b[i][j] != 'T')break;
		if(j == 4)return 1;
	}

	for(int i = 0; i < 4; i++){
		int j;
		for(j = 0; j < 4; j++)
			if(b[j][i] != c && b[j][i] != 'T')break;
		if(j == 4)return 1;
	}

	int j;
	for(j = 0; j < 4; j++)
		if(b[j][j] != c && b[j][j] != 'T')break;
	if(j == 4)return 1;
	for(j = 0; j < 4; j++)
		if(b[j][3-j] != c && b[j][3-j] != 'T')break;
	if(j == 4)return 1;
	return 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int ti = 1; ti <= tc; ti++){
		for(int i = 0; i < 4; i++)
			scanf("%s", b[i]);
		printf("Case #%d: ", ti);
		if(check('X'))printf("X won\n");
		else if(check('O'))printf("O won\n");
		else {
			int ec = 0;
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; j++)
					if(b[i][j] == '.')ec++;
			if(ec == 0)printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
	return 0;
}