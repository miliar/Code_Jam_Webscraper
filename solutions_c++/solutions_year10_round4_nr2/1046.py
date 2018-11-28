#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
void print ( int kase ,  long long yes )
{
 	 cout <<"Case #"<<kase<<": ";
	 cout<<yes;
	 cout <<"\n";
 	 return ;
}
long long  price [11] [ 2000 ];
int P , M [ 2010 ], deg [2010];
typedef pair < int ,int > PII;
typedef pair < int , PII > PIII;
vector < PIII > Cost;
vector < PII > A;
int main ()
{
 	freopen ("B1.in","r",stdin);
 	freopen("B1.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- )
 	{
 		cin >> P; 
 		memset ( price , 0 ,sizeof ( price ) );
 		A.clear();
 		for ( int i = 0 ; i < (1<<P) ;i++ )  cin >> M [i] , deg [i] = P - M [i];
 		for ( int i = P , k = 0; i  >= 0 ;i-- , k++)
 		{
 			//cout << i/2 <<"\n";
 			for ( int j =0  ; j < (1<<(i-1))  ; j++  ) cin >> price [k][j];
 		}
 		//for ( int i = 0 ; i < P ;i++ ,cout<<"\n") for  ( int j =0  ; j < (1<<P) ; j++ ) cout << price [i][j] << " ";
 		for ( int i = 0 ; i < (1<<P)  ;i++ ) A.push_back (make_pair (M [i], i) );
 		sort (A.begin() , A.end() );
 		bool round [ 11 ] [ 2000 ] ;
 		memset ( round , false ,sizeof ( round ) );
 		//for ( int i = 0 ; i < A.size() ;i++ ) cout << A [i].first << " " << A [i].second<<"\n";
 		//bool visit [ 2000 ] ; memset(visit , false, sizeof ( visit ));
 		for ( int i = 0 ; i < A.size() ;i++ )
 		{
 			int t = A [i].second , d = P  - A [i].first;
 			//visit [ t ] = true;
 			int t1 = A[i].first;
 			//bool tmp_round [11][ 2000 ] ; memset ( tmp_round , false ,sizeof ( tmp_round) );
 			int a = t >> 1;
 			for ( int j = 0 ; j < P ;j++ ) 
 			{
 				if ( round [j][a] ) d--;
 				a >>= 1;
 			}	
 			while ( d > 0 )
 			{
 				d--;
 				int mini = 1<<29 ;
 				int k = t >> 1;
 				int l[2] = {-1,-1};
 				for ( int j = 0 ; j < P ;j++ )  
 				{
 					if (!round[j][k] &&mini >= price [j][k] )
 					{
 						mini = price [j][k]; 
 						l[1] = k; l[0] = j;
 					}
 					//cout << mini << " "<< t<< " " <<j << " "<< k <<"\n";
 					k >>=1;
 				}
 				if ( mini == (1<<29) ) break;
 				round [ l[0] ] [l[1]] = true;
 				/*for ( int j = i+1 ; j < A.size() ;j++ )
 				{
 					int t = A [i].second;
 					for ( int k = 0 ; k < P; k++ )*/
 			}
 			//for ( int j = 0 ; j < P ;j++ ) for ( int k = 0 ; k < (1<<P) ; k++ ) round [j][k] |= tmp_round [j][k];
 		}
 		long long ans = 0;
 		for ( int i = 0 ; i < P; i++ ) for ( int j = 0 ; j < (1<<P)  ;j++ ) if ( round [i][j] )  ans += price [i][j];
 		print(++kase ,ans );
 	}
 	return 0;
 }
 						
 			
