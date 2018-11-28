#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

struct walk {
	int begin;
	int end;
	int speed;
};

bool cmp( walk a, walk b ) {
	if ( a.speed == b.speed ) {
		if ( a.begin == b.begin ) {
			return a.end < b.end;
		}
		return a.begin < b.begin;
	}

	return a.speed < b.speed;
}

int main()
{
	freopen("F:\\gcj\\a0.txt","r", stdin);
	freopen("F:\\gcj\\a0o.txt","w", stdout);

	int t;
	cin >> t;
	for ( int Case = 1; Case <= t; Case++ ) {
		int x,s,r,ti,n;
		cin >> x >> s >> r >> ti >> n;
		
		double t = ti;
		double left = x;
		walk w[1005];
		for ( int i = 0; i < n; i++ ) {
			cin >> w[i].begin >> w[i].end >> w[i].speed;
			left -= (w[i].end - w[i].begin);
		}

		sort( w, w + n, cmp );

		double ans = 0.0;
		if ( t * r <= left ) {
			left -= t *  r;
			ans += t;
			ans += left * 1.0 / s;
			for ( int i = 0; i < n; i++ ) {
				ans += ( w[i].end - w[i].begin + 0.0 ) / ( s + w[i].speed);
			}
		}  else {
			ans += ( left / r );  
			t -= ( left / r);
			for ( int i = 0; i < n; i++ ) {
				if ( t * ( w[i].speed + r ) <= (w[i].end - w[i].begin + 0.0)  ) {
					ans += t;
					ans += ( (w[i].end - w[i].begin + 0.0) - t * ( r + w[i].speed ) ) / ( s + w[i].speed ) ;
					t = 0;
				} else {
					ans +=  (w[i].end - w[i].begin + 0.0) / ( r + w[i].speed ) ;
					t -= (w[i].end - w[i].begin + 0.0) / ( r + w[i].speed );
				}
			}
		}

		printf("Case #%d: %6lf\n", Case, ans);
	}

	return 0;
}

