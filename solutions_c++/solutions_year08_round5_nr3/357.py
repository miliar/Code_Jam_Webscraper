#include <iostream>
using namespace std;

const int MAXL = 10;

int H, W;
string room[MAXL];
int ans[MAXL][MAXL][1 << (MAXL+1)];

void read()
{
	cin >> H >> W;
	for(int i=0; i<H; i++)
		cin >> room[i];
}

inline int getDigit(int mark, int p)
{
	return (mark & (1 << p));
}

int getAns(int r, int c, int mark)
{
	if (r >= H)
		return 0;
	if (c >= W)
		return getAns(r+1, 0, mark);
	if (ans[r][c][mark] == -1)
	{
		ans[r][c][mark] = getAns(r, c+1, mark/2);
		if (room[r][c] == '.' && !(r > 0 && c > 0 && getDigit(mark, 0)) && !(c > 0 && getDigit(mark, W)) && !(r > 0 && c < W-1 && getDigit(mark, 2)))
			ans[r][c][mark] = max(ans[r][c][mark], 1+getAns(r, c+1, (mark >> 1)|(1 << W))); 
	}
	return ans[r][c][mark];
}

void work()
{
	read();
	memset(ans, -1, sizeof(ans));
	cout << getAns(0, 0, 0) << endl;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	cin >> T;
	for(int testCase=0; testCase<T; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
