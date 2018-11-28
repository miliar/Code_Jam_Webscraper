#include <cstdio>
#include <cstring>

using namespace std;

int t;
char f[105][105];
double wp[105], owp[105], oowp[105];
int n;


void init()
{
	scanf("%d\n", &n);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			scanf("%c", &f[i][j]);
		scanf("\n");
	}
}

void work()
{
	double sum, sumt;
	double total = 0;
	for (int i = 1; i <= n; i++)
	{
		sum = 0;
		total = 0;
		for (int j = 1; j <= n; j++)
		{
			if (f[i][j] == '1')
				sum++;
			if (f[i][j] != '.')
				total++;
		}
		wp[i] = sum / total;
	}

	for (int i = 1; i <= n; i++)
	{
		sumt = 0;
		for (int j = 1; j <= n; j++)
		{
			if (f[ i ][ j ] == '.')
				continue;
			sum = 0;
			total = 0;
			for (int k = 1; k <= n; k++)
			{
				if (k == i)
					continue;
				if (f[j][k] == '1')
					sum++;
				if (f [j][k] != '.')
					total++;
			}
			sumt += sum /  total;
		}

		total = 0;
		for(int j = 1; j <= n; j++)
			if (f[i][j] != '.')
				total++;
		owp[i] = sumt / total;
	}

	for (int i = 1; i <= n; i++)
	{
		sum = 0;
		total = 0;
		for(int j = 1; j <= n; j++)
		{
			if (f[i][j] != '.')
			{
				sum += owp[j];
				total++;
			}
		}
		oowp[i] = sum / total;
	}
	
	for (int i = 1; i <= n; i++)
		printf("%.10lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	return;
}
  


int main()
{
	freopen("A-large.in" ,"r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		init();
		work();
	}
	return 0;
}
