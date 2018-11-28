#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int XX[111];

int main() {

	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		double time = 0.0;
		double Rt;
		int X, S, R, N;
		
		cin >> X >> S >> R >> Rt >> N;
		
		for (int i = 0; i <= 100; ++i)
			XX[i] = 0;

		for (int i = 0; i < N; ++i) {
			int b, e, w;
			cin >> b >> e >> w;

			for (int j = b; j < e; ++j)
				XX[j] = w;
		}

		sort(XX, XX+X);

		if (R <= S) Rt = 0;
	
		for (int i = 0; i < X; ++i) {
			int speed = (Rt > 0.0) ? R : S;
			speed += XX[i];
			double _t = 1.0 / speed;

			if (Rt > 0.0 && _t > Rt) {
				_t = Rt + (1.0 - Rt * speed) / (S + XX[i]);
				Rt = -0.0;
			}

			time += _t;
			Rt -= _t;

			//cout << _t << " ";
		}
		//cout << endl;

		printf("Case #%d: %0.6f\n", t, time);
	}

}


