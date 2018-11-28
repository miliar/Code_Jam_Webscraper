#include	<iostream>

using namespace std;

int main(){
	int i;
	int t;
	int n, k, result;
	bool arr[10];
	cin >> t;
	for(i = 1; i <= t; ++i){
		cin >> n >> k;
		result =  (k % (1 << n));
		cout << "Case #" << i << ": ";
		if(result == ((1 << n) - 1))
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}
