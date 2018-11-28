//	Google Code Jam 2009
//	Round 1B
//	B. The Next Number

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

char sn[50];
int snl;
int df[128];

void doWork() {
	int ntc;
	fscanf(inpf, "%d", &ntc);

	for (int i = 1; i <= ntc; i++) {
		*sn = '0';
		fscanf(inpf, "%s", sn + 1);
		snl = strlen(sn);
		memset(df, 0, sizeof df);

		for (int j = snl - 1; j >= 0; j--) {
			char dc = sn[j];
			df[dc]++;
			while (++dc <= '9' && !df[dc]);

			if (dc <= '9') {
				sn[j] = dc;
				df[dc]--;

				for (char k = '0', m = j + 1; k <= '9'; k++) {
					while (df[k]--) {
						sn[m++] = k;
					}
				}

				fprintf(outf, "Case #%d: %s\n", i, *sn == '0' ? sn + 1 : sn);
				break;
			}
		}
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
