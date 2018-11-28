#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int i,j,kase,k,l,ans,a,b,c,d,x0,y0,m,n,cnt;
	long long x[100],y[100];
	int dup[100];
	cin >> kase;
	for (i = 1;i <= kase;i ++) {
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		//cout << n << " " << a << " " << b << " " << c << " " << d << " " << x0 << " " << y0 << " " << m << endl;
		cnt = 0;
		x[0] = x0;
		y[0] = y0;
		for (j = 0;j < n;j ++) dup[j] = 0;
		for (j = 1;j < n;j ++) {
			x[j] = ((((a % m) * (x[j - 1] % m)) % m) + (b % m)) % m;
			y[j] = ((((c % m) * (y[j - 1] % m)) % m) + (d % m)) % m;
			for (k = 0;k < j;k ++) {
				if (x[j] == x[k] && y[j] == y[k]) {
					dup[j] = 1;
					break;
				}
			}
		}
		for (j = 0;j < n;j ++) {
			//cout << x[j] << "," << y[j] << endl;
		}
		for (j = 0;j < n;j ++) {
			for (k = j + 1;k < n;k ++) {
				if (k >= n) break;
				for (l = k + 1;l < n;l ++) {
					if (l >= n) break;
					if (   !dup[j] && !dup[k] && !dup[l]
						&& (((x[j] % 3) + (x[k] % 3) + (x[l] % 3)) % 3 == 0)
						&& (((y[j] % 3) + (y[k] % 3) + (y[l] % 3)) % 3 == 0)  ) {
						cnt ++;
					}
				}
			}
		}

		cout << "Case #" << i << ": " << cnt << endl;
	}
}