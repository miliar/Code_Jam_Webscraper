#include<iostream>
#include<set>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<vector>
using namespace std ;
int pot[8];
int dig( int n ){
	int res = 0;
	while( n ) n/=10, res++;
	return res;
}
set<pair<int,int> > S;
void F( int n, int b ){
	int dg = dig( n);
	int res = 0;
	for( int i  = 0 ; i <= 8; i++){
		int t = n, k = 0, T = 0;
		int f = 1;
		while( k++ < i  && t){
			T += f*( t % 10);
			f *= 10;
			t /= 10;
		}
		int N = t + T * pot[ dg - k + 1];
		if ( N <= b && N > n ) {
			S.insert( make_pair( n, N ));
		}
	}
}

int main(){
	pot[0] = 1;
	for( int i = 1; i < 8;i++) pot[i] = 10*pot[i-1];
	int T, a, b;
	cin >> T;
	for( int r  = 1; r <= T ; r++){
		int res  = 0;
		cin >> a >> b;
		S.clear();
		for( int i = a ; i <= b; i++){
			 F( i, b );
		}
		res = S.size();
		printf("Case #%d: %d\n",  r,res);
	}


	return 0;
}
