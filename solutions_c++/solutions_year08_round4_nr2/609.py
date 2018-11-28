#include <iostream>
using namespace std;

int main() {
	int C;
	cin >> C;
	for(int i = 1; i <= C; i++) {
		int N, M, A, b;
		bool fnd = false;
		cin >> N >> M >> A;
		for(int x1 = 1, y1 = 0; x1 <= N && !fnd; x1++) {
			for(int x2 = 0, y2 = 0; y2 <= M && !fnd; y2++) {
				for(int x3 = 1; x3 <= N && !fnd; x3++) {
					for(int y3 = 1; y3 <= M && !fnd; y3++) {
						int area = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1);
						if(area == A || area == -A) {
							fnd = true;
							cout << "Case #" << i << ": " << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
						}
					}
				}
			}
		}
		if(!fnd)
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
