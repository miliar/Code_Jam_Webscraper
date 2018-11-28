#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>

using namespace std;

int n, c;
int x[5];
int y[5], raio;
double r[5];
double res;

double dist(int a, int b)
{

	double res = sqrt((double)((x[a] - x[b])*(x[a] - x[b])+ (y[a] - y[b])*(y[a] - y[b])));

	//printf("res = %f\n", res);
	res = res + r[a] + r[b];

	return res/2;
}


int main()
{
	int testes;

	scanf("%d", &testes);

	for(int t = 1; t <= testes; t++)
	{
		scanf("%d", &n);

		for(int i = 0; i < n; i++)
		{
			scanf("%d %d %d", &x[i], &y[i], &raio);

			r[i] = raio;
			//printf("%d %d %lf\n", x[i], y[i], r[i]);
		}

		if(n == 1)
			printf("Case #%d: %.5f\n",t, r[0]);
		else if(n == 2)
		{
			res = max(r[0], r[1]);
			printf("Case #%d: %.5f\n",t, res);
		}
		else
		{
			res = max(dist(0,1), r[2]);
			res = min(res, max(dist(0,2), r[1]));
			res = min(res, max(dist(1,2), r[0]));
			printf("Case #%d: %.5f\n",t, res);
		}

	}

	return 0;
}
