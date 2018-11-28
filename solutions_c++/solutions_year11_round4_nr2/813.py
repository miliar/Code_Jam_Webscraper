#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <sstream>
#include <cstdio>
#include <algorithm>
using namespace std;

char t[505][505];
#define EPS 1e-9

int main()
{
	int T; cin >> T;
	for (int C = 1; C <= T; ++C)
	{
		int r, c, d;
		cin >> r >> c >> d;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				cin >> t[i][j];
		
		int ret = -1;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
			{
				for (int size = 3; size <= min(r-i, c-j); ++size)
				{
					pair<double,double> p(0,0);
					double sum = .0;
					for (int k = 0; k < size; ++k)
						for (int l = 0; l < size; ++l)
						{
							if ( k == 0 and l == 0 ) continue;
							if ( k == size-1 and l == 0 ) continue;
							if ( k == 0 and l == size-1 ) continue;
							if ( k == size-1 and l == size-1 ) continue;
							
							//cout << k << "," << l << ": " << ( size/2.0 - (k+.5))*(t[i+k][j+l]-'0') << "," <<
							//								 (size/2.0 - (l+.5))*(t[i+k][j+l]-'0') << endl;
							p.first += (k+.5)*(t[i+k][j+l]-'0'+d);
							p.second += (l+.5)*(t[i+k][j+l]-'0'+d);
							sum += (t[i+k][j+l]-'0'+d);
						}
					//cout << i << "," << j << "," << size << ": " << p.first << "," << p.second << " " << sum << endl;
					p.first /= sum; p.first -= size/2.0;
					p.second /= sum; p.second -= size/2.0;
					//cout << i << "," << j << "," << size << ": " << p.first << "," << p.second << " " << sum << endl;
					if ( abs( p.first ) < EPS and abs(p.second) < EPS )
						ret = max(ret, size);
				}
			}
	
		cout << "Case #" << C << ": ";
		if (ret == -1) cout << "IMPOSSIBLE\n";
		else cout << ret << endl;
	}
}
