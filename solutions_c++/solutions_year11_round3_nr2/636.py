#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	long long i, j, k, t, c, n, l, m, mb, b, q, mb2;
	long long a[1010], m1, m2, a1, a2;
		
	cin >> t;
	for (k=0; k<t; k++) {
		cin >> l >> q >> n >> c;
		m1=0; 
		m2=0;
		for (i=0; i<c; i++) 
			cin >> a[i];
		m=0;
		mb=0;
		mb2=0;
		if (l==0)
			for (i=0; i<n; i++) 
				m+=a[i%c]*2;
		if (l>0) {
			for (i=0; i<n; i++) {
				b=(a[i%c]*2-max((q-m), m2))/2;
				if (b>mb) {
					mb=b;	
					m1=i;
				}
				m+=a[i%c]*2;
			}
			m-=mb;
		}
		if (l==2) {
			m=0;
			for (i=0; i<n; i++) {
				if (i==m1) {
					m+=a[i%c]*2-mb;
				}
				else {
					b=(a[i%c]*2-max((q-m),m2))/2;
					if (b>mb2) mb2=b;	
					m+=a[i%c]*2;
				}
			}
			m-=mb2;
		}
		cout << "Case #" << k+1 << ": " << m <<	endl;
	}
	return 0;
}
