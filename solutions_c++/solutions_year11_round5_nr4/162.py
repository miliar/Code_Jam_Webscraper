#include <iostream>
#include <string>

using namespace std;

const int MAX = 1 << 26;

int z[2][MAX];

string get(int x, int len)
{
	__int64 y = x;
	y *= y;
	char buf[200] = {0};
	for (int i = len-1; y; y >>= 1, i--)
	{
		buf[i] = '0' + (y & 1);
	}
	return string(buf);
}

bool cmp(int x, string n, int len)
{
	__int64 y = x;
	y *= y;
	for (int i = 1; i <= len; i++, y >>= 1)
	{
		if (i > n.length())
		{
			if (y & 1)
				return false;
			continue;
		}
		if (n[n.length()-i] == '0' + ((~y) & 1))
			return false;
	}
	return true;
}

int main()
{
  freopen("d.in", "r", stdin);
  freopen("d.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		string n;
		cin >> n;
		int pmax = (n.length() + 1) / 2;
		int zl = 1;
		int cur = 0;
		int p = 1;
		z[cur][0] = 0;
		for (int i = 0; i < pmax - 1; i++)
		{
			int curl = 0;
			for (int j = 0; j < zl; j++)
			{
				if (cmp(z[cur][j], n, i+1))
					z[!cur][curl++] = z[cur][j];
				if (cmp(z[cur][j] + p, n, i+1))
					z[!cur][curl++] = z[cur][j] + p;
			}
			zl = curl;
			p <<= 1;
			cur = !cur;
		}
		int curl = 0;
		for (int j = 0; j < zl; j++)
		{
			if (cmp(z[cur][j] + p, n, n.length()))
				z[!cur][curl++] = z[cur][j] + p;
		}
		zl = curl;
		cur = !cur;
		cout << get(z[cur][0], n.length());
    cout << endl;
  }
  return 0;
}