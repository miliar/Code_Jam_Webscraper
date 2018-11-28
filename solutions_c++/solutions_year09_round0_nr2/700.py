#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <ctime>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define sz(x) ((int)(x).size())
#define init(st) memset(st, 0, sizeof(st)) 
#define ll long long

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int arr[101][101];
char dp[101][101];
int dy[] = {-1, 0, 0, 1};
int dx[] = {0, -1, 1, 0};
int H,W;

bool inside(int r, int c)
{
	return (r >= 0 && c >= 0 && r < H && c < W);
}

char go(int r, int c, char cur)
{
	if(dp[r][c])
		return dp[r][c];

	int index = -1;
	int value = arr[r][c];
	for(int i = 0; i < 4; i++)
	{
		int nr = r + dy[i];
		int nc = c + dx[i];

		if(!inside(nr,nc))
			continue;

		if(arr[nr][nc] < value)
		{
			value = arr[nr][nc];
			index = i;
		}
	}

	if(index == -1)
		return dp[r][c] = cur;
	return dp[r][c] = go(r+dy[index], c + dx[index], cur);
}

void show()
{
	for(int i = 0; i < H; i++)
	{
		for(int j = 0; j < W; j++)
			cout << dp[i][j] << " ";
		cout << "\n";
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T;
	cin >> T;

	for(int q = 0; q < T; q++)
	{
		cin >> H >> W;
		init(arr);
		init(dp);
		for(int i = 0; i < H; i++)
			for(int j = 0; j < W; j++)
				cin >> arr[i][j];
		
		char cur = 'a';
		for(int i = 0; i < H; i++)
			for(int j = 0; j < W; j++)
				if(!dp[i][j])
				{
					if(go(i,j,cur) == cur)
						cur++;
				}
		
		printf("Case #%d:\n", q + 1);
		show();
	}

	return 0;
}