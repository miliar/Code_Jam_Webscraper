#include <stdio.h>
#include <cstring>
#define maxlen 1010
#define maxk 20
using namespace std;
int k,ans,L;
int now[maxk];
bool used[maxk];
char s[maxlen];
char f[maxlen];
void readin(void)
{
	scanf("%d",&k);
	scanf("%s",&s);
	L = strlen(s);
}
void calc(void)
{
	for (int i = 0;i < L;i++)
	{
		int poi = now[i % k + 1];
		f[i] = s[i / k * k + poi - 1];
	}
	int temp = 1;
	for (int i = 1;i < L;i++) if (f[i] != f[i - 1]) temp++;
	if (ans > temp) ans = temp;
}
void dfs(int step)
{
	if (step > k)
	{
		calc();
		return;
	}
	for (int i = 1;i <= k;i++) if (!used[i])
	{
		used[i] = true;
		now[step] = i;
		dfs(step + 1);
		now[step] = 0;
		used[i] = false;
	}
}
void work(void)
{
	memset(used,false,sizeof(used));
	ans = L;
	dfs(1);
}
int main(void)
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int n;
	scanf("%d",&n);
	for (int cases = 1;cases <= n;cases++)
	{
		readin();
		work();
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}
