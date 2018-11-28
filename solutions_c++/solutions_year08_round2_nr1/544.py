#include<algorithm>
#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<math.h>
#include<functional>

using namespace std ;

int main()
{
	long long int point[105][2] , t , n , A , B , C , D , x0 , y0 , M , x , y , i , j , k , res ;

	freopen("1.txt" , "r" , stdin) ;
	freopen("2.txt" , "w" , stdout) ;

	cin >> t ;
	for(int tcase = 1 ; tcase <= t ; tcase++)
	{
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >>M ;

		x = x0 ;
		y = y0 ;
		for(i = 0 ; i < n ; i++)
		{
			point[i][0] = x ;
			point[i][1] = y ;
			x = (A * x + B) % M ;
			y = (C * y + D) % M ;
		}

		res = 0 ;
		for(i = 0 ; i < n ; i++)
		{
			for(j = i + 1 ; j < n ; j++)
			{
				for(k = j + 1 ; k < n ; k++)
				{
					if(!((point[i][0] + point[j][0] + point[k][0]) % 3) && !((point[i][1] + point[j][1] + point[k][1]) % 3))
						res++ ;
				}
			}
		}

		cout << "Case #" << tcase << ": " << res << "\n" ;
	}
}