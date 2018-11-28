#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
using namespace std ;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int T, N;
	int kase;
	double ans;

	double mars[505][6];
	double x, y, z;
	double vx, vy, vz;
	scanf("%d", &T);
	for(kase = 1; kase <= T; kase ++)
	{
		scanf("%d", &N);
		int i;
		x = 0; y = 0; z = 0;
		vx = 0; vy = 0; vz = 0;
		for(i = 0; i < N; i ++)
		{
			scanf("%lf%lf%lf%lf%lf%lf", 
					&mars[i][0], &mars[i][1], &mars[i][2],
					&mars[i][3], &mars[i][4], &mars[i][5]);
				 
			x += mars[i][0];
			y += mars[i][1];
			z += mars[i][2];
			vx += mars[i][3];
			vy += mars[i][4];
			vz += mars[i][5];
		}
		x /= N;
		y /= N;
		z /= N;
		vx /= N;
		vy /= N;
		vz /= N;
		
//		printf("%.3lf %.3lf %.3lf %.3lf %.3lf %.3lf\n", x, y , z , vx, vy, vz);
		
		
		double a, b, c;
		a = vx * vx + vy * vy + vz * vz;
		b = 2 * (vx * x + vy * y + vz * z);
		c = x * x + y * y + z * z;
		
//		cout << a << " " << b << "	" << c << endl;
		double t ;
		if(fabs(a) < 1e-9)
		{
			if(fabs(b) < 1e-9)
				t = 0;
			else t = -1 * c / b ;				
		}
		else
		{
			t = -1 * b / a / 2;	
		}
		
		if(t < 0)	t = 0;
		
		x += vx * t;
		y += vy * t;
		z += vz * t;
		
		ans = sqrt(x * x + y * y + z * z);
		
		printf("Case #%d: %.8lf %.8lf\n", kase, ans, t);
	}
    return 0;
}


/*
Input 
 
   
3
3
3 0 -4 0 0 3
-3 -2 -1 3 0 0
-3 -1 2 0 3 0
3
-5 0 0 1 0 0
-7 0 0 1 0 0
-6 3 0 1 0 0
4
1 2 3 1 2 3
3 2 1 3 2 1
1 0 0 0 0 -1
0 10 0 0 -10 -1

   
Output

Case #1: 0.00000000 1.00000000
Case #2: 1.00000000 6.00000000
Case #3: 3.36340601 1.00000000

 

 


*/
