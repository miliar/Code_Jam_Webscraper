#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<algorithm>
using namespace std;

int csK, csN, N, X[4], Y[4], R[4];

inline double dist(int x1, int y1, int x2, int y2)
{
	return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}

int main()
{
	int i, j, k, m, t;
	double r1, r2, r3;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d", &N);
		for(i = 0; i < N; ++i)
			scanf("%d %d %d", &X[i], &Y[i], &R[i]);
		if(N == 1)
			printf("Case #%d: %d\n", csK, R[0]);
		else if(N == 2)
			printf("Case #%d: %d\n", csK, max(R[0], R[1]));
		else if(N == 3)
		{
			r1 = (dist(X[0], Y[0], X[1], Y[1])+R[0]+R[1]) / 2;
			r2 = (dist(X[0], Y[0], X[2], Y[2])+R[0]+R[2]) / 2;
			r3 = (dist(X[2], Y[2], X[1], Y[1])+R[2]+R[1]) / 2;
			if(R[2] > r1) r1 = R[2];
			if(R[1] > r2) r2 = R[1];
			if(R[0] > r3) r3 = R[0];
			if(r2 < r1) r1 = r2;
			if(r3 < r1) r1 = r3;
			printf("Case #%d: %lf\n", csK, r1);
		}

	}
}

