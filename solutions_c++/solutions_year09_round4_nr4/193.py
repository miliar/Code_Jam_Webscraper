#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
double p[30][3];

double dis(double x1, double y1, double x2, double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}


int main()
{
	int tcse;
	double ans;
	int n;
	freopen("d2.in", "r", stdin);
	freopen("dout.txt", "w", stdout);
	scanf("%d", &tcse);
	for(int i = 1; i <= tcse; i++)
	{
		scanf("%d", &n);
		for(int k = 0; k < n; k++) 
			for(int j = 0; j < 3; j++) scanf("%lf", &p[k][j]);
		//printf("4545\n");
		if(n == 1) ans = p[0][2];
		else if( n == 2)
		{
			ans = p[0][2] > p[1][2] ? p[0][2] : p[1][2];
		}
		else if(n == 3)
		{
			ans = dis(p[0][0], p[0][1], p[1][0], p[1][1]);
			ans += p[0][2]+p[1][2];
			ans /= 2;
			double tmp;
			tmp = dis(p[0][0], p[0][1], p[2][0], p[2][1]);
			tmp += (p[0][2]+p[2][2]);
			tmp /= 2;
			ans = ans < tmp ? ans : tmp;
			
			
			tmp = dis(p[1][0], p[1][1], p[2][0], p[2][1]);
			tmp += (p[1][2]+p[2][2]);
			tmp /= 2;
			ans = ans < tmp ? ans : tmp;
			
		}
		printf("Case #%d: %.6lf\n", i, ans);
	}
	return 0;
}
