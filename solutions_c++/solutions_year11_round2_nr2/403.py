#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

int p[256], v[256];
vector<double> P;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d:", t);
		int d, c, sf = 0;
		scanf("%d%d", &c, &d);
		P.clear();
		for(int i = 0; i < c; i++)
		{
			scanf("%d%d", &p[i], &v[i]);
			for(int j = 0; j < v[i]; j++)
				P.push_back(p[i]);
			sf += v[i];
		}
		double ini = 0, fim = 1000000000000000000;
		for(int i = 0; i < 300; i++)
		{
			int ok = 1;
			double meio = (ini+fim)/2;
			vector<double> C = P;
			C[0] -= meio;
			for(int j = 1; j < C.size(); j++)
			{
				double start = C[j];
				C[j] = C[j-1] + d;
				if(fabs(start - C[j]) > meio)
				{
					if(C[j] > start) { ok = 0; break; }
					else C[j] = start-meio;
				}
			}
			if(ok) fim = meio;
			else ini = meio;
		}
		printf(" %.9lf\n", ini);
	}
	return 0;
}
