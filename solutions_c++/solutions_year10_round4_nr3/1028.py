#include <iostream>
#include <set>
#include <string>
#include <string.h>
using namespace std;

bool b[256][256];
bool t[256][256];

void Solve()
{
	int r;
	memset(b, 0, sizeof(b));
	cin >> r;
	for(int i = 0; i < r; i++)
	{
		int x1, x2, y1, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		if(x1 > x2)
			swap(x1, x2);
		if(y1 > y2)
			swap(y1, y2);
		for(int i = y1; i <= y2; i++)
			for(int j = x1; j <= x2; j++)
			{
				b[i][j] = 1;
			}
	}
	int cnt = 0;
	while(1)
	{
		bool has = 0;
		for(int i = 0; i < 256; i++)
			for(int j = 0; j < 256; j++)
				if(b[i][j])
				{
					has = 1;
					break;
				}
		if(!has)
			break;
		cnt++;
		memset(t, 0, sizeof(t));
		for(int i = 1; i < 256; i++)
			for(int j = 1; j < 256; j++)
				if(b[i][j] && !b[i - 1][j] && !b[i][j - 1])
					t[i][j] = 0;
				else if(!b[i][j] && b[i - 1][j] && b[i][j - 1])
					t[i][j] = 1;
				else
					t[i][j] = b[i][j];
		memcpy(b, t, sizeof(b));
	}
	cout << cnt << endl;
}

int main()
{
	freopen("d:\\input.in", "r", stdin);
	freopen("d:\\output.out", "w", stdout);
	int T;
	cin >> T;
	for(int tt = 1; tt <= T; tt++)
	{
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}