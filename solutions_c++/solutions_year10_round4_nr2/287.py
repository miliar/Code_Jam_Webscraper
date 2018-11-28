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

int m[2000];
int ss[2000];
long long f[3000][13];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	cin >> t;
	for (int T = 0; T < t; T++)
	{
		int p;
		cin >> p;
		int s = 1;
		for (int i = 0; i < p; i++ ) s = s * 2;
		for (int i = 0; i < 2050; i++)
		for (int j = 0; j <= 12; j++)
		f[i][j] = 1000000005;
		for (int i = s -1 ; i >=0 ; i--) cin >> ss[i];
		for (int i = 0; i < s; i++)
		{
			int x = ss[i];
			if (ss[i] > p) x = p;
			for (int j = 0; j <= x; j++) f[i+s-1][j] =0; 
		}
		for (int i = s-2; i >= 0;i--) 
		{
			cin >> m[i];
			int x  = i * 2 + 1;
			int y = i * 2 +2;
			for (int j = p ; j >=0; j--)
			{
				if (j ==p) f[i][j] = 1000000005; else f[i][j] = f[i][j+1];
				if (f[i][j] > f[x][j+1]+f[y][j+1]) f[i][j] = f[x][j+1]+f[y][j+1];
				if (f[i][j] > f[x][j] + f[y][j] + m[i]) f[i][j] = f[x][j]+f[y][j] +m[i];
			}
		}
		cout << "Case #" << T+1 << ": " << f[0][0] << endl;
		
	}
}
