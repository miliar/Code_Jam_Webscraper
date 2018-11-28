#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>

using namespace std ;

#define ALL(x) (x).begin(),(x).end()
#define ll long long

int main ()
{
	int N ;
	cin >> N ;
	for (int c = 1 ; c <= N ; c++)
	{
		int n , A , B , C , D , x0 , y0 , M ;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M ;
		vector <long long> x (n) , y (n) ;
		x[0] = x0 ;
		y[0] = y0 ;	
		int i ;
		long long ans = 0 ;
		for (i = 1 ; i <= n - 1 ; i++)
		{
			x[i] = (A * x[i - 1] + B ) % M ;
			y[i] = (C * y[i - 1] + D) % M ;
			//cout << endl << x[i] << " " <<y[i] << endl;
		}
		for (i = 0 ; i < n ; i++)
		{
			for (int j = 0 ; j < n ; j++)
			{
				for (int k = 0 ; k < n ; k++)
				{
					if (i == k || j == k || j == i)
						continue ;
					ll tx = (x[i] + x[j] + x [k]);
					ll ty = (y[i] + y[j] + y[k]);
					if (tx % 3 == 0 && ty % 3 == 0)
					{
						ans ++ ;
					}	
				}	
			}	
		}
		cout << "Case #" << c << ": " << (ans / 6) << endl;
	}
	return  0 ;	
}
