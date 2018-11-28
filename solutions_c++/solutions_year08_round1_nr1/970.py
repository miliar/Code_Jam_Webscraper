
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

#define PATH "c:\\jam3\\debug\\"

long long mini = 100000LL *100000*802;
long long r[801][801];
long long mi[801];

long long check(bool b[801], int n, int p, long long pre)
{
if (n == p) return pre;
if (pre + mi[p] + 1 > mini) return mini + 1;

for(int k = 0; k < n; ++k)
{
	if (b[k])
		continue;
	b[k] = true;
	long long ans = check(b, n, p + 1, pre + r[p][k]);
	if (ans < mini)
	{
		mini = ans;
	}
	b[k] = false;
}
return mini;

}

int main(void)
{
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    string line;

    int count;
    fin >> count;
    for (int t = 1; t <= count; ++t)
    {
		int x[801];
		int y[801];

        int i;
        int numEngine;
		int n;
		fin >> n;
		for (i = 0; i <n ; ++i) fin >> x[i];
		for (i = 0; i <n ; ++i) fin >> y[i];

		for (i = 0; i < n; ++i)
		{
			mi[i] = 0;
			for (int j = 0; j < n; ++j)
			{
				r[i][j] = x[i]*y[j];
				if (mi[i] > r[i][j])
					mi[i] = r[i][j];
			}
		}
		for (i = n - 2; i >= 0; --i)
			mi[i] = mi[i] + mi[i + 1];

		mini = 100000LL *100000*802;
		bool b[801] = {false};
		long long ans = check(b, n, 0, 0);


        fout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

