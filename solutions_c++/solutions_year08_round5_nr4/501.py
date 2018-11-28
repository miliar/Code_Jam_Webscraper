#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define SZ(a) (int)(a).size()
#define For(i, a, b) for(int i=(a); i<(b); ++i)

typedef long long ll;

void main()
{
	int tc;
	cin >> tc;
	For(_case, 1, tc+1)
	{
		int h, w, R, d[102][102];
		cin >> h >> w >> R;
		memset(d, 0, sizeof(d));
		For(i, 0, R)
		{
			int c, r;
			cin >> c >> r;
			d[c][r]=-1;
		}
		d[1][1]=1;
		For(i, 2, h+1)
			For(j, 2, w+1)
				if (d[i][j]!=-1)
					d[i][j]+=(max(d[i-2][j-1], 0)+max(d[i-1][j-2],0))%10007;
		cout << "Case #" << _case << ": " << d[h][w] << endl;
	}
}