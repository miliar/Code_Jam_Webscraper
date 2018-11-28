#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int i, j, k, t, n, l, h, m, a[101], z;
		
	cin >> t;
	for (k=0; k<t; k++) {
		cin >> n >> l >> h;
		for (i=0; i<n; i++)
		  cin >> a[i];
		m=0;
		for (i=h; i>=l; i--) {
			z=1;
			for (j=0; j<n; j++) {
				if (a[j]>i) {
					if (a[j]%i)	z=0;
				}
				else {
					if (i%a[j])	z=0;
				}
			}
			if (z) m=i;
		} 
		if (m) cout << "Case #" << k+1 << ": " << m <<	endl;
		else cout << "Case #" << k+1 << ": NO" <<	endl;
	}
	return 0;
}
