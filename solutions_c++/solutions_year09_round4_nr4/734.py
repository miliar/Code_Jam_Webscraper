//	Google Code Jam 2009
//	Round 2
//	D. Watering Plants

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
#include <cmath>

using namespace std;

FILE *inpf, *outf;

double px[50], py[50], pr[50];
int pcnt;

const double wpEps = 1e-8;

double pairRad(int pa, int pb) {
	double cdx = px[pa] - px[pb],
		cdy = py[pa] - py[pb],
		cdist = sqrt(cdx * cdx + cdy * cdy),
		minpr = min(pr[pa], pr[pb]),
		maxpr = max(pr[pa], pr[pb]);
	return max((cdist + minpr + maxpr) / 2, maxpr);
}

void doWork() {
	int ntc;
	fscanf(inpf, "%d\n", &ntc);

	for (int i = 1; i <= ntc; i++) {
		fscanf(inpf, "%d", &pcnt);

		for (int j = 0; j < pcnt; j++) {
			fscanf(inpf, "%lf %lf %lf", px + j, py + j, pr + j);
		}

		double res = 0;

		switch (pcnt) {
		case 1:
			res = pr[0];
			break;
		case 2:
			res = max(pr[0], pr[1]);
			break;
		case 3:
			res = max(pairRad(0, 1), pr[2]);
			res = min(res, max(pairRad(0, 2), pr[1]));
			res = min(res, max(pairRad(1, 2), pr[0]));
			break;
		}

		fprintf(outf, "Case #%d: %.8lf\n", i, res);
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
