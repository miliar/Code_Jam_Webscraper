#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int n;
int s;
int q;
int least[100][1000];
string engines[100];
string queries[1000];

int main() {
	fstream in;
	in.open("prob1.in", fstream::in);
	fstream out;
	out.open("prob1.out", fstream::out);

	in >> n;
	for (int a = 0; a < n; a++) {
		in >> dec >> s;
		char temp[100];
		in.getline(temp,100);
		for (int b = 0; b < s; b++) {
			in.getline(temp,100);
			engines[b] = temp;
		}

		in >> dec >> q;
		in.getline(temp,100);
		for (int c = 0; c < q; c++) {
			in.getline(temp,100);
			queries[c] = temp;
		}

		for (int i = 0; i < s; i++) {
			for (int j = 0; j < q; j++) {
				least[i][j] = q + 2;
			}
		}
		for (int k = 0; k < s; k++) {
			if (engines[k] != queries[0]) {
				least[k][0] = 0;
			}
		}
		for (int x = 1; x < q; x++) {
			for (int y = 0; y < s; y++) {
				if (engines[y] == queries[x]) {
					least[y][x] = q + 2;
				} else {
					int min = q + 2;
					for (int z = 0; z < s; z++) {
						if (z != y) {
							if (least[z][x-1] + 1 < min) {
								min = least[z][x-1] + 1;
							}
						} else {
							if (least[z][x-1] < min) {
								min = least[z][x-1];
							}
						}
					}
					least[y][x]=min;
				}
			}
		}
		int ans = q + 2;
		for (int t = 0; t < s; t++) {
			if (least[t][q - 1] < ans) {
				ans = least[t][q-1];
			}
		}
		out << "Case #" << a + 1 << ": " << ans << endl;
	}

	in.close();
	out.close();

	return 0;
}