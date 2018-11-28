#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <bitset>
#include <algorithm>
#include <sstream>
using namespace std;

const double pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679;
const int mod = 1000000007;
const int maxn = 10010;

int T, n, dist;
int d[maxn];
int md[maxn];
int l[maxn];
bool check[maxn];

void init()
{
	scanf("%d", &n);
	for (int i=0; i<n; i++)
		scanf("%d%d", &d[i], &l[i]);
	scanf("%d", &dist);
}

string work()
{
	memset(check, 0, sizeof(check));
	memset(md, 0, sizeof(md));
	check[0] = true;
	md[0] = min(l[0], d[0]);
	for (int i=0; i<n; i++)
		if (check[i])
		{
			for (int j=i+1; j<n; j++)
				if (d[j]-d[i]<=md[i])
				{
					if (d[j]-d[i]<=l[j])
						md[j] = max(d[j]-d[i], md[j]);
					else
						md[j] = l[j];
					check[j] = true;
				}
		}
	for (int i=0; i<n; i++)
		if (d[i]+md[i]>=dist && check[i])
			return "YES";
	return "NO";
}

int main(){
	freopen("C:/Users/yaoyao/Downloads/A-large.in", "r", stdin);
	freopen("D:/workspace/Topcoder/Algorithm/Algorithm/out.txt", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++)
	{
		init();
		cout << "Case #" << i << ": " << work() << endl;
	}
	return 0;
}

