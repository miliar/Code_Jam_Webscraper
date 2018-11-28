#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

void usage(const int argc, const char *argv[]) {
    const char *progname = strrchr(argv[0], '/');
    progname = progname ? progname + 1 : argv[0];
    cerr << "Usage: " << progname << " inputfile" << endl;
    exit(2);
}

int flowdown(int p, int *alt, int H, int W) {
    int r = p / W;
    int c = p % W;
    int min = alt[p];
    int next = -1;
    if (r > 0 && alt[p - W] < min) {
	next = p - W;
	min = alt[p - W];
    }
    if (c > 0 && alt[p - 1] < min) {
	next = p - 1;
	min = alt[p - 1];
    }
    if (c < W - 1 && alt[p + 1] < min) {
	next = p + 1;
	min = alt[p + 1];
    }
    if (r < H - 1 && alt[p + W] < min) {
	next = p + W;
	min = alt[p + W];
    }
    return next;
}

int flowuplabel(int p, int *flow, int H, int W, char *lab, char label) {
    lab[p] = label;
    int labeled = 1;
    int r = p / W;
    int c = p % W;
    if (r > 0 && flow[p - W] == p) {
	labeled += flowuplabel(p - W, flow, H, W, lab, label);
    }
    if (c > 0 && flow[p - 1] == p) {
	labeled += flowuplabel(p - 1, flow, H, W, lab, label);
    }
    if (c < W - 1 && flow[p + 1] == p) {
	labeled += flowuplabel(p + 1, flow, H, W, lab, label);
    }
    if (r < H - 1 && flow[p + W] == p) {
	labeled += flowuplabel(p + W, flow, H, W, lab, label);
    }
    return labeled;
}

int main(const int argc, const char *argv[]) {
    if (argc != 2) {
	usage(argc, argv);
    }

    int T;

    ifstream inputfile(argv[1], ifstream::in);
    if (inputfile.is_open()) {
	inputfile >> T;
	for (int t = 1; t <= T; t++) {
	    int H;
	    int W;
	    inputfile >> H >> W;
	    int alt[H * W];
	    for (int r = 0; r < H; r++) {
		for (int c = 0; c < W; c++) {
		    inputfile >> alt[r * W + c];
		}
	    }

	    int flow[H * W];
	    for (int p = 0; p < H * W; p++) {
		flow[p] = flowdown(p, alt, H, W);
	    }

	    char lab[H * W];
	    memset(lab, 0, sizeof(char) * H * W);
	    int tolabel = H * W;
	    char label = 'a';
	    int nextunlabeled = 0;
	    while (tolabel > 0) {
		while (lab[nextunlabeled]) {
		    nextunlabeled++;
		}
		int p = nextunlabeled;
		while(flow[p] >= 0) {
		    p = flow[p];
		}
		tolabel -= flowuplabel(p, flow, H, W, lab, label);
		label++;
	    }

	    cout << "Case #" << t << ": " << endl;
	    for (int r = 0; r < H; r++) {
		cout << lab[r * W];
		for (int c = 1; c < W; c++) {
		    cout << " " << lab[r * W + c];
		}
		cout << endl;
	    }
	}
    }
    inputfile.close();
}
