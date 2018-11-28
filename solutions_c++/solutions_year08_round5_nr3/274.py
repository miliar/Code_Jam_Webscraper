#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<int> VI;
typedef vector<VI> VVI;

int getchair(const VC& v)
{
	int retval = 0;
	for (int i=0; i<(int)v.size(); i++)
		if (v[i] == 'x')
			retval += (1 << i);
	return retval;
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int m, n;
		cin >> m >> n;
		VVC a(m, VC(n, '.'));
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
				cin >> a[i][j];
		int upto = 1 << n;
		VVI num(m, VI(upto, 0));
		for (int p=0; p<upto; p++)
		{
			if (p & (p << 1))
				continue;
			if (p & (p >> 1))
				continue;
			int chair = getchair(a[0]);
			if (p & chair)
				continue;
			int cnt = 0;
			for (int k=0; k<n; k++)
				if (p & (1 << k))
					cnt++;
			num[0][p] = cnt;
		}
		for (int i=1; i<m; i++)
		{
			for (int pcur=0; pcur<upto; pcur++)
			{
				if (pcur & (pcur >> 1))
					continue;
				if (pcur & (pcur << 1))
					continue;
				int chair = getchair(a[i]);
				if (pcur & chair)
					continue;
				int cnt = 0;
				for (int k=0; k<n; k++)
					if (pcur & (1 << k))
						cnt++;
				for (int prev=0; prev<upto; prev++)
				{
					if (pcur & (prev << 1))
						continue;
					if (pcur & (prev >> 1))
						continue;
					num[i][pcur] = max(num[i][pcur], num[i-1][prev]+cnt);
				}
			}

		}
		int sol = 0;
		for (int p=0; p<upto; p++)
			sol = max(sol, num[m-1][p]);
		cout << "Case #" << kase << ": " << sol << endl;
	}
	return 0;
}
