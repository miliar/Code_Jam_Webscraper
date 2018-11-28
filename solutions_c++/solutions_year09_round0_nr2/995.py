#include <cstdio>
#include <map>
using namespace std;

int t, h, w;
int step[4][2] = {{-1,0},{0,-1},{0,1},{1,0}}; // N W E S
int m[100][100];
int r[10000];
map<int,char> c;
inline bool valid(int i, int j)
{
	return (i>=0)&&(i<h)&&(j>=0)&&(j<w);
}
int relax(int x)
{
	if (r[x] == x) // root
		return x;
	r[x] = relax(r[x]);
	return r[x];
}
inline void num(int x)
{
	if (c.find(x) == c.end())
		c[x] = c.size()+'a';
}

int main()
{
	freopen("D:/gcj/b.txt", "w", stdout);
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ++ti)
	{
		scanf("%d%d", &h, &w);
		for (int i = 0; i<h; ++i)
			for (int j = 0; j<w; ++j)
				scanf("%d", &m[i][j]);
		int pos = 0;
		for (int i = 0; i<h; ++i)
		{
			for (int j = 0; j<w; ++j)
			{
				int ma = m[i][j];
				int mk = pos;
				for (int k = 0; k<4; ++k)
				{
					int ii = i+step[k][0], jj = j+step[k][1];
					if (valid(ii, jj) && m[ii][jj]<ma) // can flow
					{
						ma = m[ii][jj];
						mk = ii*w+jj;
					}
				}
				r[pos] = mk; // flow to
				++pos;
			}
		}
		c.clear();
		printf("Case #%d:\n", ti);
		pos = 0;
		for (int i = 0; i<h; ++i)
		{
			for (int j = 0; j<w; ++j)
			{
				relax(pos);
//				printf("%d:", r[pos]);
				num(r[pos]);
				putchar(c[r[pos]]);
				putchar((j==w-1)?'\n':' ');
				++pos;
			}
		}
	}
//	system("pause");
	return 0;
}