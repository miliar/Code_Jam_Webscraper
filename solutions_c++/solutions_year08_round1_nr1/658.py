#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef int Capa;
typedef long long Cost;

const Cost INFTY = 1LL << 60;

Cost mincost(vector< vector<Capa> > &capa,
			 vector< vector<Cost> > &cost,
			 Capa req, int s, int t)
{
	Cost sum = 0;
	const Capa n = capa.size();

	vector<Cost> h(n, 0);
	vector<Cost> d(n);
	vector<int > p(n);
	vector<int > v(n);

	while(req > 0) {
		fill(d.begin(), d.end(), INFTY);
		fill(p.begin(), p.end(), -1);
		fill(v.begin(), v.end(), 0);

		d[s] = 0;
		p[s] = s;

		while(true) {
			int j = n;

			for(int i = 0; i < n; i++) {
				if(v[i] == 0 && (j == n || d[j] > d[i])) { j = i; }
			}

			if(j == n) { return INFTY; }
			if(j == t) { break; }

			v[j] = 1;

			for(int i = 0; i < n; i++) {
				if(capa[j][i] == 0) { continue; }
				if(v[i] != 0) { continue; }
				Cost e = d[j] + cost[j][i] + h[j] - h[i];
				if(d[i] > e) { d[i] = e; p[i] = j; }
			}
		}

		--req;

		for(int i = t; i != p[i]; i = p[i]) {
			sum += cost[p[i]][i];
			--capa[p[i]][i];
			++capa[i][p[i]];
		}

		for(int i = 0; i < n; i++)
			h[i] += d[i];
	}

	return sum;
}

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int n;
		cin >> n;

		vector<Cost> x(n);
		for(int i = 0; i < n; i++) { cin >> x[i]; }
		vector<Cost> y(n);
		for(int i = 0; i < n; i++) { cin >> y[i]; }

		int N = 2 * n + 2;
		int s = N - 2;
		int t = N - 1;

		vector< vector<Capa> > capa(N, vector<Capa>(N, 0));
		vector< vector<Cost> > cost(N, vector<Cost>(N, 0));

		Cost m = 1LL << 40;

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				capa[i+0][j+n] = 1;
				cost[i+0][j+n] = +( x[i] * y[j] + m );
				cost[j+n][i+0] = -( x[i] * y[j] + m );
			}
		}

		for(int i = 0; i < n; i++) {
			capa[s][i+0] = 1;
			capa[i+n][t] = 1;
		}

		cout << "Case #" << iCase << ": "
			 << mincost(capa, cost, n, s, t) - m * n << endl;
	}

	return 0;
}
