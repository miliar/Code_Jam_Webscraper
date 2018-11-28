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
#include <climits>

using namespace std;

#define PB push_back
#define MP make_pair
#define two(a) (1 << (a))
#define contain(a, b) (((a) & two(b)) != 0)
#define lowbit(a) ((a) & -(a))

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIP;

bool r[100][100];

bool check(int a, int b)
{
	if(a < 0 || b < 0) return false;
	return r[a][b];
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int tCase;
	cin >> tCase;
	for(int ncase = 1; ncase <= tCase; ncase++)
	{
		int R, ct = 0;
		cin >> R;
		while(R--)
		{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			x1--, x2--, y1--, y2--;
			//for(int i = y1; i <= y2; i++) s[ct++] = PIP(i, PII(x1, x2));
			for(int i = y1; i <= y2; i++) for(int j = x1; j <= x2; j++)
				r[i][j] = true;
		}
		
		int rt = 0;
		bool flag = true;
		while(flag)
		{
			rt++;
			flag = false;
			for(int i = 99; i >= 0; i--)
				for(int j = 99; j >= 0; j--)
				{
					if(check(i, j)) flag = true;
					if(check(i - 1, j) && check(i, j - 1)) r[i][j] = true;
					if(!check(i - 1, j) && !check(i, j - 1)) r[i][j] = false; 
				}
		}
		
		cout << "Case #" << ncase << ": " << --rt << endl;
	}
	return 0;
}