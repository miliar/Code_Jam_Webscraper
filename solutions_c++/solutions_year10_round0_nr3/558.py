#include<iostream>
using namespace std;

const int maxn = 1000 + 10;
int r, k, n;
int a[maxn];
int lastTime[maxn], next[maxn];
long long lastMoney[maxn], Sum[maxn];
int mark[maxn];

void precount()
{
	for (int i = 0; i < n; i++)
	{
		long long sum = 0;
		next[i] = i; Sum[i] = 0;
		for (int j = 0; j < n; j++)
		{
			sum += a[(i + j) < n ? i + j : i + j - n];
			if (sum > k) { next[i] = i + j < n ? i + j : i + j - n; break; }
			Sum[i] = sum;
		}
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; i++)	scanf("%d", &a[i]);
		precount();
		int curp = 0, curt = 0;
		long long ans = 0;
		memset(mark, 0, sizeof(mark));
		while (curt < r)
		{
			
			if (mark[curp] == 0)
			{
				lastTime[curp] = curt;
				lastMoney[curp] = ans;
				mark[curp] = 1;
			}	else
			if (mark[curp] == 1)
			{
				lastTime[curp] = curt - lastTime[curp];
				lastMoney[curp] = ans - lastMoney[curp];
				mark[curp] = 2;
			}
			if (mark[curp] == 2)
			{
				if (r - curt >= lastTime[curp])
				{
					int tmp = (r - curt) / lastTime[curp];
					curt += tmp * lastTime[curp];
					ans += tmp * lastMoney[curp];
					continue;
				}
			}
			
			curt++;
			ans += Sum[curp];
			curp = next[curp];
		}		
		cout << ans << endl;
	}
}