//	Google Code Jam 2009
//	Qualification Round
//	A. Alien Language

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

#include <vector>
#include <algorithm>

using namespace std;

FILE *inpf, *outf;

int wlen, wcnt, pcnt;
char wlst[5000][20];
char pbuf[15 * 30];
vector <char> pdat[15];

void doWork() {
	fscanf(inpf, "%d %d %d", &wlen, &wcnt, &pcnt);

	for (int i = 0; i < wcnt; i++) {
		fscanf(inpf, "%s", wlst + i);
	}

	for (int i = 1; i <= pcnt; i++) {
		fscanf(inpf, "%s", pbuf);
		int pci = 0;

		for (int pdi = 0; pdi < wlen; pdi++) {
			vector <char> &cpd = pdat[pdi];
			cpd.clear();

			if (pbuf[pci] != '(') {
				cpd.push_back(pbuf[pci++]);
			} else {
				pci++;

				while (pbuf[pci] != ')') {
					cpd.push_back(pbuf[pci++]);
				}

				pci++;
			}

			sort(cpd.begin(), cpd.end());
			cpd.push_back('z' + 1);
		}

		int res = 0;

		for (int j = 0; j < wcnt; j++) {
			int k;

			for (k = 0; k < wlen; k++) {
				char cwc = wlst[j][k];
				vector <char> &cpd = pdat[k];
				int lb = 0, ub = cpd.size() - 1;

				while (ub - lb > 1) {
					int mb = ub + lb >> 1;

					if (cpd[mb] <= cwc) {
						lb = mb;
					} else {
						ub = mb;
					}
				}

				if (cpd[lb] != cwc) {
					break;
				}
			}

			if (k == wlen) {
				res++;
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
