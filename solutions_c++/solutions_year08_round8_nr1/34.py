#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <stdarg.h>
#include <cassert>

void dbg(char * fmt, ...)
{
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(fmt);
}

double mat[10][10];

void solve(int test_case)
{
	double x1,x2,x3,y1,y2,y3;
	scanf("%lf%lf%lf%lf%lf%lf", &x1, &y1, &x2, &y2, &x3, &y3);
	mat[0][0] = x2-x1;
	mat[0][1] = x3-x1;
	mat[0][2] = -1;
	mat[0][3] = 0;
	mat[0][4] = x1;
	mat[1][0] = y2-y1;
	mat[1][1] = y3-y1;
	mat[1][2] = 0;
	mat[1][3] = -1;
	mat[1][4] = y1;
	

	scanf("%lf%lf%lf%lf%lf%lf", &x1, &y1, &x2, &y2, &x3, &y3);
	mat[2][0] = x2-x1;
	mat[2][1] = x3-x1;
	mat[2][2] = -1;
	mat[2][3] = 0;
	mat[2][4] = x1;
	mat[3][0] = y2-y1;
	mat[3][1] = y3-y1;
	mat[3][2] = 0;
	mat[3][3] = -1;
	mat[3][4] = y1;
	
	for(int i = 0; i < 4; i++)
	{


		if (mat[i][i] == 0)
			for(int j = i+1; j <= 4; j++)
			{
				assert(j < 4);
				if (mat[j][i] != 0)
				{
					for(int k = 0; k < 5; k++)
					{
						double temp = mat[j][k];
						mat[j][k] = mat[i][k];
						mat[i][k] = temp;
					}
					break;
				}
			}
		/*for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 5; k++)
				dbg("%.8lf ", mat[j][k]);
			dbg("\n");
		}
		dbg("\n");*/
		
		for(int j = 0; j < 4; j++)
		{
			if (j != i)
			{
				for(int k = 0; k < 5; k++)
				{
					if (k != i)
						mat[j][k] -= mat[i][k] * mat[j][i] / mat[i][i]; 
				}
				mat[j][i] = 0;
			}
		}
		
	}
	printf("Case #%d: %.10lf %.10lf\n", test_case, -mat[2][4]/mat[2][2], -mat[3][4]/mat[3][3]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);
	return 0;
}
