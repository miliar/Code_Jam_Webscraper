#include <iostream>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int t = 0 ; t < T ; t++){
		int n , k ; cin >> n >> k ;
		int x = 1 << n ;
		bool state = ((k % x) == x-1) ;
		cout << "Case #" << t+1 << ": " << (state?"ON":"OFF") << endl ; 
	}
}
