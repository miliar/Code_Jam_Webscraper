#include <iostream>
#include <fstream>

using namespace std;

#define cin fin
#define cout fout

ifstream fin("A-large.in");
ofstream fout("a.out");

const int maxn = 100000;

long long s[16];

int main()
{
	int num, t;
    long long x,y, a, b, c, d, m, n, i, ans, j , k;
	long long tmp;
	cin >> t;
	for (num = 1;num <= t;num ++)
	{
		cin >> n >> a >> b >> c >> d >> x >> y >> m;
		memset(s, 0, sizeof(s));
		s[(x % 3) * 3 + (y % 3)] ++;
		for (i = 1;i <= n- 1;i ++)
		{
			tmp = x;
			tmp = (tmp * a + b) % m;
			x = tmp;
			tmp = y;
			tmp = (tmp * c + d) % m;
			y = tmp;
			s[(x % 3) * 3 + (y % 3)] ++;
		
		}
//		for (i = 0;i < 9;i ++ ) cout << i << " " << s[i] << endl;
		ans = 0;
		for (i = 0;i < 9;i ++)
			if (s[i] > 0)
			for (j = i;j < 9;j ++)
				if (s[j] > 0)
				for (k = j;k < 9;k ++)
					if (s[k] > 0)
				{
					if ((i / 3 + j / 3 + k / 3) % 3 == 0 && ((i % 3 + j % 3 + k % 3) % 3) == 0)
						if (i == j) {
							if (j == k) {
								ans += s[i] * (s[i] - 1) / 2 * (s[i] - 2) / 3;
							} else {
								ans += s[i] * (s[i] - 1) / 2 * s[k];
							}
						} else {
							if (j == k)
								ans += s[j] * (s[j] - 1) / 2 * s[i];
							else 
								ans += s[i] * s[j] * s[k];
						}
							
				}
		cout << "Case #" << num << ": " << ans << endl;
	}
	return 0;
}
