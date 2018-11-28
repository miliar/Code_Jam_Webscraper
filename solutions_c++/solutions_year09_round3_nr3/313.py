#include <iostream>

bool mark[8], pa[128];
int qa[8], p, q;
int min;
void init()
{
	int i, l = sizeof(pa);
	for(i=1;i<=p;i++)
		pa[i]=true;
	pa[p+1] = false;

	for(i=0;i<8;i++)
		mark[i] = false;
	min = 1e9;
}
int check(int pos)
{
	int count=0;
	int i=pos-1;
	while(pa[i])count++, i--;
	i=pos+1;
	while(pa[i])count++, i++;
	return count;
}
void dfs(int layer, int sum)
{
	if(layer == q)
	{
		if(sum<min)min = sum;
	}
	for(int i=0;i<q;i++)
	if(!mark[i]){
		mark[i] = true;
		pa[qa[i]] = false;
		dfs(layer+1,check(qa[i])+sum);
		pa[qa[i]] = true;
		mark[i] = false;
	}
}
void solve()
{
	int i, j;
	scanf("%d%d", &p, &q);
	init();
	for(i=0;i<q;i++)
		scanf("%d", qa+i);
	dfs(0, 0);
	printf("%d\n", min);
	return;
}
int main()
{
	int ncase, icase;
	freopen("test.in", "r+", stdin);
	freopen("test.out", "w+", stdout);
	scanf("%d", &ncase);
	for(icase = 1;icase<=ncase;icase++)
	{
		printf("Case #%d: ", icase);
		solve();
	}
	return 0;
}