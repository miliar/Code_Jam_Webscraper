#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int map[20][20];
int R, C;
char solution;
int dx[] = {-1, -1,  0,  1, 1, 1, 0, -1};
int dy[] = { 0, -1, -1, -1, 0, 1, 1,  1};
bool dfs(int x, int y)
{
	int nx, ny;
	for(int i =0 ; i < 8;i++)
	{
		nx = x + dx[i];
		ny = y + dy[i];
		if(map[nx][ny] == 0)
		{
			map[nx][ny] = 1;
			if(dfs(nx, ny) == false) {
				map[nx][ny] = 0;
				return true;
			}
			map[nx][ny] = 0;
		}
	}
	return false;
}
void solve(int kx, int ky)
{
	if(dfs(kx, ky) == true)
	{
		solution = 'A';
	}
	else
	{
		solution = 'B';
	}
}

int main()
{
	ifstream fin("problem4.in");
	ofstream fout("problem4.out");

	int CC;
	int kx, ky;
	string t;
	fin >> CC;
	for(int c = 1; c <= CC; c++)
	{
		fout << "Case #" << c << ": ";
		fin >> R >> C;
		for(int i = 0; i < R; i++)
		{
			fin >> t;
			for(int j = 0; j < C; j++)
			{
				if(t[j] == '#') map[i + 1][j + 1] = 1;
				else if(t[j] == '.') map[i + 1][j + 1] = 0;
				else {
					map[i + 1][j + 1] = 1;
					kx = i + 1;
					ky = j + 1;
				}
			}
		}
		for(int i = 0; i <= R + 1; i++) map[i][0] = map[i][C + 1] = 1;
		for(int i = 0; i <= C + 1; i++) map[0][i] = map[R + 1][i] = 1;
		solve(kx, ky);
		fout << solution << endl;
	}
	return 0;
}