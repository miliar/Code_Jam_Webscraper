#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cassert>
using namespace std;
#define sz(A) ((int)A.size())
typedef long long LL;
typedef pair < LL , LL > PI;
int main () {
	int t , n ;
	cin >> t;
	for ( int kase = 1 ; kase <= t ; kase ++ ) {
		cout <<"Case #" << kase << ": " ;
		/*
		 *first = x0, second = y0
print first, second
for i = 1 to n-1
  first = (A * first + B) mod M
  second = (C * second + D) mod M
  print first, second

		 */
		LL A , B , C , D , x0 , y0 , M;
		vector < PI > V;
		cin >> n;
		V.resize(n);
		cin >> A >> B >> C >> D >> x0 >> y0 >> M;
		V[0].first = x0 , V[0].second = y0;
		LL x,y;
		x=x0 , y = y0;
		for ( int i=1;i<=n-1;i++ ) {
			x = (A*x + B)%M;
			y = (C*y + D)%M;
			V[i].first=x;
			V[i].second=y;
		}
		int cnt = 0;
		for ( int i=0;i<n;i++ )
			for ( int j=i+1;j<n;j++ ) 
				for ( int k=j+1;k<n;k++ ){
					if ((( V[i].first + V[j].first + V[k].first ) % 3 == 0 )&& 
						( V[i].second + V[j].second + V[k].second )%3 == 0 ) cnt ++;
				}
	cout << cnt << endl;
	}
	return 0;
}
