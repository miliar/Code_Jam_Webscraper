#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
const int MAXN=1009;
using namespace std;

int a[MAXN][MAXN];
int N;
int ci, cj;

bool able(int x, int y, int dx, int dy)
{
	return dx < 0 || dx > N * 2 - 2 || dy < 0 || dy > N * 2 - 2 || a[dx][dy] < 0 || a[x][y] < 0 || a[dx][dy] == a[x][y];
}

int work()
{
    cin >> N;
		for (int i = 0; i < N * 2; i++)
			for (int j = 0; j < N * 2; j++)
				a[i][j] = -1;
		for (int i = 0; i < 2 * N - 1; i++)
		{
			int count = 0, start = 0;
			if (i < N)
			{
				count = i + 1;
				start = (N - 1) - i;
			}
			else
			{
				count = N - (i - (N - 1));
				start = i - (N - 1);
			}
			for (int j = 0; j < count ;j++)
			{
				cin >> a[i][start];
				start += 2;
			}
		}
		int minsize = INT_MAX;
		int ansx, ansy;
	
		for (int i = 0; i < N * 2 - 1; i++)
			for (int j = 0; j < N * 2 - 1; j++)
			{
  	            bool success=true;
				ci = i, cj = j;
				int s, d, gg, g;
				for (int x = 0; x < N * 2 - 1; x++)
					for (int y = 0; y < N * 2 - 1; y++)
					{
						if (!able(x, y, i * 2 - x, y) || !able(x, y, x, j * 2 - y))
						{
                           success=false;
                           break;
                        }
                        if (!success) break;
                    }   
                if (!success)  continue;
				gg = max(abs(i - j), abs(i + j + 2 - N * 2));
				g = gg / 2 + N / 2;
				if (N % 2)
					if (gg&1)  s = 2 * (g + 1);
					else s = 2 * g + 1;
				else
					if (gg&1)
						s = 2 * g+ 1;
					else
						s = 2 * g;
				if (s < minsize)
				{
					minsize = s;
					ansx = i;
					ansy = j;
				}
              
			}
	return minsize;
}
    

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
	int T;
	cin>>T;
	for (int z = 1; z <= T; z++)
	{
		int minsize=work();
		cout << "Case #" << z << ": " << minsize * minsize - N * N << endl;
	}
	fclose(stdin);    fclose(stdout);
	return 0;
}

