#include <stdio.h>

char ent[16][16];

int won(char x) {
	int wonh = 1, wonv = 1, wonpd = 1, wonad = 1;
	for(int i = 0; i < 4; i++) {
		if(ent[i][i] != x && ent[i][i] != 'T') wonpd = 0;
		if(ent[i][3-i] != x && ent[i][3-i] != 'T') wonad = 0;
		for(int j = 0; j < 4; j++) if(ent[i][j] != x && ent[i][j] != 'T') wonh = 0;
		for(int j = 0; j < 4; j++) if(ent[j][i] != x && ent[j][i] != 'T') wonv = 0;
		if(wonh || wonv) return 1;
		wonh = wonv = 1;
	}
	return wonpd || wonad;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int caso = 1; caso <= T; caso++) {
		int pd = 0;
		for(int i = 0; i < 4; i++) {
			scanf("%s", ent[i]);
			for(int j = 0; j < 4; j++)
				if(ent[i][j] == '.') pd = 1;
		}
		printf("Case #%d: ", caso);

		if(won('X')) printf("X won\n");
		else if(won('O')) printf("O won\n");
		else if(pd) printf("Game has not completed\n");
		else printf("Draw\n");
	}
}
