#include <iostream>
#include <vector>
#include <complex>
using namespace std;

typedef complex<double> point;

double inline det(const point & u, const point & v) {
	return imag(conj(u) * v);
}

// Test whether [a,b] and [c,d] intersect each other
bool inline intersect(const point & a, const point & b, const point & c,
		const point & d) {
	double z = det(b - a, d - c);
	double x = det(c - a, b - a);
	double y = det(d - c, a - c);
	int sx = (x > 0 ? 1 : -1);
	int sy = (y > 0 ? 1 : -1);
	// Compute the test using only integers if possible
	return (z != 0 && x * z >= 0 && sx * x < sx * z && y * z >= 0 && sy * y
			< sy * z);
}

int main(void) {
	int t,num,n,i,j,x,y,accu;
	vector<point> a,b;
	for(cin >> t, num = 1; num <= t; ++num) {
		cin >> n;
		a.resize(n);
		b.resize(n);
		for (i = 0; i < n; ++i) {
			cin >> x >> y;
			a[i] = point(0,x);
			b[i] = point(1,y);
		}
		accu = 0;
		for (i = 0; i < n; ++i) {
			for (j = i+1; j < n; ++j) {
				if (intersect(a[i],b[i],a[j],b[j]))
					++accu;
			}
		}
		cout << "Case #" << num << ": " << accu << endl;
	}
}
