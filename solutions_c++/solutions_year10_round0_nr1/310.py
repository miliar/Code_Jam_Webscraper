#include <iostream>

using namespace std;



int main(){
	int nt, tt;
	cin >> nt;
	int n, k;
	for (tt = 1; tt <= nt; tt++)
	{
		cin >> n >> k;
		cout << "Case #" << tt << ": ";
		if ((k + 1) % (1 << n) == 0) cout << "ON\n";
		else cout << "OFF\n";
	}
	return 0;
}
