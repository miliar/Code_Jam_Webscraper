#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("D-small-attempt0.in");
ofstream fout("d.out");

const int maxs = 65536 + 10;
const int maxr = 4;
const int maxc = 4;
const int dx[8] = {-1, -1, -1,0,0,1,1,1};
const int dy[8] = {1,0,-1,1,-1,-1,0,1};
int t[maxr][maxc][maxs], two[maxr * maxc + 5], r, c;
char s[maxr + 5][maxc + 5];

void check(int st, int x, int y)
{
	int i,nx,ny,nst;
	for (i = 0;i < 8;i ++)
	{
		nx = dx[i] + x;
		ny = dy[i] + y;
		if (nx >= 0 && nx < r && ny >= 0 && ny < c && ((two[nx * c + ny] & st) == 0)) {
			nst = two[nx * c + ny] + st;
			if (t[nx][ny][nst] == 0)
				check(nst, nx,ny);
			//cout << nx << " " << ny <<" " << nst << " " << t[nx][ny][nst] << endl;
			if (t[nx][ny][nst] == -1) {
				t[x][y][st] = 1;
				return;
			}
			
		}
	}
	t[x][y][st] = -1;	
}

int main()
{
	int i,j,k,n, x, y, st;
	cin >> n;
	for (i = 0;i < maxr * maxc + 2;i ++)
		two[i] = (2 << i);
	for (k = 1;k <= n;k ++)
	{
		cin >> r >> c;
		memset(t, 0, sizeof(t));
		for (i = 0;i < r;i ++)
			cin >> s[i];	
		st = 0;
		for (i = 0;i < r;i ++)
			for (j = 0;j < c;j ++)
				if (s[i][j] == 'K') {
					x = i;
					y = j;
					st += two[i * c + j];
				} else 
					if (s[i][j] == '#') {
						st += two[i * c + j];
					}
		check(st, x, y);
		cout << "Case #" << k << ": ";
		if (t[x][y][st] == -1)
			cout << "B" << endl;
		else cout << "A" << endl;
	}
    return 0;
}
