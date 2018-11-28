#include <iostream>
using namespace std;

int main(){
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i=0; i<t; i++){
		cout << "Case #" << i+1;
		int n, k;
		cin >> n >> k;
		if ((k & ((1<<n)-1)) == (1<<n) - 1){
			cout <<  ": ON" << endl;
		} else {
			cout <<  ": OFF" << endl;
		}
	}
	return 0;
}