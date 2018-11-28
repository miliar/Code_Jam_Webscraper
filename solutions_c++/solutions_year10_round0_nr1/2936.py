#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;
int state [ 40 ];
void print ( int kase ,  bool yes )
{
 	 cout <<"Case #"<<kase<<": ";
	  if ( yes ) cout <<"ON";
	  else cout <<"OFF" ;
	  cout <<"\n";
 	 return ;
}
int main ()
{
 	freopen ("A-large1.in","r",stdin);
 	freopen("A-large2.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- )
 	{
	 	int N ,K ; cin >> N >> K;
	 	/*memset ( state , 0 ,sizeof ( state ) ); state [0] = 1;
	 	for ( int i = 0 ;  i< K ;i++ ) 
	 	{
		 	for ( int j = 0  ; j <= N ;j++ ) cout << state [j] << " " ; cout <<"\n";
		 	int tmp [40]; memset ( tmp , 0 ,sizeof ( tmp ) ) ; tmp [0] = 1;
 	        for ( int j = 1 ; j <= N ;j++ ) 
            {
			 	bool flag = true;
			 	for ( int k = 1 ; k < j ;k++ ) if ( state [k] == 0 ) flag = false;
			 	if ( flag ) tmp [j] = !state [j];
			 	else tmp [j] = state [j];
			}
			for ( int j = 0 ; j <= N ;j++ ) state [j] = tmp [j];
		}
		bool yes = true;
		for ( int j = 0  ; j <= N ;j++ ) cout << state [j] << " " ; cout <<"\n";
		for ( int i = 0 ; i <=N ;i++ ) if ( state [i] == 0 ) yes = false;
		
		print ( ++kase , yes);*/
		long long A = (1L<<N);
		if ( A < 0 ) cout << "asdsafsdfsgfsdggdgdfsdgfsdsfsdfsdfsdfssfssdsd\n";
		K %= A;
		bool yes = false;
		if ( K == A-1 ) yes = true;
		print (++kase , yes );
     }
     return 0;
}
