#include <iostream>
using namespace std;

const int MAXM = 10000;

int M, V;
int changeable[MAXM+1];//from 1
int value[MAXM+1];//0 OR
int ans[MAXM+1][2];

void read()
{
	cin >> M >> V;
	memset(changeable, -1, sizeof(changeable));
	for(int i=1; i<=(M-1)/2; i++)
		cin >> value[i] >> changeable[i];
	for(int i=(M-1)/2+1; i<=M; i++)
		cin >> value[i];
}

inline void update(int *a, int p, int q, int l, int r, int nowType, int change)
{
	if (p == -1 || q == -1)
		return;
	int nowValue;
	if (nowType == 0)
		nowValue = (l | r);
	else
		nowValue = (l & r);
	if (a[nowValue] == -1 || a[nowValue] > p+q+change)
		a[nowValue] = p+q+change;
}

void work()
{
	read();
	memset(ans, -1, sizeof(ans));
	for(int i=M; i>=1; i--)
		if (changeable[i] == -1)
			ans[i][value[i]] = 0;
		else
		{
			for(int change=0; change<2; change++)
				if (!change || changeable[i])
				{
					int nowType = change^value[i];
					for(int l=0; l<2; l++)
						for(int r=0; r<2; r++)
							update(ans[i], ans[i*2][l], ans[i*2+1][r], l, r, nowType, change);
				}
		}

	if (ans[1][V] == -1)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans[1][V] << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int nOfTest;
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
