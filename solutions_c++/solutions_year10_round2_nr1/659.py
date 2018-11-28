//	Google Code Jam 2010
//	Round 1B
//	A. File Fix-it

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

struct DirNode;
typedef DirNode *PtrDirNode;

struct DirNode {
	string dnName;
	vector <string> dnChNms;
	vector <PtrDirNode> dnChPts;
};

DirNode dnRoot;
char inpBuf[250];
string cip, cdrnm;
int cipl;

long long insPath(int ci, DirNode *cdrnd) {
	if (ci == cipl) {
		return 0;
	}

	int ni = cip.find('/', ci + 1);
	cdrnm = cip.substr(ci + 1, ni - ci - 1);
	int j, jl = cdrnd->dnChNms.size();

	for (j = 0; j < jl && cdrnd->dnChNms[j] != cdrnm; j++);

	if (j < jl) {
		return insPath(ni, cdrnd->dnChPts[j]);
	}

	PtrDirNode ndrnd = new DirNode;
	ndrnd->dnName = cdrnm;
	cdrnd->dnChNms.push_back(cdrnm);
	cdrnd->dnChPts.push_back(ndrnd);
	return 1 + insPath(ni, ndrnd);
}

void delTree(DirNode *cdrnd) {
	if (!cdrnd) {
		return;
	}

	int j, jl = cdrnd->dnChPts.size();

	for (j = 0; j < jl; j++) {
		delTree(cdrnd->dnChPts[j]);
		delete cdrnd->dnChPts[j];
	}

	cdrnd->dnChNms.clear();
	cdrnd->dnChPts.clear();
}

void doWork() {
	int ntc;
	fscanf(inpf, "%d", &ntc);

	for (int i = 1; i <= ntc; i++) {
		int epc, npc;
		fscanf(inpf, "%d%d", &epc, &npc);

		for (int j = 0; j < epc; j++) {
			fscanf(inpf, "%s", inpBuf);
			cip = inpBuf;
			cipl = cip.size();
			cip += '/';
			insPath(0, &dnRoot);
		}

		long long res = 0;

		for (int j = 0; j < npc; j++) {
			fscanf(inpf, "%s", inpBuf);
			cip = inpBuf;
			cipl = cip.size();
			cip += '/';
			res += insPath(0, &dnRoot);
		}

		fprintf(outf, "Case #%d: %lld\n", i, res);
		delTree(&dnRoot);
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
