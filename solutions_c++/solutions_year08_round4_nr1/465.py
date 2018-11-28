#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int ca=0; ca<N; ca++)
	{
		int m, v;
		cin >> m >> v;


		int g[20000], c[20000], a[20000];
		
		for (int i=0; i<(m-1)/2; i++)
			cin >> g[i] >> c[i];
		
		for (int i=(m-1)/2; i<m; i++)
			cin >> a[i];
			
		int f[20000][2];
#define lc(x) (x*2+1)
#define rc(x) (x*2+2)

		for (int i=m-1; i>=(m-1)/2; i--)
		{
			f[i][a[i]] = 0;
			f[i][1-a[i]] = 99999;
		}
		for (int i=(m-1)/2-1; i>=0; i--)
		{

			f[i][0] = 99999;
			f[i][1] = 99999;
			
			//f[i][j] node i is j
			for (int x=0; x<2; x++)
				for (int y=0; y<2; y++)
				{//and
					int val;
					
					val = (g[i]==1) ? (x&&y) : (x||y);
					if (f[lc(i)][x] + f[rc(i)][y] < f[i][val]) // no changes
						f[i][val] = f[lc(i)][x] + f[rc(i)][y];
						
					if (c[i])
					{
						val = (g[i]==0) ? (x&&y) : (x||y); // change
						if (f[lc(i)][x] + f[rc(i)][y] + 1 < f[i][val])
							f[i][val] = f[lc(i)][x] + f[rc(i)][y] + 1;
					}
				}
		}
//		for (int i=0; i<m; i++)
//			printf("%d %d\n", f[i][0], f[i][1]);
			
		if (f[0][v] < 99999)
			printf("Case #%d: %d\n", ca+1, f[0][v]);
		else
			printf("Case #%d: IMPOSSIBLE\n", ca+1);
		
	}
}
