//	Google Code Jam 2009
//	Qualification Round
//	C. Welcome to Code Jam

//	This code compiles in Visual C++ 2008 Express Edition
//	on Windows when placed in an empty CLR project.
//	The compiled program is intended to be called
//	from the command line.
//	For usage instructions see function main() below
//	or run the program without arguments.
//	During normal execution the program doesn't print
//	any progress information.

#include <cstdio>
#include <cstring>

#include <memory.h>

using namespace std;

FILE *inpf, *outf;

char *wm = "welcome to code jam";
int wml;
char tx[505];
int txl;
int dp[25][510];
char sb[100];

void doWork() {
	wml = strlen(wm);
	int ntc;
	fgets(sb, sizeof sb, inpf);
	sscanf(sb, "%d", &ntc);

	for (int i = 1; i <= ntc; i++) {
		fgets(tx, sizeof tx, inpf);
		txl = strlen(tx);
		tx[--txl] = '\0';
		memset(dp, sizeof dp, 0);

		for (int j = 0; j < 510; j++) {
			dp[0][j] = 1;
		}

		for (int r = 0; r < wml; r++) {
			dp[r + 1][0] = 0;
			char cc = wm[r];

			for (int s = 0; s < txl; s++) {
				dp[r + 1][s + 1] = dp[r + 1][s];

				if (tx[s] == cc) {
					dp[r + 1][s + 1] += dp[r][s];
					dp[r + 1][s + 1] %= 10000;
				}
			}
		}

		fprintf(outf, "Case #%d: %04d\n", i, txl ? dp[wml][txl] : 0);
	}
}

int main(int argc, char **argv) {
	inpf = outf = 0;
	int rescode = 0;

	if (argc != 3) {
		fputs("!! bad arguments\n"
			"usage: <command path> <input file path> <output file path>\n"
			"for example on Windows:\n"
			"C:\\gcj\\solution.exe C:\\gcj\\A-large.in C:\\gcj\\A-large.out\n"
			"if you are in C:\\gcj you can also use:\n"
			"solution.exe A-large.in A-large.out\n"
			"more generally, all paths can be absolute or relative\n",
			stderr);
		rescode = -1;
	} else if (!(inpf = fopen(argv[1], "r"))) {
		fprintf(stderr, "!! cannot open input file %s\n", argv[1]);
		rescode = -2;
	} else if (!(outf = fopen(argv[2], "w"))) {
		fprintf(stderr, "!! cannot open output file %s\n", argv[2]);
		rescode = -3;
	} else {
		doWork();
	}

	if (inpf && fclose(inpf)) {
		fprintf(stderr, "!! cannot close input file %s\n", argv[1]);

		if (!rescode) {
			rescode = -4;
		}
	}

	if (outf && fclose(outf)) {
		fprintf(stderr, "!! cannot close output file %s\n", argv[2]);

		if (!rescode) {
			rescode = -5;
		}
	}

	return rescode;
}
