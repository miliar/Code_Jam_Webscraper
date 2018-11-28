									/* in the name of Allah */
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

ifstream fin("C-smallarge.in");
ofstream fout("C-smallarge.out");

#define cin fin
#define cout fout

int main(){
	int T, test = 0;
	int n, a, mn, xor, sum;
	for(cin >> T; T--; ){
		mn = 10000000;
		sum = xor = 0;
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> a;
			mn = min(a, mn);
			sum += a;
			xor ^= a;
		}
		cout << "Case #" << ++test << ": ";
		if(xor == 0)
			cout << sum - mn << endl;
		else cout << "NO" << endl;
	}
	return 0;
}
