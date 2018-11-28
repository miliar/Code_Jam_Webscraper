#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

long long f[100001];
long long infi;
int h[100001],pos[100001],app[100001],b[100];
int n;

void up(int x)
{
	int y = (x -1) / 2;
	if (f[h[x]] < f[h[y]])
	{
		pos[h[x]] = y;
		pos[h[y]] = x;
		int t = h[x];
		h[x] = h[y];
		h[y] = t;
		up(y);
	}
}

void down(int x)
{
	int y = x * 2+1;
	if (y >= b[n-1]) return;
	if (y + 1 <b[n-1])
	{
		if (f[h[y+1]] < f[h[y]]) y = y +1;
	}
	if (f[h[y]] < f[h[x]])
	{
		pos[h[x]] = y;
		pos[h[y]] = x;
		int t = h[x];
		h[x] = h[y];
		h[y] = t;
		down(y);
	}
}
		

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	cin >> t;
	for (int T = 0; T < t; T++)
	{
		long long l;
		cin >> l;
		cin >> n;
		for (int i = 0; i < n; i++) cin >> b[i];
		for (int i = 0; i < n ; i++)
			for (int j = i ; j < n ; j++)
				if (b[i] > b[j])
				{
					int tt = b[i];
					b[i] = b[j];
					b[j] = tt;
				}
		cout << "Case #"  << T+1 << ": ";
		if ((n == 1)&&(b[0] == 1)) cout << l << endl;
		else{
			infi = 1000000000;
			infi = infi * infi;
			infi = infi +1;
			for (int i = 0; i < b[n - 1]; i++) {
				f[i] = infi;				
			}
			f[0] = 0;
			f[b[n-1]] = infi + 1;
			for (int i = 0; i < b[n-1]; i++)
			{
				h[i] = i;
				pos[i] = i;
			}
			for (int i = 0; i < b[n-1]; i++)
			{
				int x = h[0];
				for (int j = 0; j < n -1 ; j++)
				{
					int  y = 0;
					int k = (x + b[j]) % b[n-1];
					if (x + b[j] < b[n-1]) y = 1;
					if (f[x] + y < f[k])
					{
						f[k] = f[x] + y;
						up(pos[k]);
					} 
				}
				h[0] = b[n-1];
				down(0);
			}
			long long ans = f[l % b[n-1]] + l / b[n-1];
			if (ans < infi) cout << ans << endl; else cout << "IMPOSSIBLE\n";
		}
	}
}
