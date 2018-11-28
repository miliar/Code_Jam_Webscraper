#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int t,n;

int a1,b1;
int a2,b2;

int heights[10001];

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		for (int j = 0; j < 10001; j++) heights[i] = 0;
		cin >> n;
		if (n == 1) { cin >> a1 >> b1; cout << "Case #" << i << ": 0" << endl; }
		else {
			cin >> a1 >> b1;
//			if (a1 > b1) swap(a1,b1);
			cin >> a2 >> b2;
//			if (a2 > b2) swap (a2,b2);
		//	cout << "from " << a1 << " to " << b1 << " vs " << a2 << " to " << b2 << endl;
			int delta = (int)abs((b2 - a2) - (b1-a1));
			//cout << "delta = " << delta << endl;
			if (delta==0) cout << "Case #" << i << ": 0" << endl;
			else {
			double dist = (abs)((double)(a1-a2)/delta);

			//cout << "dist = " <<dist << endl << "intersection must be between " << minHeight << " and " << maxHeight << endl;
			
				if (dist > 0  && dist < 1) cout << "Case #" << i << ": 1" << endl;
				else cout << "Case #" << i << ": 0" << endl;
			}
		}
	}
	
	return 0;
}
