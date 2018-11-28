#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int C;
int N;
int M;
int A;

int main() {
	fstream in;
	fstream out;
	in.open("prob2.in", fstream::in);
	out.open("prob2.out",fstream::out);

	in >> C;
	
	int area;
	int ans3,ans4,ans5,ans6;

	for (int a = 0; a < C; a++) {
		in >> N;
		in >> M;
		in >> A;
		bool done = false;

		for (int a1 = 0; a1 <= N; a1++) {
			for (int a2 = 0; a2 <= N; a2++) {
				for (int b1 = 0; b1 <= M; b1++) {
					for (int b2 = 0; b2 <= M; b2++) {
						area = a1 * b2 - b1 * a2;
						if (area < 0) {
							area = - area;
						}
						if (area == A) {
							done = true;
							ans3 = a1;
							ans4 = b1;
							ans5 = a2;
							ans6 = b2;
							break;
						}
					}
				}
			}
		}
		out << "Case #" << a + 1 << ": ";
		if (done) {
			out << "0 0 " << ans3 << " " << ans4 << " " << ans5 << " " << ans6 << endl;
		} else {
			out << "IMPOSSIBLE" << endl;
		}
	}
	
	in.close();
	out.close();
	return 0;
}