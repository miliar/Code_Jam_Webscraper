//	Google Code Jam 2010
//	Qualification Round
//	C. Theme Park

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
#include <string>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

FILE *inpf, *outf;

int rnds, maxLd, grpCnt, grpSzs[1010], nxtQb[1010];
long long rdVals[1010];

void doWork() {
	int ntc;
	fscanf(inpf, "%d", &ntc);

	for (int i = 1; i <= ntc; i++) {
		fscanf(inpf, "%d%d%d", &rnds, &maxLd, &grpCnt);

		for (int j = 0; j < grpCnt; j++) {
			fscanf(inpf, "%d", grpSzs + j);
		}

		for (int j = 0; j < grpCnt; j++) {
			int crs = 0, k = j;

			for (;;) {
				if (crs + grpSzs[k] > maxLd) {
					break;
				}

				crs += grpSzs[k];

				if (++k == grpCnt) {
					k = 0;
				}

				if (k == j) {
					break;
				}
			}

			nxtQb[j] = k;
			rdVals[j] = crs;
		}

		int cqb = 0;
		long long res = 0;

		while (rnds--) {
			res += rdVals[cqb];
			cqb = nxtQb[cqb];
		}

		fprintf(outf, "Case #%d: %lld\n", i, res);
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
