#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

double p[10], e[10];

int main ()
{
	int T, A, B;
	int i, j, k;
	double ans, temp;
	
	scanf("%d", &T);
	
	for (i=1; i<=T; i++)
	{
		scanf("%d", &A);
		scanf("%d", &B);
		
		B -= A;
		
		for (j=0; j<A; j++)
			scanf("%lf", &p[j]);
		
		ans = 100000000000000.0;
		
		if (A == 3)
		{
			e[0] = p[0] * p[1] * p[2];
			e[1] = p[0] * p[1] * (1 - p[2]);
			e[2] = p[0] * p[2] * (1 - p[1]);
			e[3] = p[2] * p[1] * (1 - p[0]);
			e[4] = (1 - p[0]) * p[2] * (1 - p[1]);
			e[5] = (1 - p[0]) * p[1] * (1 - p[2]);
			e[6] = (1 - p[2]) * p[0] * (1 - p[1]);
			e[7] = (1 - p[0]) * (1 - p[2]) * (1 - p[1]);
			
			temp = e[0] * (B + 1) + (e[1]+e[2]+e[3]+e[4]+e[5]+e[6]+e[7])*(2*B+5);
			ans = min(ans, temp);
			
			temp = (e[0]+e[1])*(B+3) + (e[2]+e[3]+e[4]+e[5]+e[6]+e[7])*(2*B+7);
			ans = min(ans, temp);
			
			temp = (e[0]+e[1]+e[2]+e[6])*(B+5) + (e[3]+e[4]+e[5]+e[7])*(2*B+9);
			ans = min(ans, temp);
			
			ans = min(ans, double(B+5));
		}
		
		else if (A == 1)
		{
			e[0] = p[0];
			e[1] = 1 - p[0];
			
			temp = (B+1)*e[0] + e[1]*(2*B+3);
			ans = min(ans, temp);
			ans = min(ans, double(B+3));
		}
		
		else if (A == 2)
		{
			e[0] = p[0] * p[1];
			e[1] = p[0] * (1 - p[1]);
			e[2] = (1 - p[0]) * p[1];
			e[3] = (1 - p[0]) * (1 - p[1]);
			
			temp = e[0] * (B + 1) + (2*B+4) * (e[1] + e[2] + e[3]);
			ans = min(ans, temp);
			
			temp = (e[2] + e[3]) * (2*B + 6) + (B+3) * (e[1] + e[0]);
			ans = min(ans, temp);
			
			ans = min(ans, double(B+4));
		}
		
		printf("Case #%d: %lf\n", i, ans);
	}
	
	return 0;
}
