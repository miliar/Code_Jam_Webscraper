#include <iostream>
using namespace std;

const int MOD = 10007;
const int MAXR = 10;
const int MAXV = 200;

int r[MAXR+2], c[MAXR+2];
int ans[MAXR+2][MAXR+2];
int R, H, W;
int comb[MAXV+1][MAXV+1];

void read()
{
	r[0] = c[0] = 1;
	cin >> H >> W >> R;
	for(int i=0; i<R; i++)
		cin >> r[i+1] >> c[i+1];
	r[R+1] = H, c[R+1] = W;
}

inline bool inRange(int a, int b, int x)
{
	return (r[x] < r[b] && r[x] > r[a] && c[x] < c[b] && c[x] > c[a]);
}

inline void myMinus(int &a, int b)
{
	a = ((a-b)%MOD+MOD)%MOD;
}

inline void plus(int &a, int b)
{
	a = (a+b)%MOD;
}

inline int calc(int a, int b)
{
	int h = r[b]-r[a], w = c[b]-c[a];
	int p = (2*h-w), q = (2*w-h);
	if (p < 0 || q < 0 || p%3 || q %3)
		return 0;
	p /= 3, q /= 3;
	return comb[p+q][p];
}

int getAns(int a, int b)
{
	if (ans[a][b] == -1)
	{
		ans[a][b] = calc(a, b);
		for(int i=1; i<=R; i++)
			if (inRange(a, b, i))
			{
				int temp = (((long long)getAns(a, i)*calc(i, b))%MOD);
				myMinus(ans[a][b], temp);
			}
	}
	return ans[a][b];
}

void work()
{
	read();
	memset(ans, -1, sizeof(ans));
	cout << getAns(0, R+1) << endl;
}

void calcComb()
{
	memset(comb, 0, sizeof(comb));
	for(int i=0; i<=MAXV; i++)
	{
		comb[i][0] = 1;
		for(int j=1; j<=i; j++)
			comb[i][j] = (comb[i-1][j]+comb[i-1][j-1])%MOD;
	}
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("d.out", "w", stdout);
	calcComb();
	int T;
	cin >> T;
	for(int testCase=0; testCase<T; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
