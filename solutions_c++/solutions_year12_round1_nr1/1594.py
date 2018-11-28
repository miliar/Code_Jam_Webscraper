#include <iostream>
#include <cfloat>
#include <cmath>
#include <cstdio>

using namespace std;

int main () {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		float p[7], va = 1.0, vb = 1.0, vc = 1.0;
		int A, B;
		cin >> A >> B;

		p[0] = B - A + 1;
		p[1] = p[0] + B + 1;

		p[2] = B - A + 3;
		p[3] = p[2] + B + 1;

		p[4] = B - A + 5;
		p[5] = p[4] + B + 1;

		p[6] = B + 2;

		for (int i = 0; i < A; i++) {
			float tmp;
			cin >> tmp;

			va *= tmp;
			if (i < A - 1)
				vb *= tmp;
			if (i < A - 2)
				vc *= tmp;
		}

//for (int i = 0; i < 7; i++) cout << p[i] << endl;

		float menor = p[0]*va + p[1]*(1-va);
		menor = p[2]*vb + p[3]*(1-vb) < menor ? p[2]*vb + p[3]*(1-vb) : menor;
		menor = p[4]*vc + p[5]*(1-vc) < menor ? p[4]*vc + p[5]*(1-vc) : menor;
		menor = p[6] < menor ? p[6] : menor;

		printf("Case #%d: %.6f\n", t, menor);
	}

	return 0;
}