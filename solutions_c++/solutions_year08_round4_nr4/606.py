
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>

using namespace std;

#define PATH "c:\\jam3\\jam3\\"

		char buf[1024];
		int k;

int mini;

int check(int p[5], int use[5], int pos)
{
	if (pos == k)
	{
		int cnt = 0;
		int prev = -1;
		for (int n = 0; n < strlen(buf); ++n)
		{
			int cc = (int)(n / k) * k + p[n % k];
			if (prev != buf[cc])
			{
				++cnt;
				prev = buf[cc];
				if (cnt > mini)
					return -1;
			}
		}
		if (cnt < mini)
			mini = cnt;
		return 0;
	}

	for (int c = 0; c < k; ++c)
	{
		if (use[c]) continue;
		p[pos] = c;
		use[c] = 1;
		check(p, use, pos + 1);
		use[c] = 0;
	}
	return mini;
}

int main(void)
{
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    int count;
    fin >> count;

    for (int c = 1; c <= count; ++c)
    {
		fin >> k;
		fin.getline(buf, 1024);
		fin.getline(buf, 1024);

		int i,j;
		for (i = 0; i < strlen(buf); ++i)
			if (buf[i] < 'a' || buf[i] >'z') buf[i] = 0;

		int p[5];
		int use[5] = {0};
		mini = 10000;
		int ans = check(p, use, 0);

		fout << "Case #" << c << ": " << ans << "\n";
    }

    return 0;
}

