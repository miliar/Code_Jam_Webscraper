// Name        : DancingWithGooglers.cpp
// Author      : Pavan Kumar Sunkara
// Version     :
// Copyright   : MIT/X11


#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv) {
	int t, n, s, p, g, i, j, k, max, min;
	ifstream in;

	in.open(argv[1], ifstream::in);

	if (in.is_open()) {
		in >> t;
		for (i=0; i<t; i++) {
			g = 0;
			in >> n >> s >> p;
			max = (p-1)*3+1;
			min = (p-1)*3-1;

			for (j=0; j<n; j++) {
				in >> k;
				if (k >= max) {
					g++;
				} else if (k < max && k >= min && k > 0) {
					if (s > 0) {
						g++;
						s--;
					}
				}
			}

			cout << "Case #" << i+1 << ": " << g << endl;
		}

		in.close();
	} else {
		cout << "Error opening file" << endl;
	}

	return 0;
}
