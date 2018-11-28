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
vector < string > grid;
void print ( int kase ,  int yes )
{
 	 cout <<"Case #"<<kase<<": ";
	  if ( yes == -1 ) cout <<"Neither";
	  else if ( yes == 0 ) cout <<"Blue";
	  else if ( yes == 1 ) cout <<"Red";
	  else if ( yes == 2 ) cout <<"Both";
	  cout <<"\n";
 	 return ;
}
void rotate(int N)
{
 	 vector <string > tmp  = grid;
 	 for ( int i = N-1 , k = 0; i >= 0 ;i-- ,k++) for ( int j = 0 , l = 0; j < N ;j++ ,l++)
 	 {
	  	 tmp [l][k] = grid [i][j];
      }
      grid = tmp;
      return ;
}
void gravity ( int N )
{
 	 //cout<<"\n";for ( int i = 0 ; i < N ;i++ ,cout <<"\n") for  (int j = 0 ; j < N ;j++ ) cout << grid [i][j] << "" ;cout<<"\n\n";
 	 bool flag = true;
 	 while ( flag )
 	 {
	  	   flag = false;
	  	  for ( int i = 0 ; i < N ;i++ ) for ( int j = 0 ; j < N ;j++ ) if ( i+1 < N && grid [i][j] != '.' && grid [i+1][j] == '.' ) 
		  {
		   	   swap ( grid [i+1][j] ,  grid [i][j] );
				  flag = true;
				  break;
		  } 
	  }
	 // cout<<"\n";for ( int i = 0 ; i < N ;i++ ,cout <<"\n") for  (int j = 0 ; j < N ;j++ ) cout << grid [i][j] << "" ;
	  return ;
}
bool chk(char a , int N, int K)
{
 	 int cnt = 0;
 	 for ( int i = 0 ; i < N ; i++ ) for ( int j = 0 ; j < N ; j++ ) if ( grid [i][j] == a )
 	 {
	  	 bool found = true;
	  	 int t = 0 ;
	  	 for ( int k = j ; k < N ; k++ ) if ( grid [i][k] != a ) break; else t++;
	  	 //cout <<t << " " <<K<<" "<<"row\n";
	  	 if ( t >= K ) return true;
	  	 t = 0;
	  	 for ( int k = i ; k < N ; k++ ) if ( grid [k][j] != a ) break; else t++;
	  	 //cout <<t << " " <<K<<" "<<"col\n";
	  	 if ( t >= K ) return true; t = 0;
	  	 for ( int k = i ; k < N && k-i+j < N; k++ ) if ( grid [k][k-i+j] != a ) break; else t++;
	  	 
	  	 if ( t >= K ) return true; t = 0;
	  	 for ( int k = i ; k < N && j-(k-i) >=0; k++ ) if ( grid [k][j - (k-i)] != a ) break; else t++;
	  	 if ( t >= K )return true; t = 0;
     }
     return false;
}
int main ()
{
 	freopen ("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- )
 	{
	 	int N ,K ; cin >> N >> K;
	 	grid.clear();
	 	for ( int i = 0 ; i < N ;i++ )
	 	{
		 	string a ; cin >> a;
		 	grid.push_back(a);
		}
		rotate(N);
		gravity(N);
		int val = -1;
		if ( chk ( 'B' ,N,K) ) val += 1;
		if ( chk ('R' , N ,K ) )val += 2;
		print (++kase , val );
    }
    return 0;
}
	 	
