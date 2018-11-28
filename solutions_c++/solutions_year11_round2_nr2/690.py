#include<cstdio>
#include<cstdlib>
#include<cmath>

int P[201], V[201];
int C, D;

bool check(double time)
{
	int i;
	double Lstart, Lend;
	double Rstart, Rend;
	double pre;
	pre = -1e9;
	for(i = 0; i < C; i ++)
	{
		if((V[i]-1)*D/2.0 > time)return false;
		Lstart = P[i] - time;
		Lend = Lstart + (V[i]-1)*D;
		
		Rend = P[i] + time;
		Rstart = Rend - (V[i]-1)*D;
		
		if(Lstart > pre)
		{
			pre = Lend+D;
		}
		else if(pre > Rstart)
		{
			return false;
		}
		else {
			pre = pre + V[i]*D;
		}
	}
	return true;
}

int main()
{
	int cas, T;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int i, j, k;
		
		scanf("%d %d", &C, &D);
		
		for(i = 0; i < C; i ++)
		{
			scanf("%d %d", &P[i], &V[i]);
		}
		
		double left, right, mid;
		left = 0; right = 1e10;
		while(fabs(left-right)>1e-8)
		{
			mid = (left+right)/2.0;
			if(check(mid))
			{
				right = mid;
			}
			else {
				left = mid;
			}
		}
		
		printf("Case #%d: %.8lf\n", cas, left);
		
	}
	return 0;
} 
