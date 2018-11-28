#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <stack>
#include <set>

using namespace std;

typedef unsigned long long ull;
typedef unsigned int uint;

const double eps = 1.e-8;

int main(int argc, char **argv)
{
	uint T;
	freopen("A-large.in", "rb", stdin);
	freopen("A-large.out", "wb", stdout);

	scanf("%u", &T);

	for(uint testNum = 0; testNum < T; testNum++)
	{
		uint X, S, R, N;
		double t;
		vector<double> B, E, w;
		double answer = 0;

		scanf("%u %u %u %lf %u", &X, &S, &R, &t, &N);
		B.resize(N);
		E.resize(N);
		w.resize(N);

		for(uint i = 0; i < N; i++)
		{
			scanf("%lf %lf %lf", &B[i], &E[i], &w[i]);
		}

		if(B[0] > eps)
		{
			E.insert(E.begin(), B[0]);
			B.insert(B.begin(), 0);
			w.insert(w.begin(), 0);
			N++;
		}
		for(uint i = 1; i < N; i++)
		{
			if(B[i] > E[i - 1] + eps)
			{
				E.insert(E.begin() + i, B[i]);
				B.insert(B.begin() + i, E[i - 1]);
				w.insert(w.begin() + i, 0);
				N++;
			}
		}
		if(E[N - 1] < X - eps)
		{
			B.push_back(E[N - 1]);
			E.push_back(X);
			w.push_back(0);
			N++;
		}

		vector< pair<uint, uint> > wsort(N);
		for(uint i = 0; i < N; i++)
		{
			w[i] += S;
			wsort[i].first = w[i];
			wsort[i].second = i;
		}
		
		R -= S;

		sort(wsort.begin(), wsort.end());

		for(uint i = 0; i < wsort.size() && t > eps; i++)
		{
			uint index = wsort[i].second;

			double tm = (E[index] - B[index]) / (R + wsort[i].first);
			if(tm > t + eps)
			{
				tm = t;
			}

			E[index] -= tm * R; 

			t -= tm;
		}

		for(uint i = 0; i < N; i++)
		{
			answer += (E[i] - B[i]) / (w[i]);
		}

		printf("Case #%u: %0.10lf\n", testNum + 1, answer);
	}

	fclose(stdin);
	fclose(stdout);
}