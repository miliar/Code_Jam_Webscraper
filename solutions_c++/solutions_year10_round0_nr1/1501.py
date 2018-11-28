#include <iostream>

using namespace std;

typedef long long int int64;

int main(){
	int64 t;
	cin >> t;
	for(int64 i = 0; i < t; i++){
		int64 n, k;
		cin >> n >> k;
		int64 offset = 0;
		for(int64 i = 0; i < n; i++){
			offset += 1 << i;
		}
		int64 div = 1 << n;

		bool ret;
		if((k - offset) % div == 0)
			ret = true;
		else
			ret = false;
		
		cout << "Case #" << (i+1) << ": " << (ret ? "ON" : "OFF") << endl;
	}
}
