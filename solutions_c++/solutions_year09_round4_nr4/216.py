#include <iostream>
#include <vector>
using namespace std;

#define MAX 50

#define EPS 1E-7

int nTest, test, n, x[MAX], y[MAX], r[MAX];

double _l, _r, _m, ret;

vector<int> a, b;

double sqr(double a) {return a*a;}

bool intersect(int i, int j, double R) {
	return sqr(x[i]-x[j])+sqr(y[i]-y[j]) < sqr(R-r[i]+R-r[j]);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);	
	
	cin >> nTest;
	for (int test=1; test<=nTest; ++test) {
		cin >> n;
		for (int i=0; i<n; ++i) {
			cin >> x[i] >> y[i] >> r[i];
		}
		
		if (n==1) {
			ret=r[0];
		} else if (n==2) {
			ret=max(r[0], r[1]);
		} else {
		
		_l=0; _r=100000;
		while (_l+EPS < _r) {
			_m=(_l+_r)/2;
			
			a.clear();
			b.clear();
			
			bool can=true;
			
			for (int i=0; i<n; ++i) {
				bool ok=true;
				for (int j=0; j<a.size(); ++j) {
					if (!intersect(i,a[j], _m)) {
						ok=false;
						break;
					}
				}
				if (ok) {
					a.push_back(i);
					continue;
				}
				
				ok=true;
				for (int j=0; j<b.size(); ++j) {
					if (!intersect(i,b[j],_m)) {
						ok=false;
						break;
					}
				}
				if (ok) {
					b.push_back(i);
					continue;
				}	
				
				can=false;
				break;		
			}
			
			if (can) {
				ret=_m;
				_r=_m;
			} else
				_l=_m;
		}
		}
		
		printf("Case #%d: %.6lf\n", test, ret);
	}

	return 0;
}
