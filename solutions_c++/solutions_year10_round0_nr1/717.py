#include <iostream>
using namespace std;

int main() {
	int t; cin>>t;
	for (int c = 1; c <= t; c++) {
		int n, k; cin>>n>>k;
		bool ok = true;
		for (int i = 0; i < n; i++) {
			if (!(k&1<<i)) ok = false;
		}
		cout<<"Case #"<<c<<": "<<(ok?"ON":"OFF")<<endl;
	}
	return 0;
}
