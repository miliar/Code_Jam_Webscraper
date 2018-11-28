#include<cstdio>

int main () {
	int ncase;
	scanf("%d", &ncase);
	char map[4][5];
	for(int c=1; c<=ncase; c++) {
		printf("Case #%d: ", c);
		for(int i=0;i<4;i++) scanf("%s", map[i]);
		
		int stat=0;
		bool finish = true;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++) 
				if(map[i][j] =='.') {
					finish = false;
					map[i][j] = 0;
				}
		
		for(int i=0;i<4 && !stat;i++) {
			bool fin;
			if(map[i][0]) {
				fin = true;
				for(int j=1; j<4; j++)
					if(!(map[i][j] == map[i][0] || map[i][j] =='T')) {
						fin = false;
						break;
					}
				if(fin) {
					int c = map[i][0] == 'T' ? 1 : 0;
					stat = map[i][c] == 'X' ? 1 : 2;
					break; 
				}
			}
			if(map[0][i]) {
				fin = true;
				for(int j=1; j<4; j++)
					if(!(map[j][i] == map[0][i] || map[j][i] == 'T')) {
						fin = false;
						break;
					}
				if(fin) {
					int c = map[0][i] == 'T' ? 1 : 0;
					stat = map[c][i] == 'X' ? 1 : 2;
					break;
				}
			}
		}
		if(!stat) {
			bool fin;
			if(map[0][0]) {
				fin = true;
				for(int i=1;i<4;i++)
					if(!(map[i][i] == map[0][0] || map[i][i] == 'T')) {
						fin = false;
						break;
					}
				if(fin) {
					int c = map[0][0] == 'T' ? 1 : 0;
					stat = map[c][c] == 'X' ? 1 : 2;
				}
			}
			if(map[0][3]) {
				fin = true;
				for(int i=1; i<4; i++)
					if(!(map[i][3-i] == map[0][3] || map[i][3-i] == 'T')) {
						fin = false;
						break;
					}
				if(fin) {
					int c = map[0][3] == 'T' ? 1 : 0;
					stat = map[c][3-c] == 'X' ? 1 : 2;
				}
			}
		}
		if(stat) printf("%c won\n", stat==1?'X':'O');
		else printf("%s\n", finish ? "Draw" : "Game has not completed");
	}
	return 0;
}
