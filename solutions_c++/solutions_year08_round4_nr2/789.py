#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	int C;
	cin >> C;
	for(int nacho = 1; nacho <= C; nacho++) {
		int N, M, A;
		cin >> N >> M >> A;
		double area2 = 1.0*A/2.0;
		int x1, y1, x2, y2, x3, y3;
		x1 = y1 = 0;
		bool encontrado = false;
		for(x2 = 0; x2 <= N && !encontrado; x2++)
		for(y2 = 0; y2 <= M && !encontrado; y2++)
		for(x3 = 0; x3 <= N && !encontrado; x3++)
		for(y3 = 0; y3 <= M && !encontrado; y3++) {
			double a = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
			double b = sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3));
			double c = sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
			double p = a+b+c;
			p = p/2.0;
			double area1 = sqrt(p*(p-a)*(p-b)*(p-c));
			if(fabs(area1-area2) < 1e-7) {
				encontrado = true;
			}
		}
		cout << "Case #" << nacho << ": ";
		if(!encontrado)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << x1 << " " << y1 << " " << --x2 << " " << --y2 << " " << --x3 << " " << --y3 << endl;
	}

	return 0;
}
