#include<iostream>
#include<cmath>
#include<algorithm>
#include<cctype>
#include<vector>
#include<cassert>
#include<set>
#include<string>
#include<ctime>
#include<map>
using namespace std;
int best_performance [2000];
int best_normal [2000] ;
int dp[200][200] ;
int n ;
int score[200];
int lb ;
int nCritical;
int f ( int index , int remain ){
	if ( remain < 0 ) return -100000 ;
	if ( index == n ){
		if ( remain == 0 )
			return 0 ;	
		return -10000000;
	}
	int & ret = dp[index][remain] ;
	if ( ret != -1 ) return ret;
	ret = 0 ;
	if ( best_performance[score[index]] >= lb ){
		ret = max ( ret ,  1 + f ( index + 1 , remain - 1 ) );
	}
	else ret = max ( ret , f ( index + 1 , remain - 1 ) );

	if ( best_normal[score[index]] >= lb )
		ret = max ( ret , 1 + f ( index + 1 , remain ) );
	else ret = max ( ret , f ( index + 1 , remain ) );
	return ret;
}
int main (){
	freopen ( "B-large.in" , "r" , stdin ) ;
	freopen ( "B-large.out" , "w" , stdout ) ;
	memset(best_performance,-1,sizeof best_performance);
	memset(best_normal,-1,sizeof best_normal);
	for ( int a = 0 ; a<=10 ; a++ )
		for ( int b=a ; b<=10 && b<=a+2 ; b++ )
			for ( int c = b ; c<=10 && c<=a+2 ; c++ ){
				if ( c - a == 2 ){
					int index = a + b + c;
					if (  best_performance[index] == -1 ) best_performance[index] = c;
					else best_performance[index] = max ( best_performance[index] , c );
				}
				else if ( c - a <= 1 ){
					int index = a + b + c ;
					if ( best_normal [index] == -1 ) best_normal [index] = c;
					else best_normal [index] = max ( best_normal [index] , c ) ;
				}
			}
	int tc;
	cin >> tc;
	for ( int case_number = 1 ; case_number <= tc ; case_number ++ ){
		cin >> n >> nCritical >> lb ;
		for ( int i=0 ; i<n ; i++ )
			cin >> score[i];
		memset(dp,-1,sizeof dp);
		cout << "Case #" << case_number << ": " << f ( 0 , nCritical ) << endl;
	}
}