#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int d, n, a[110];

int check(double z)
{
	int i, j, o;
	double m;

	o=0;
	m=a[0]-z;
	for (i=1; i<n; i++) {
		if ((m+d)>(a[i]+z)) o++;
		m=max(m+d, a[i]-z);
	}
	if (o) return 0;
	else return 1;
}

double find(double l, double r)
{
	double m;
	
	//cerr << l << " - " << r << endl;
	
	if ((r-l)<0.00000001) return l;
	else { 
		m=(l+r)/2;
		if (check(m)) return find(l,m);
			else return find(m,r);
	}
}

int main()
{
	int i, j, k, c, t, p, v;
	double m;
	
	cin >> t;
	for (k=0; k<t; k++) {
		n=0;
		cin >> c >> d;
		for (i=0; i<c; i++) {
			cin >> p >> v;
			for (j=0; j<v; j++) {
				a[n]=p;
				n++;
			}
			m=find(0.0, n*d);  
		}
		cout << "Case #" << k+1 << ": " << m << endl;
	}
	return 0;
}
