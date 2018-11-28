#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int nt;

int L, S, R, t, n;
int from[1001], to[1001], v[1001], order[1001];

bool cmp(int a, int b)
{
	return v[a] < v[b];
}

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d %d %d %d %d", &L, &S, &R, &t, &n);
		
		R -= S;
		
		for(int i = 0; i < n; i++)
		{
			scanf("%d %d %d", &from[i], &to[i], &v[i]);
			to[i] -= from[i];
			L -= to[i];
			order[i] = i;
			v[i] += S;
		}
		
		order[n] = n;
		to[n] = L;
		v[n] = S;
		n++;
		
		sort(order, order + n, cmp);
		
		double res = 0.0;
		double runleft = t;
		
		for(int i = 0; i < n; i++)
		{
			double dist = to[order[i]];
			double speed = v[order[i]];
			
			if (dist <= (R + speed) * runleft)
			{
				runleft -= dist / (R + speed);
				res += dist / (R + speed);
				dist = 0.0;
			}
			else
			{
				dist -= (R + speed) * runleft;
				res += runleft;				
				runleft = 0.0;
			}
			
			res += dist / speed;
		}
		
		printf("%.10lf\n", res);
		
	}
	
	return 0;
}