#include <iostream>
#include <string>
using namespace std;
const int maxx = 500;

class fenwik 
{
private:
	int f[maxx];
	int fn;
public:
	fenwik()
	{
		fn = maxx;
		memset(f, 0, sizeof f);
	}
	void init()
	{
		memset(f, 0, sizeof f);
	}
	void fmod(int ind, int val)
	{
		for(int i = ind; i < fn; i |= i + 1)
			f[i] += val;
	}
	int fsum(int r)
	{
		int res = 0;
		for(int i = r; i >= 0; i &= i + 1, i--)
			res += f[i];
		return res;
	}
	int fsum(int l, int r)
	{
		return fsum(r) - fsum(l - 1);
	}
};


fenwik h[maxx];
fenwik v[maxx];

#define X first
#define Y second
char s[40];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int z = 1; z <= t; ++z)
	{
		for(int i = 0; i < maxx; ++i)
			h[i].init(),
			v[i].init();
		int L; cin >> L;
		int x = maxx / 2, y = maxx / 2;
		int dir = 0;
		for(int i = 0; i < L; ++i)
		{
			int rep;
			scanf("%s %d", s, &rep);
			int sn = strlen(s);
			for(int j = 0; j < rep; ++j)
			{
				for(int k = 0; k < sn; ++k)				
					if(s[k] == 'L')
						dir = (dir + 1) % 4;
					else if(s[k] == 'R')
						dir = (dir - 1 + 4) % 4;
					else // 'F'
					{
						if(dir == 0)
							h[y].fmod(x, 1), y++;
						else if(dir == 2)
							h[y - 1].fmod(x, 1), y--;
						else if(dir == 1)
							v[x].fmod(y, 1), x++;
						else if(dir == 3)
							v[x-1].fmod(y, 1), x--;
					}
			}
		}
		int cnt = 0;
		for(int i = 0; i < maxx; ++i)
			for(int j = 0; j < maxx; ++j)
			{
				int hj = h[j].fsum(i);
				if((hj & 1) == 0)
				{
					int hj2 = h[j].fsum(i+1, maxx-1);
					if(hj > 0 && hj2 > 0)
						cnt++;
					else
					{
						int vi = v[i].fsum(j);
						int vj = v[i].fsum(j+1, maxx-1);
						if(vi > 0 && vj > 0)
							cnt++;
					}
				}
			}
		printf("Case #%d: %d\n", z, cnt);
	}
	return 0;
}