#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "D-small-attempt0.in.txt"
#define OUTPUTFILENAME "output.txt"
template<class T> inline void smaller(T &a,T b){if(b<a) a=b;}
template<class T> inline void larger(T &a,T b){if(b>a) a=b;}

const int maxn = 200;
int h, w, r;
int map[maxn][maxn];
int s[maxn][maxn];


void init()
{
	memset(map, 0, sizeof(map));
	cin >> h >> w >> r;
	int x, y;
	for (int i = 0; i < r; i++)
	{
		cin >> x >> y;
		map[x][y] = 1;
	}

}

void solve(int testnumber)
{
	s[1][1] = 1;
	for (int i = 2; i <= h; i++)
		for (int j = 1; j <= w; j++)
			if (map[i][j] == 1)
				s[i][j] = 0;
			else
			{
				s[i][j] = 0;
				if (j >= 3)
					s[i][j] = (s[i][j] + s[i - 1][j - 2]) % 10007;
				if (i >= 3 && j >= 2)
					s[i][j] = (s[i - 2][j - 1] + s[i][j]) % 10007;
			}
	cout << "Case #" << testnumber << ": " << s[h][w] << endl;
}	

int main()
{
	int testnumber;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> testnumber;
	for (int i = 0; i < testnumber; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}