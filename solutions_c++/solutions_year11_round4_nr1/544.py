#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

int w[1001];
int R, S, N;
long B[1001], E[100l], L[1001];
long X, t;

int main()
{

	int ncase;
	scanf("%d", &ncase);

	for(int caseidx = 1; caseidx <= ncase; caseidx++){
		scanf("%ld %d %d %ld %d", &X, &S, &R, &t, &N);

		for(int i = 0; i < N; i++){
			scanf("%ld %ld %d", &B[i], &E[i], &w[i]);
			L[i] = E[i] - B[i];
		}

		double ret = 0;

		long tX = X;
		for(int i = 0; i < N; i++){
			ret += (double(L[i]) / double(S + w[i]));
			tX -= L[i];
		}
		ret += (double(tX) / double(S));

		L[N] = tX;
		w[N] = 0;

		N++;

		vector<pair<double, double> >v;

		for(int i = 0; i < N; i++){
			pair<double, double> P(double(R - S) / double(S + w[i]), double(L[i]) / double(R + w[i]));

			v.push_back(P);
		}
		sort(v.begin(), v.end());

		double tt = t;
		int pos = N - 1;
		while(tt > 0 && pos >= 0){

			//cout << v[pos].first << endl;

			double dect = MIN(tt, v[pos].second);
			tt -= dect;
			ret -= (dect * v[pos].first);

			pos--;
		}

		printf("Case #%d: %lf\n", caseidx, ret);
	}
	
	return 0;
}

// vi: ts=2 sw=2
