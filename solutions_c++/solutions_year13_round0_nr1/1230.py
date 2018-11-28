#include <cstdio>

int T;
char map[10][10];
int num[10];
int dots;
char res[][100]={"X won", "O won", "Draw", "Game has not completed"};
int vysl;

int main()
{
	scanf("%d\n", &T);

	for(int q=1; q<=T; q++) {
		for(int i=0; i<4; i++) scanf("%s\n", map[i]);

		vysl=-1;
		dots=0;

		for(int i=0; i<4; i++) {
			num[0]=num[1]=0;
			for(int j=0; j<4; j++) {
				if(map[i][j]=='X') num[0]++;
				else if(map[i][j]=='O') num[1]++;
				else if(map[i][j]=='T') {num[0]++; num[1]++;}
				else dots++;
			}
			if(num[0]==4) vysl=0;
			else if(num[1]==4) vysl=1;
		}

		for(int i=0; i<4; i++) {
			num[0]=num[1]=0;
			for(int j=0; j<4; j++) {
				if(map[j][i]=='X') num[0]++;
				else if(map[j][i]=='O') num[1]++;
				else if(map[j][i]=='T') {num[0]++; num[1]++;}
			}
			if(num[0]==4) vysl=0;
			else if(num[1]==4) vysl=1;
		}

		num[0]=num[1]=0;
		for(int i=0; i<4; i++) {
			if(map[i][i]=='X') num[0]++;
			else if(map[i][i]=='O') num[1]++;
			else if(map[i][i]=='T') {num[0]++; num[1]++;}
		}
		if(num[0]==4) vysl=0;
		else if(num[1]==4) vysl=1;

		num[0]=num[1]=0;
		for(int i=0; i<4; i++) {
			if(map[3-i][i]=='X') num[0]++;
			else if(map[3-i][i]=='O') num[1]++;
			else if(map[3-i][i]=='T') {num[0]++; num[1]++;}
		}
		if(num[0]==4) vysl=0;
		else if(num[1]==4) vysl=1;

		if(vysl==-1) {
			if(dots) vysl=3;
			else vysl=2;
		}

		printf("Case #%d: %s\n", q, res[vysl]);
	}

	return 0;
}
