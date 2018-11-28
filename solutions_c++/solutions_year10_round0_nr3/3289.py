#include <iostream>
#include <list>
using namespace std;

list<int> fila, temp;
int r, k, n, a, t;
long long total, parcial;

int main() {
cin >> t;
for (int caso = 1; caso <= t; caso++) {	
	fila.clear();
	temp.clear();
	total = 0;

	cin >> r >> k >> n;
	while (n--) {
		cin >> a;
		fila.push_back(a);
	}
	
	while (r--) {
		parcial = 0;
		while (!fila.empty() && parcial + fila.front() <= k) {
			parcial += fila.front();
			temp.push_back(fila.front());
			fila.pop_front();
		}
		
		while (!temp.empty()) {
			fila.push_back(temp.front());
			temp.pop_front();
		}
		total += parcial;
//		cout << parcial << endl;
	}
	cout << "Case #" << caso << ": " << total  << endl;
}
return 0;
}
