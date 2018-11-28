#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std ;

int t, n, k ;

int main(){
	scanf(" %d", &t) ;
	for(int i = 0 ; i < t ; i++){
		scanf(" %d %d", &n, &k) ;
		n = 1 << n ; k %= n ;
		cout << "Case #" << i + 1 << ": " << (k == n-1 ? "ON" : "OFF") << endl ;
	}
}
