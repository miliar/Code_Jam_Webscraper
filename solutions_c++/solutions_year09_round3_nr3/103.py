#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<cmath>
using namespace std;
int p , q, ind[103] , mas[103][103] ;
int rec( int ind1, int ind2 ){
	if( mas[ind1][ind2] != -1  ) return mas[ind1][ind2] ;
	int qveda = ind[ind1] , zeda = ind[ind2] ;
	int ans =  10000030, i ; 
	for( i= ind1+1; i < ind2; i++){
		int tval =  zeda - qveda - 2 +  rec( ind1 , i   ) + rec( i , ind2) ;
		ans = min( ans , tval ) ;

	}
	if( ans == 10000030  ) ans = 0;
	mas[ind1][ind2] = ans; 
	return ans ; 
	
	
}
int main(){
	freopen("avto.in","r", stdin);
	freopen("avto.out","w", stdout);
	int T ; 
	cin >> T ;
	for( int t = 1; t <= T ; t++){
		cin >> p >> q; 
		int i ;
		for( i=0; i < q; i++ ){
			cin >> ind[i];
		}
		for( i=0; i < 103; i++ )
			for(int j=0; j < 103; j++)
				mas[i][j] = -1 ;
		ind[q] = 0 ; ind[q+1] =  p+1  ; 
		sort( ind , ind + q+2 ) ;
		int val = rec( 0 , q+1 );
		cout << "Case #" << t << ": " << val << "\n" ;
		


		

	}

	return 0;

}