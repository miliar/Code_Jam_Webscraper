#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>

const double ZERO = 1e-10;

using namespace std;



int N,X,S,R,t;
int w[1000];
int B[1000];
int E[1000];
int order[1000];

int dcmp(double a, double b)
{
	if (fabs(a - b) < ZERO) return 0;
	else if (a - b > ZERO) return 1;
	else return -1;
}

bool cmp(int a, int b)
{
	return w[a] < w[b];
}

double Run()
{
	int total = B[0];
	for (int i = 1 ; i < N; ++i)
		total += B[i] - E[i - 1];
	total += X - E[N - 1];
	if (R * t <= total)
	{
		double needTime = t + (total - R * t) * 1.0 / S;
		for (int i = 0; i < N; ++i)
			needTime += (E[i] - B[i]) * 1.0 / (w[i] + S);
		return needTime;
	}
	double needTime = total * 1.0 / R;;
	double leftRunTime = t - needTime;

	for (int i = 0; i < N; ++i) order[i] = i;
	sort( order, order + N, cmp);

	for (int i = 0; i < N; ++i)
	{
		int now = order[i];
		if (dcmp(leftRunTime * (w[now] + R) , E[now] - B[now]) <= 0)
		{
			needTime += leftRunTime + (E[now] - B[now] - leftRunTime * (w[now] + R)) / (w[now] + S);
			for (int j = i + 1; j < N; ++j)
			{
				int cur = order[j];
				needTime += (E[cur] - B[cur]) * 1.0 / (w[cur] + S);
			}
			return needTime;
		}
		else
		{
			needTime += (E[now] - B[now]) * 1.0 / (w[now] + R);
			leftRunTime -= (E[now] - B[now]) * 1.0 / (w[now] + R);
		}

	}
	return needTime;

}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt" ,"w", stdout);

	int cases;
	scanf("%d" , &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d%d%d%d", &X,&S,&R,&t,&N);
		for (int i = 0; i < N; ++i) scanf("%d%d%d", B + i, E + i, w + i);

		double ans = Run();
		printf("Case #%d: %.8lf\n", ca , ans);
	}
}
