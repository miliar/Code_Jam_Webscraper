#include <iostream>
using namespace std;

int main(){
	int t, n, k;
	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> n >> k;
		int flag = 1;
		for (int j = 0; j < n; j++){
			if (!(k & (1 << j))){
				flag = 0;
				break;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (flag) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
	return 0;
}
