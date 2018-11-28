#include <iostream>

using namespace std;

int main(){
	int n, ni, c, l, i, m, s, x;
	
	cin >> n;

	for (ni = 1; ni <= n; ni++){
		cin >> c;
		
		cin >> m;
		x = m;
		s = m;
		for (i = 1; i < c; i++){
			cin >> l;
			if (m>l) m=l;
			x ^= l;
			s += l;			
		}
		if (x == 0)
			cout << "Case #" << ni << ": " << (s - m) << endl;
		else
			cout << "Case #" << ni << ": NO" << endl;
	}
}
