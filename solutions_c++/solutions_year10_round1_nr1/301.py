#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <map>
#include <climits>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <set>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<int, LL> PIL;
typedef pair<PII, PII> SEG;

#define lowbit(a) ((a) & (-a))
#define two(a) (1 << (a))
#define left(a) (((a) <<1) + 1)
#define right(a) (left(a) + 1)

int n, k;
vector<string> board, b;
void getData()
{
	board.clear();
	cin >> n >> k;
	for(int i = 0; i < n; i++)
	{
		string str;
		cin >> str;
		board.push_back(str);
	}
}

void updata()
{
	bool flag = true;
	while(flag)
	{
		flag = false;
		for(int i = n - 2; i >= 0; i--)
			for(int j = 0; j < n; j++) if(b[i + 1][j] == '.' && b[i][j] != '.')
			{
				flag = true;
				swap(b[i][j], b[i + 1][j]);
			}
	}
}

string solve()
{
	b.clear();
	b.resize(n, "");
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			b[i].push_back(board[j][i]);
	for(int i = 0; i < n; i++) reverse(b[i].begin(), b[i].end());

	updata();

	int stat = 0;

	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++) if(b[i][j] != '.')
		{
			bool flag = true;
			for(int m = 0; m < k; m++) if(j + m >= n || b[i][j + m] != b[i][j])
			{
				flag = false;
				break;
			}
			if(flag) stat |= b[i][j] == 'R' ? 1: 2;

			flag = true;
			for(int m = 0; m < k; m++) if(i + m >= n || b[i + m][j] != b[i][j])
			{
				flag = false;
				break;
			}
			if(flag) stat |= b[i][j] == 'R' ? 1: 2;

			flag = true;
			for(int m = 0; m < k; m++) if(i + m >= n || j + m >= n || b[i + m][j + m] != b[i][j])
			{
				flag = false;
				break;
			}
			if(flag) stat |= b[i][j] == 'R' ? 1: 2;

			flag = true;
			for(int m = 0; m < k; m++) if(i + m >= n || j - m < 0 || b[i + m][j - m] != b[i][j])
			{
				flag = false;
				break;
			}
			if(flag) stat |= b[i][j] == 'R' ? 1: 2;
		}
	if(stat == 0) return "Neither";
	if(stat == 1) return "Red";
	if(stat == 2) return "Blue";
	return "Both";
}

int main()
{
	freopen("a1.in", "r", stdin);
	freopen("a1.out", "w", stdout);

	int t;
	cin >> t;
	for(int nc = 1; nc <= t; nc++)
	{
		getData();
		cout << "Case #" << nc << ": " << solve() << endl;
	}
	return 0;
}
