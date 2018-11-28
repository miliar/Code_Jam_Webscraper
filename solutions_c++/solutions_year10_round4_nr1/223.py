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

int l[200];
int a[200][100];
int b[200][100];
int aa[200];
int bb[200];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >> t;
	int ll;
	for (int T = 0;  T < t; T++)
	{
		int k;
		int ans = 1000000;
		cin >> k;
		for (int i = 0; i < k; i++)
		{
			for (int j = 0; j <= i; j++) cin >> a[i][j];
			l[i] = i + 1;
		}
		for (int i = k - 1; i > 0; i--)
		{
			for (int j = 0; j < i; j++) cin >> a[2 * k - i - 1][j];
			l[2 * k - i - 1] = i;
		} 
		
		for (int i = 0 ; i < 2 * k - 1; i++)
			for (int j = 0; j < l[i]; j++) b[i][j] = a[i][j];
		int pp = 2 * k;
		
		for (int i = 0; i < 2 * k - 1; i++)
		{
			int p = labs(i - k + 1);
			int o = 0;
			
			for (int j = 0; j < i; j++)
			{
				int jj = i * 2 - j;
				if ((jj >= 0) && (jj < 2 * k - 1))
				{
					ll = l[j];
					if (l[jj] < ll) ll = l[jj];
				
				
				for (int u = 0; u < ll ; u++)
				{
					int x,y;
					x = (l[j] - ll) / 2 +u;
					y = (l[jj] - ll) / 2 +u;
					if (a[j][x] != a[jj][y]) {o = 1;}
				}
				}
			}  
			if (o ==0) aa[p] = 1;
			if ((o == 0) && (p < pp)) pp = p;
		}
		int s[100];
		for (int i = 0; i < 2 * k - 1; i++) s[i] = l[i];
		for (int i = 0 ; i < 2 * k - 1; i++)
		{
			int x,y;
			x = k - 1 - i;
			y = k - 1 + i;
			if (x < 0) x = 0;
			if  (y > 2 * k -2) y = 2*k-2;
			int o  =0;
			for (int j = x; j <=y ;j++)
			{
				if ((s[j] !=0)&&(((j - k +1+10000 )%2)== (i % 2)))
				{
					a[i][o] = b[j][s[j] - 1];
					s[j] --;
					o++;
				} 
				
			}
		}
		int qq = 2 * k;
		for (int i = 0; i < 2 * k - 1; i++)
		{
			int q = labs(i - k + 1);
			int o = 0;
			for (int j = 0; j < i; j++)
			{
				int jj = i * 2 - j;
				if ((jj >= 0) && (jj < 2 * k - 1))
				{
				 ll = l[j];
					if (l[jj] < ll) ll = l[jj];
				
				for (int u = 0; u < ll ; u++)
				{
					int x,y;
					x = (l[j] - ll) / 2 +u;
					y = (l[jj] - ll) / 2 +u;
					if (a[j][x] != a[jj][y]) o = 1;
				}
				}
			}  
			if ((o == 0) && (q < qq)) qq = q;
			if (o == 0) bb[q] = 1;
		}
	
		ans  = (k+pp+qq)*(k+pp+qq) -k*k;
		cout << "Case #" << T+1 << ": " << ans << endl; 
	}
}
