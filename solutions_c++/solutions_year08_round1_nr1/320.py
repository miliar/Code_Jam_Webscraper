#include <iostream>
#include <algorithm>
using namespace std;

typedef long long num;

const int maxN = 2048;

num x[maxN], y[maxN];

void doit(){
	int i, n;
	num res = 0;
	cin >> n;
	for(i = 0; i < n; i++) cin >> x[i];
	for(i = 0; i < n; i++) cin >> y[i];
	sort(x, x + n);
	sort(y, y + n);
	//cout << "n:" << endl;
	//cout << n << endl;
	//for(i = 0; i < n; i++) cout << x[i] << " ";
	//cout << endl;
	//f//or(i = 0; i < n; i++) cout << y[i] << " ";
	for(i = 0; i < n; i++) res += x[i]*y[n - 1 - i];
	//cout << endl;
	cout << res;
}

int main(){
	int tst, tc;
	cin >> tst;
	for(tc = 1; tc <= tst; tc++){
		cout << "Case #" << tc <<": ";
		doit();
		cout << endl;
	}
	return 0;
}