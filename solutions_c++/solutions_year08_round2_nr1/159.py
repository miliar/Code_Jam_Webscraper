#include <iostream>
#include <fstream>
using namespace std;

long long m;

long long cnt[4][4];
#define add(x, y) cnt[x%3][y%3]++;
int main()
{
	ifstream cin("large.in");
	ofstream cout("large.out");

	int z;
	cin>>z;
	int tc = 1;
	while(z--)
	{
		memset(cnt, 0, sizeof(cnt));

		int n;
		long long A, B, C, D;
		cin>>n>>A>>B>>C>>D;

		long long x, y;
		cin>>x>>y>>m;

		add(x, y);
		for (int i = 1 ; i < n ; i++)
		{
			x = (A*x + B)%m;
			y = (C*y + D)%m;
			add(x, y);
		}

		long long res = 0;
#define FOR(a, b) for (int a = b ; a < 3 ; a++)
#define conv(a, n) int x##n = a/3; int y##n = a%3

		for (int i = 0 ; i < 9 ; i++)
			for (int j = i ; j < 9 ; j++)
				for (int k = j ; k < 9 ; k++)
				{
					conv(i, 1);
					conv(j, 2);
					conv(k, 3);

					if ((x1 + x2 + x3)%3 == 0 && (y1 + y2 + y3)%3 == 0)
					{
						long long c = cnt[x1][y1];
						int dec = 0;
						if (i == j) dec++;
						c *= cnt[x2][y2]-dec;
						if (j == k) dec++;
						c *= cnt[x3][y3]-dec;

						if (dec == 1) c /= 2;
						else if (dec == 2) c /= 6;
						res += c;
					}
				}

		cout<<"Case #"<<tc++<<": "<<res<<endl;
			

	}
}