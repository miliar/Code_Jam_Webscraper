//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <stdio.h>
#include <string>
#include <memory.h>

using namespace std;

#define ldb long double
#define LL long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int INF = 1000 * 1000 * 1000;
const LL INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

char mp[100][100];
bool bad[100][100];
string s;
int n;

void Load()
{          
	memset (mp, 0, sizeof (mp));
	memset (bad, 0, sizeof (bad));

	int c;
	cin >> c;
	for (int i = 0; i < c; i++)
	{
		cin >> s;
		mp[s[0]][s[1]] = s[2];
		mp[s[1]][s[0]] = s[2];
	}
	cin >> c;
	for (int i = 0; i < c; i++)
	{
		cin >> s;
		bad[s[0]][s[1]] = 1;
		bad[s[1]][s[0]] = 1;
	}
	cin >> n >> s;
}

void Solve()
{
	vector <char> ans;
	ans.push_back(s[0]);
	for (int i = 1; i < n; i++)
	{
		ans.push_back(s[i]);
		int j = ans.size() - 2;
		while (j >= 0)
		{
			if (mp[ans[j]][ans[j + 1]] != 0)			
			{
				ans.pop_back();
				ans[j] = mp[ans[j]][ans[j + 1]];
				j--;
			}
			else
				break;
		}
		for (int j = 0; j < (int)ans.size(); j++)
			for (int k = j + 1; k < (int)ans.size(); k++)
				if (bad[ans[j]][ans[k]])
				{
					ans.clear();
					j = 1000000;
					break;
				}
	}
	cout << "[";
	for (int i =0; i < (int)ans.size() - 1; i++)
		cout << ans[i] << ", ";
	if (!ans.empty())
		cout << ans.back() << "]\n";
	else
		cout << "]\n";
}
                
int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int t, T;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		Load();
		Solve();
	}
	return 0;
	return 0;
}
