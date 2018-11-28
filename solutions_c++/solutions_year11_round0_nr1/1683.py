#include <stdio.h>
#include <stdlib.h>

#include <algorithm>

FILE* fid;
FILE* fout;


using namespace std;

int solve() {
	int elapsed = 0;

	int N;

	fscanf(fid, "%d ", &N);

	int lastloc[2];
	int lastelapsed[2];

	lastloc[0] = lastloc[1] = 1;
	lastelapsed[0] = lastelapsed[1] = 0;

	for (int i=0; i < N; i++) {
		char colour;
		int newloc;
		fscanf(fid, " %c %d", &colour, &newloc);

		int id = (colour == 'B') ? 1 : 0;



		//printf(" += 1 + max(0, %d - %d + abs(%d - %d))\n", lastelapsed[id],elapsed  , lastloc[id] , newloc);

		elapsed = elapsed + 1 + max(0, lastelapsed[id] - elapsed + abs(lastloc[id] - newloc));

		//printf("%c %d %d %d\n", colour, id, newloc, elapsed);

		lastloc[id] = newloc;
		lastelapsed[id] = elapsed;
	}

	//printf("\n");

	return elapsed;
}

int main(int argc, char** argv) {

	fid = fopen("A-large.in", "r");
	fout = fopen("A.out", "w");

	int T;
	fscanf(fid, "%d", &T);

	for (int i = 1; i <= T; i++) {
		fprintf(fout, "Case #%d: %d\n", i, solve());
	}

	return 0;
}