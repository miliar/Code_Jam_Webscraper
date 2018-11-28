#include<iostream>
#include<cmath>
using namespace std;
#define forn(i,n) for(int i = 0; i < n; i++)

double x[1000],y[1000],z[1000];
double a[1000],b[1000], c[1000];
double xx, yy, zz, aa, bb, cc;

int main()
{
	freopen("C:\\1.txt","rt",stdin);
	freopen("C:\\2.txt","wt",stdout);
	int T, i;
	cin >> T;
	for(int test = 0; test < T; test++)
	{		
		int n;
		cin >> n;
		xx = 0; yy = 0; zz = 0; aa = 0; bb = 0; cc = 0;
		for(i = 0; i < n; i++) cin >> x[i] >> y[i] >> z[i] >> a[i] >> b[i] >> c[i];
		forn(i,n) xx += x[i];
		forn(i,n) yy += y[i];
		forn(i,n) zz += z[i];
		forn(i,n) aa += a[i];
		forn(i,n) bb += b[i];
		forn(i,n) cc += c[i];
		xx /= n; yy /= n; zz /= n; aa /= n; bb /= n; cc /= n;
		double tmin;
		if ( 2 * aa * aa + 2 * bb * bb + 2 * cc * cc < 0.000001 ) tmin = 0;
		else tmin = - ( 2. * xx * aa + 2 * yy * bb + 2 * zz * cc ) /
			( 2 * aa * aa + 2 * bb * bb + 2 * cc * cc );
		if ( tmin < 0 ) tmin = 0;
		double dmin = sqrt ( ( xx + aa * tmin ) * ( xx + aa * tmin ) + 
			( yy + bb * tmin ) * ( yy + bb * tmin )
			+ ( zz + cc * tmin ) * ( zz + cc * tmin ) );		
		cout << "Case #" << test + 1 << ": ";
		printf("%.7lf %.7lf\n",dmin,tmin);
		//cout << dmin <<" " << tmin << endl;
	}
	return 0;
}