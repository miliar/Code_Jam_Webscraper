#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1001;
double precalc[MAX];
int fact[MAX];

double match(int n, int k) {
	double ret = .0;
	double alt = -1;
	for(int i = 0; i <= n-k; ++i) {
		alt=-alt;
		ret+=alt/fact[i];
	}
	ret/=fact[k];
	return ret;
}

double cyclic(int n) {
	//cerr << "cyclic(" << n << ")" << endl;

	if(n <= 1) { return 0; }
	if(precalc[n]>0) { return precalc[n]; }
	double soln = .0;

	double m = match(n, 0);
	soln += m/(1-m);

	for(int i = 1; i <= n; ++i) {
		soln += match(n, i)/(1-m)*(cyclic(n-i)+1);
	}
	return (precalc[n]=soln);
}

int initcyclic() {
	for(int i = 0; i < MAX; ++i) {
		precalc[i] = -1;
	}
	return 0;
}

int initfact() {
	fact[0] = 1;
	int f = 1;
	for(int i = 1; i < MAX; ++i) {
		f*=i;
		fact[i]=f;
	}
}

int main(void) {
	initfact();
	initcyclic();

	int T;
	cin >> T;
	for(int t = 0; t < T; ++t) {
		double soln = .0;

		int N; cin >> N;
		vector<int> data;
		vector<int> done;
		for(int i = 0; i < N; ++i) {
			int tmp; cin >> tmp;
			data.push_back(tmp-1);
			done.push_back(0);
		}

		for(int i = 0; i < N; ++i) {
			if(done[i]) { continue; }
			int c = data[i];
			if(c == i) { done[i]=1; continue; }

			done[i]=1;
			int k = c;
			int n = 1;

			while(k != i) {
				++n;
				done[k]=1;
				k = data[k];
			}
			soln += cyclic(n);
		}

		printf("Case #%d: %.06lf\n", t+1, soln);
	}
}
