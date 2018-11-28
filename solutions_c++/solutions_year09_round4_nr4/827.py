#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std ;

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out.txt", "w", stdout);
	int T;
	int kase;
	double ans;
	int n, k;
	int plant[45][3];
	
	
	cin >> T;
	for(kase = 1; kase <= T; kase ++)
	{
		cin >> n;
		int i;
		for(i = 0; i < n; i ++)
		{
			cin >> plant[i][0] >> plant[i][1] >> plant[i][2];	
		}
		
		ans = 9999999;
		if(n == 1)
		{
			ans = plant[0][2];	
		}
		else if(n ==2)
		{
			ans = max(plant[0][2], plant[1][2]);	
		}
		else
		{
			double r1, r2;
			
			r1 = plant[0][2];
			r2 = sqrt((double)(plant[1][0] - plant[2][0])*(plant[1][0] - plant[2][0]) +
						(plant[1][1] - plant[2][1])*(plant[1][1] - plant[2][1]));
			r2 = (r2 + plant[1][2] + plant[2][2]) / 2.0;
			
			ans = min(ans, max(r1, r2));
			
			r1 = plant[1][2];
			r2 = sqrt((double)(plant[0][0] - plant[2][0])*(plant[0][0] - plant[2][0]) +
						(plant[0][1] - plant[2][1])*(plant[0][1] - plant[2][1]));
			r2 = (r2 + plant[0][2] + plant[2][2]) / 2.0;
			
			ans = min(ans, max(r1, r2));
			
			r1 = plant[2][2];
			r2 = sqrt((double)(plant[1][0] - plant[0][0])*(plant[1][0] - plant[0][0]) +
						(plant[1][1] - plant[0][1])*(plant[1][1] - plant[0][1]));
			r2 = (r2 + plant[1][2] + plant[0][2]) / 2.0;
			
			ans = min(ans, max(r1, r2));		
		}

	
		cout << "Case #" << kase << ": " << ans << endl;
	}
    return 0;
}


