#include <iostream>

using namespace std;

int main(){
	int T; cin >> T;
	for(int test=1;test<=T;test++){
		int N, K; cin >> N >> K;
		cout << "Case #" << test << ": " << (K%(1<<N) == (1<<N)-1 ? "ON" : "OFF") << endl; 
	}
}