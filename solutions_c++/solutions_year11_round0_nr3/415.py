#include <iostream>

using namespace std;

int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		int n;
		cin >> n;
		int sum= 0, sumX= 0, minVal= 1000 * 1000 * 1000;
		for (int i=0 ; i<n ; i++){
			int k;
			cin >> k;
			sumX^= k;
			sum+= k;
			if (k < minVal)
				minVal= k;
		}
		cout << "Case #" << t << ": ";
		if (sumX==0)
			cout << sum - minVal;
		else
			cout << "NO";
		cout << endl;
	}
	return 0;
}