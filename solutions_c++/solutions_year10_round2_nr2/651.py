//	Google Code Jam 2010
//	Round 1B
//	B. Picking Up Chicks

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

int nv, kv, bv, tv;
vector <pair <int, int> > cd;

void doWork() {
	int ntc;
	fscanf(inpf, "%d", &ntc);

	for (int i = 1; i <= ntc; i++) {
		fscanf(inpf, "%d%d%d%d", &nv, &kv, &bv, &tv);
		cd.resize(nv);

		for (int j = 0; j < nv; j++) {
			fscanf(inpf, "%d", &cd[j].first);
		}

		for (int j = 0; j < nv; j++) {
			fscanf(inpf, "%d", &cd[j].second);
		}

		sort(cd.begin(), cd.end());
		int usc = 0, ctsc = kv;

		for (int j = nv - 1; j >= 0 && ctsc; j--) {
			int cp = cd[j].first, cv = cd[j].second;

			if (bv - cp <= tv * cv) {
				// home
				ctsc--;
			} else {
				// loose
				usc += ctsc;
			}
		}

		if (ctsc) {
			fprintf(outf, "Case #%d: IMPOSSIBLE\n", i);
		} else {
			fprintf(outf, "Case #%d: %d\n", i, usc);
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
