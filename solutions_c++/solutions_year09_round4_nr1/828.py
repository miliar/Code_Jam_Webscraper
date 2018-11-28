//	Google Code Jam 2009
//	Round 2
//	A. Crazy Rows

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

#include <algorithm>

using namespace std;

FILE *inpf, *outf;

int md, dat[50];
char inpBuf[50];

void doWork() {
	int ntc;
	fscanf(inpf, "%d\n", &ntc);

	for (int i = 1; i <= ntc; i++) {
		fscanf(inpf, "%d", &md);

		for (int j = 0; j < md; j++) {
			fscanf(inpf, "%s", inpBuf);
			int loi;

			for (loi = md - 1; loi >= 0 && inpBuf[loi] == '0'; loi--);
			dat[j] = loi;
		}

		int res = 0;

		for (int j = 0; j < md; j++) {
			if (dat[j] <= j) {
				continue;
			}

			int k;

			for (int k = j + 1; k < md; k++) {
				if (dat[k] <= j) {
					int s = dat[k];

					for (int m = k; m > j; m--) {
						dat[m] = dat[m - 1];
					}

					dat[j] = s;
					res += k - j;
					break;
				}
			}
		}

		fprintf(outf, "Case #%d: %d\n", i, res);
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
