#include<vector>
#include<iostream>
#include<algorithm>

const int Max = 101;
using namespace std;

int T, H, W;
char cur = 'a' - 1;
char Res[Max][Max];
int Field[Max][Max];

bool inRange(int i, int j)
{
	if ((i >= 0) && (j >= 0))
		if ((i < H) && (j < W))
			return true;
	return false;
}

char mark(int i, int j)
{
	vector<pair<int, int>> v;
	if (Res[i][j] != '*') return Res[i][j];
	if (inRange(i - 1, j))
		v.push_back(pair<int, int>(Field[i - 1][j], 1));
	if (inRange(i, j - 1))
		v.push_back(pair<int, int>(Field[i][j - 1], 2));
	if (inRange(i, j + 1))
		v.push_back(pair<int, int>(Field[i][j + 1], 3));
	if (inRange(i + 1, j))
		v.push_back(pair<int, int>(Field[i + 1][j], 4));
	sort(v.begin(), v.end());
	if (v.empty())
	{ cur++; Res[i][j] = cur; return Res[i][j]; }
	if (v[0].first >= Field[i][j])
	{ cur++; Res[i][j] = cur; return Res[i][j]; }
	switch (v[0].second)
	{
	case 1: 
		Res[i][j] = mark(i - 1, j);
		return Res[i][j];
	case 2: 
		Res[i][j] = mark(i, j - 1);
		return Res[i][j];
	case 3: 
		Res[i][j] = mark(i, j + 1);
		return Res[i][j];
	case 4: 
		Res[i][j] = mark(i + 1, j);
		return Res[i][j];
	}
	for(int i = 0; i < H; i++)
	{
		for(int j = 0; j < W; j++)
			cout << Res[i][j] << " ";
		cout << endl;
	}
}	

void calc()
{
	cur = 'a' - 1;
	for(int i = 0; i < H; i++)
		for(int j = 0; j < W; j++)
			mark(i, j);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	string s;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cin >> H >> W;
		for(int j = 0; j < H; j++)
			for(int k = 0; k < W; k++)
			{
				Res[j][k] = '*';
				cin >> Field[j][k];
			}
		calc();
		cout << "Case #" << i + 1 << ":\n";
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
				cout << Res[j][k] << " ";
			cout << endl;
		}
	}
	return 0;
}