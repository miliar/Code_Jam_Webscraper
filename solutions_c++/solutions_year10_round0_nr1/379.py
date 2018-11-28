#include <iostream>
#include <vector>
using namespace std;
typedef long long LL;
int main() {
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	for(int i=1; i<=z; i++) {
		LL a, b;
		cin >> a >> b;
		a = 1LL<<a;
		//cout << a << ' ' << b << endl;
		cout << "Case #" << i << ": ";
		if(b%a == (a-1))
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
	return 0;
}
