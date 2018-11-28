#include <iostream>

using namespace std;

const int MAX_N = 104;
const int MAX_K = 30;

int p[MAX_N][MAX_K];
bool a[MAX_N][MAX_N];
int matchX[MAX_N], matchY[MAX_N], trace[MAX_N], queue[MAX_N];
int n, k, front, rear, finish, res;

void enter()
{
	cin >> n >> k;
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= k; ++j)
			cin >> p[i][j];
}

bool ac(int i, int j)
{
	for (int t = 1; t <= k; ++t)
		if (p[i][t] >= p[j][t]) return false;
	return true;
}

void init()
{
	memset(a, false, sizeof(a));
	
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			if (ac(i, j)) a[i][j] = true;
			
	memset(matchX, 0, sizeof(matchX));
	memset(matchY, 0, sizeof(matchY));
}

void findAugmentingPath(int s)
{
	finish = 0;
	front = rear = 1;
	queue[1] = s;
	memset(trace, 0, sizeof(trace));
	while (front <= rear)
	{
		int i = queue[front++];
		for (int j = 1; j <= n; ++j)
			if (trace[j] == 0 && a[i][j] && matchY[j] != i)
			{
				trace[j] = i;
				if (matchY[j] == 0)
				{
					finish = j;
					return;
				}
				queue[++rear] = matchY[j];
			}
	}
}

void enlarge()
{
	while (finish > 0)
	{
		int x = trace[finish];
		int next = matchX[x];
		matchX[x] = finish;
		matchY[finish] = x;
		finish = next;
	}
}

void solve()
{
	init();
	res = 0;
	for (int i = 1; i <= n; ++i)
	{
		findAugmentingPath(i);
		if (finish)
		{
			++res;
			enlarge();
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int run = 1; run <= T; ++run)
	{
		enter();
		solve();
		
		cout << "Case #" << run << ": " << n - res << endl;
	}
	
	return 0;
}
