#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;
int test , i , j , n , m , k , l , x , y , xx , yy , ans;
int a[1001][1001] , b[1001][1001];
int main()
{
	freopen("c:/input.txt" , "r" , stdin);
	freopen("c:/output.txt" , "w" , stdout);
	cin>>test;
	for (int tt = 1; tt <= test; tt++)
	{
		cin>>n;
		for (i = 0; i < 1000; i++)
			for (j = 0; j < 1000; j++)
				a[i][j] = 0;

		for (l = 0; l < n; l++)
		{
			
			cin>>x>>y>>xx>>yy;
			for (i = x; i <= xx; i++)
				for (j = y; j <= yy; j++)
					a[i][j] = 1;
		}
		ans = 0;
		while (1)
		{
			int d = 0;
			for (i = 1; i < 300; i++)
				for (j = 1; j < 300; j++)
				{
					if (a[i][j-1] == 1 && a[i-1][j] == 1 && a[i][j] == 0)
						b[i][j] = 1;
					else
					if (a[i][j] == 1 && a[i-1][j] == 0 && a[i][j-1] == 0)
						b[i][j] = 0; 
					else
						b[i][j] = a[i][j];
						
						
				}

			for (i = 0; i < 300; i++)
				for (j = 0; j < 300; j++)
				{
					a[i][j] = b[i][j];
					if (a[i][j] == 1) d = 1;
				}

			ans++;
			if (!d) break;
		}

		cout<<"Case #"<<tt<<": "<<ans<<endl;;
	}
	return 0;
}