#include <stdio.h>

const int infty = 10000000;

int one[3000];
int zeroCount[3000];
bool isOne[3000][3000];
bool isZero[3000][3000];
int state[3000];
bool pushed[3000];

class stack
{
public:
	int ar[3000];
	int size;
	void clear()
	{
		size = 0;
	}
	void push(int a)
	{
		if (pushed[a])
			return;
		pushed[a] = true;
		ar[++size] = a;
	}
	void pop()
	{
		size--;
	}
	int top()
	{
		return ar[size];
	}
	bool empty()
	{
		return size == 0;
	}
} st;

void solve(int test_case)
{
	int n,m;
	scanf("%d%d", &m, &n);
	for(int i = 0; i < m; i++)
		state[i] = 0;
	for(int i = 0; i < n; i++)
	{
		one[i] = -1;
		zeroCount[i] = 0;
		for(int j = 0; j < m; j++)
			isOne[i][j] = isZero[i][j] = false;
		pushed[i] = false;
	}
	for(int i = 0; i < n; i++)
	{
		int k;
		scanf("%d", &k);
		for(int j = 0; j < k; j++)
		{
			int d, flag;
			scanf("%d%d", &d, &flag);
				if (flag == 0)
				{
					isZero[i][d-1] = true;
					zeroCount[i] ++;
				}
				else
				{
					isOne[i][d-1] = true;
					one[i] = d - 1;
				}
		}
	}
	st.clear();
	for(int i = 0; i < n; i++)
	{
		if (zeroCount[i] == 0)
			st.push(i);
	}
	bool answer = true;
	while(!st.empty())
	{
		int cur = st.top();
		st.pop();
		if (zeroCount[cur] > 0)
			continue;
		if (one[cur] == -1)
		{
			answer = false;
			break;
		}
		int curOne = one[cur];
		state[curOne] = 1;
		zeroCount[cur] = infty;
		for(int i = 0; i < n; i++)
		{
			if (isZero[i][curOne])
				zeroCount[i]--;
			if (isOne[i][curOne])
				zeroCount[i] = infty;
			if (zeroCount[i] == 0)
				st.push(i);
		}
	}

	printf("Case #%d: ", test_case);
	if (!answer)
		printf("IMPOSSIBLE\n");
	else
	{
		for(int i = 0; i < m; i++)
			printf("%d ", state[i]);
		printf("\n");
	}

	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
