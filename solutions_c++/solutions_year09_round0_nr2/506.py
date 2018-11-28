#include <stdio.h>

char sinkid[102][102];

char* root[102][102];

int altitude[102][102]; // +1


int dir[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

char* getroot(int x, int y) {
	if (root[x][y]) return root[x][y];

	int alt = altitude[x+1][y+1];

	int lalt = alt;
	char* ret = &(sinkid[x][y]);

	for (int i=0; i < 4; i++) {
		int talt = altitude[x+1+dir[i][0]][y+1+dir[i][1]];
		if (talt < lalt) {
			lalt = talt;
			ret = getroot(x+dir[i][0],y+dir[i][1]);
		}
	}

	return root[x][y] = ret;
}

int main() {
	FILE* fid = fopen("B-large.in", "r");
	FILE* fout = fopen("B.out", "w");

	int T = 0;

	fscanf(fid, "%d", &T);

	for (int cas = 1; cas <= T; ++cas) {

		fprintf(fout, "Case #%d:\n", cas);

		for (int x=0; x<102; x++) {
			for (int y=0;y<102;y++) {
				altitude[x][y] = 20000;
				sinkid[x][y] = '\0';
				root[x][y] = 0;
			}
		}

		int H, W;

		fscanf(fid, "%d%d", &H, &W);

		for (int y=0; y < H; y++){
			for (int x=0; x<W; x++) {
				fscanf(fid, "%d", &(altitude[x+1][y+1]));
			}
		}

		char nextletter = 'a';

		for (int y=0; y < H; y++) {
			for (int x=0; x<W; x++) {
				char* cptr = getroot(x,y);
				if ('\0' == *cptr) *cptr = nextletter++;

				fprintf(fout, "%c ", *cptr);

				//fprintf(fout, "%d ", altitude[x+1][y+1]);
			}
			fprintf(fout, "\n");
		}


	}


	return 0;
}

