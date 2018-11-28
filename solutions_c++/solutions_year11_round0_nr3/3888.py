#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>

#define ll long long
using namespace std;

ll maxval;
ll rounds;
vector<ll> sean, sp, pat;
vector<ll> values, aux;

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T,N;
	scanf("%d", &T);

	for (int var = 1; var <= T; ++var) {
		scanf("%d", &N);

		ll xorall = 0,sumall =0;
		ll val;
		values.clear();
		sean.clear();
		aux.clear();
		sp.clear();
		pat.clear();
		maxval = 0;

		for (int r=0; r<N; ++r) {
			scanf("%lld", &val);
			values.push_back(val);
			xorall = xorall ^ val;
			sumall = sumall + val;
		}

		// Need to generate all distinct subsets
		rounds = 1;
		ll temp = values.front();
		sean.push_back(temp);
		sp.push_back(temp);
		aux.push_back(temp);

		if (temp == (xorall ^ temp))
			maxval = temp;

		ll loop;
		do {
			for (loop = 1; loop < pow(2,rounds); ++loop) {
				ll v = sean.at(loop - 1) + values.at(rounds);
				sean.push_back(v);
				ll t = aux.at(loop - 1);
				aux.push_back(values.at(rounds) ^ t);

				if ((t ^ values.at(rounds)) == (xorall ^ t ^ values.at(rounds))) {
					if (v != 0 && v != sumall) {
						if (v > maxval)
							maxval = v;
					}
				}

			}
			sean.push_back(values.at(rounds));
			aux.push_back(values[rounds]);

			if (values.at(rounds) == (xorall ^ values.at(rounds))) {
				if (values.at(rounds) > maxval)
					maxval = values.at(rounds);
			}

			rounds++;
		}while(rounds != N);

		if (maxval == 0)
			printf("Case #%d: NO\n", var);
		else
			printf("Case #%d: %lld\n", var, maxval);
	}
}
