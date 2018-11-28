//	Google Code Jam 2009
//	Round 1B
//	A. Decision Tree

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
#include <string>
#include <set>

using namespace std;

FILE *inpf, *outf;

int tlc;
string tdsc;
char iln[10000];
vector <double> tnp;
vector <string> tfn;
vector <int> tlft, trgt;
int pti;
int anmCnt, ftrCnt;
set <string> ftrSet;

const char *digChs = "0123456789.";
const char *ftrChs = "abcdefghijklmnopqrstuvwxyz";

void parseTree() {
	pti = tdsc.find('(', pti);
	pti++;
	pti = tdsc.find_first_not_of(' ', pti);
	int nei = tdsc.find_first_not_of(digChs, pti);
	double np;
	sscanf(tdsc.substr(pti, nei - pti).c_str(), "%lf", &np);
	pti = tdsc.find_first_not_of(' ', nei);

	if (tdsc[pti] == ')') {
		tnp.push_back(np);
		tfn.push_back("");
		tlft.push_back(-1);
		trgt.push_back(-1);
		pti++;
		return;
	}

	int fei = tdsc.find_first_not_of(ftrChs, pti);
	int vni = tnp.size();
	tnp.push_back(np);
	tfn.push_back(tdsc.substr(pti, fei - pti));
	tlft.push_back(-1);
	trgt.push_back(-1);
	pti = fei;
	tlft[vni] = tnp.size();
	parseTree();
	trgt[vni] = tnp.size();
	parseTree();
	pti = tdsc.find(')', pti);
	pti++;
}

void doWork() {
	int ntc;
	fscanf(inpf, "%d\n", &ntc);

	for (int i = 1; i <= ntc; i++) {
		fscanf(inpf, "%d\n", &tlc);
		tdsc.clear();

		for (int j = 0; j < tlc; j++) {
			fgets(iln, sizeof iln, inpf);
			iln[strlen(iln) - 1] = '\0';
			tdsc += iln;
		}

		tnp.clear();
		tfn.clear();
		tlft.clear();
		trgt.clear();
		pti = 0;
		parseTree();
		fprintf(outf, "Case #%d:\n", i);
		fscanf(inpf, "%d\n", &anmCnt);

		for (int j = 0; j < anmCnt; j++) {
			fscanf(inpf, "%s %d", iln, &ftrCnt);
			ftrSet.clear();

			for (int k = 0; k < ftrCnt; k++) {
				fscanf(inpf, "%s", iln);
				ftrSet.insert(iln);
			}

			double res = 1;
			int tti = 0;

			for (;;) {
				res *= tnp[tti];

				if (!tfn[tti].size()) {
					break;
				}

				tti = ftrSet.count(tfn[tti]) ? tlft[tti] : trgt[tti];
			}

			fprintf(outf, "%.8f\n", res);
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
