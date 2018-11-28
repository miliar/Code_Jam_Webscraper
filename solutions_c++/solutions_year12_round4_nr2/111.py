#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

const int MAXN = 1024;

int n, w, l;
int r[MAXN];


void Work()
{
	cin >> n >> w >> l;
	for (int i = 0; i < n; i ++)
		cin >> r[i];
//	sort(r, r + n);

	int h1 = -1000000000, w1, i, ww, hh, hd;
	bool next;
	for (i = 0; i < n; )
	{
		next = false;
		w1 = -1000000000;  hd = 0;
		for (; i < n; i ++)
		{
			hh = max(0, h1 + r[i]);
			ww = max(0, w1 + r[i]);
			if (ww > w)   break; 
			printf(" %.1f %.1f", (double)ww, (double)hh);
			w1 = ww + r[i];
			hd = max(hd, hh + r[i]);
		}
		h1 = hd;
	}
	cout << endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		cout << "Case #" << k << ":";
		Work();
	}

	return 0;
}