#include<iostream>

using namespace std;
int x[805],y[805],n,res;
bool flag[805];
void dfs(int len,int mult)
{
	if(len==n)
	{
		if(mult<res)
			res = mult;
		return ;
	}
	int i;
	for(i=0;i<n;i++)
		if(!flag[i])
		{
			flag[i] = 1;
			dfs(len+1,mult+x[len]*y[i]);
			flag[i] = 0;
		}
}
int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int cas,ca=1;
	cin>>cas;
	while(cas--)
	{
		cin>>n;
		int i;
		for(i=0;i<n;i++)
			scanf("%d",x+i);
		for(i=0;i<n;i++)
			scanf("%d",y+i);
		res = 0x7fffffff;
		dfs(0,0);
		printf("Case #%d: %d\n",ca++,res);
	}
	return 0;
}