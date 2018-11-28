#include<iostream>
#include<algorithm>
#include<vector>
#include <functional>

using namespace std ;

int main()
{
	int temp , t , n ;

	freopen("1.txt" , "r" , stdin) ;
	freopen("2.txt" , "w" , stdout) ;

	cin >> t ;
	for(int tcase = 1 ; tcase <= t ; tcase++)
	{
		cin >> n ;
		vector<int> a , b ;
		for(int i = 0 ; i < n ; i++)
		{
			cin >> temp ;
			a.push_back(temp) ;
		}
		for(int i = 0 ; i < n ; i++)
		{
			cin >> temp ;
			b.push_back(temp) ;
		}

		sort(a.begin() , a.end()) ;
		sort(b.begin() , b.end() , greater<int> () ) ;

		int res = 0 ;
		for(int i = 0 ; i < n ; i++)
		{
			res += a[i] * b[i] ;
		}

		cout << "Case #" << tcase << ": " << res << "\n" ;
	}
}