#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int dx[3] = { 1, 0, 1 };
int dy[3] = { 0, 1, 1 };
int R, C;

bool oor(int x, int y)
{
	return x<0||x>=C||y<0||y>=R;
}

int main()
{
	int T;
	cin >> T;
	for (int X=1; X<=T; X++)
	{
		cin >> R >> C;
		string map[R];
		for (int i=0; i<R; i++)
			cin >> map[i];

		cout << "tmp\n";

		for (int y=0; y<R; y++)
		for (int x=0; x<C; x++)
		{
			if (map[y][x]!='#') continue;
			int x1=x+dx[0], x2=x+dx[1], x3=x+dx[2];
			int y1=y+dy[0], y2=y+dy[1], y3=y+dy[2];
			if (oor(x1, y1) || oor(x2, y2) || oor(x3, y3)) continue;
			if (map[y1][x1]=='#' && map[y2][x2]=='#' && map[y3][x3]=='#')
			{
				map[y][x] = map[y3][x3] = '/';
				map[y1][x1] = map[y2][x2] = '\\';
			}
		}

		bool f = true;
		for (int y=0; y<R; y++)
		for (int x=0; x<C; x++)
			if (map[y][x] == '#')
			{
				f = false; break;
			}

		cout << "Case #" << X << ':' << endl;
		if (f)
		{
			for (int i=0; i<R; i++)
				cout << map[i] << endl;
		}
		else
		{
			cout << "Impossible" << endl;
		}

	}
	return 0;
}