#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int ferlon;
	cin >> ferlon;
	for (int _ = 0; _ < ferlon; _++){
		long long n, a, b, c, d, x0, y0, m;
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		long long cnt[3][3];
		memset(cnt, 0, sizeof(cnt));
		int i;
		for (i = 0; i < n; i++){
			cnt[x0 % 3][y0 % 3]++;
			x0 = (a * (long long) x0 + b) % m;
			y0 = (c * (long long) y0 + d) % m;
		}
		long long ans = 0;
		for (i = 0; i < 9; i++){
			long long tmp = cnt[i / 3][i % 3];
			ans += tmp * (tmp - 1) * (tmp - 2) / 6;			
		}		
		int x1, y1, x2, y2, x3, y3;
		int j, k;
		for (i = 0; i < 9; i++)
			for (j = i + 1; j < 9; j++)
				for (k = j + 1; k < 9; k++){
					x1 = i / 3;
					y1 = i % 3;
					x2 = j / 3;
					y2 = j % 3;
					x3 = k / 3;
					y3 = k % 3;
					if ((x1 + x2 + x3) % 3 == 0 && (y1 + y2 + y3) % 3 == 0) ans += cnt[x1][y1] * (long long) cnt[x2][y2] * (long long)cnt[x3][y3];
				}		
		cout << "Case #" << _ + 1 << ": " << ans << endl;						
	}
	return 0;
}	
