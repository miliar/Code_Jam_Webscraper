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
int N , arr [ 110 ],D,I,M;
int memo [310][110];
int recurse ( int num , int pos )
{
 	if ( pos >= N ) return 0;
 	//if ( num > 255 ) return 1<<29;
 	if ( memo [num][pos] != -1 ) return memo [ num ] [pos];
 	//if ( num > 255 && num < 1000 ) return 1<<29;
 	//if ( num < -255 ) return 1<<29;
 	//cout << num << " "<< pos <<"\n";
 	int &ret = memo [num][pos];
 	ret = 1<<29;
 	//memo [num][pos] = ret;
 	if (  num <= 255 && abs (arr [pos] - num) <= M ) ret = min ( ret , recurse( arr[pos] , pos+1 ) );  
 	else
 	{
	 	 if ( num >= 300 ) ret = min ( ret , recurse( arr[pos] , pos+1 ) );  
 		 //else 
 		 //{
	 	 if ( M > 0 ) 
	     {
		   	 /*int diff = abs ( arr [pos] - num );
	 		 int cnt = diff/M;
	 		 if ( diff%M == 0 ) cnt--;*/
	 		 	if ( num <= 255 ) for ( int i = -M ; i <= M ;i++ ) if ( num + i >= 0 ) ret = min ( ret ,recurse (num+i,pos)+I ) ;
 		 }
		 for ( int i = 0 ; i <= 255 ;i++ ) if ( (abs (num -i) <= M && num  <=  255) || num >= 300 ) ret = min ( ret ,recurse (i,pos+1)+abs(arr[pos]  -i) ) ;
	 	 ret = min ( ret , recurse (num,pos+1) + D );
	 //}
	 //cout << num << " "<< pos << " " << ret <<"\n";
	 }
	 return ret;//memo[num][pos] = ret;
}	 	 
void print ( int kase ,  int yes )
{
 	 cout <<"Case #"<<kase<<": ";
	  cout<<yes;
	  cout <<"\n";
 	 return ;
}
int main ()
{
 	freopen ("B-3.in","r",stdin);
 	freopen("B-3.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- )
 	{
	 	cin >> D>>I>>M>>N;
	 	for ( int i = 0 ; i < N ;i++ ) cin >> arr [i];
	 	memset ( memo , -1 ,sizeof ( memo ) ) ;
	 	int ans = recurse ( 300 , 0 );
	 	print(++kase , ans );
    }
    return 0;
}
