#include<cstdio>
#include<string>
#include<cstring>

using namespace std;

const int MAXN = 502;
int dp[MAXN][MAXN];
int n, m;
const string model = "welcome to code jam";
char line[MAXN];

int go(int s, int t)
{
	if(s == n) 
		return 1;
	if(t == m)
		return 0;

	int & res = dp[s][t];
	if(res>=0)
		return res;
	
	res = 0;

	if(model[s] == line[t])
	{
		res = (res + go(s+1, t+1)) % 10000;
	}

	res = (res + go(s, t+1)) % 10000;

	return res;
}
void init()
{
	memset(dp, -1, sizeof(dp));
}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	n=model.length();

	int numCase;
	scanf("%d", &numCase);
	getchar();
	for(int c=0; c<numCase; c++)
	{
		init();
		gets(line);
		m = strlen(line);

		int res = go(0,0);
		printf("Case #%d: %04d\n", c+1, res);
	}
}