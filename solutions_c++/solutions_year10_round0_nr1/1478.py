#include <iostream>

using namespace std;

typedef unsigned long long int s64;

int main () {
	int t,c;
	cin >> t;
	c=1;
	while (c <= t) {
		int n,k;
		cin >> n >> k;
		bool state = true;
		for(int i = 0; i < n&&state; i++)
			if(!(k&(1<<i))) state = false;
		if(state) {
			cout << "Case #"<< c << ": ON"<< endl;
		} else {
			cout << "Case #"<< c << ": OFF"<< endl;
		}
		c++;
	}
	return 0;
}
