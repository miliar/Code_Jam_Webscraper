#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std ;
int main(){
	int TCase ;
	cin >> TCase ;
	for(int T = 1 ; T<=TCase ; T++){
		int n ;
		cin >> n ;
		vector<long long> a(n) , b(n) ;
		for(int i = 0 ; i < n ; i++){
			cin >> a[i] ;
		}
		for(int i = 0 ; i < n ; i++){
			cin >> b[i] ;
		}

		sort(a.begin(),a.end()) ;
		sort(b.begin(),b.end()) ;
		long long sum = 0 ;
		for(int i = 0 ; i < n ; i++){
			sum += a[i] * b[n-i-1] ;
		}
		cout << "Case #" << T << ": " << sum << endl ;
	}
}
