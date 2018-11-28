#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int x[3];
int y[3];
int r[3];

double formula(int first, int second, int other)
{
	double dist;
	int dx = x[first] - x[second];
	int dy = y[first] - y[second];
	dist = sqrt(dx*dx + dy*dy);
	dist+=r[first];
	dist+=r[second];
	dist/=2;
	return max(dist, double(r[other]));
}

int main()
{
	FILE* input = fopen("input4.txt", "r");
	FILE* output = fopen("output4.txt", "w");
	int C;
	fscanf(input, "%d", &C);
	int i;
	for (i = 0; i < C; i++)
	{
		int n;
		fscanf(input, "%d", &n);
		if (n == 1)
		{
			int ans;
			fscanf(input, "%*d %*d %d", &ans);
			fprintf(output, "Case #%d: %d\n", i+1, ans);
		}
		if (n == 2)
		{
			int r1, r2;
			fscanf(input, "%*d %*d %d", &r1);
			fscanf(input, "%*d %*d %d", &r2);
			fprintf(output, "Case #%d: %d\n", i+1, max(r1, r2));
		}
		if (n == 3)
		{
			double mini;
			int j;
			for (j = 0; j < 3; j++)
				fscanf(input, "%d %d %d", &x[j], &y[j], &r[j]);
			mini = formula(0, 1, 2);
			mini = min(formula(1, 2, 0), mini);
			mini = min(formula(2, 0, 1), mini);
			fprintf(output, "Case #%d: %lf\n", i+1, mini);
		}
	}		
}