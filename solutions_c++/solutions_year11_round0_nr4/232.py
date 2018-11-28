#include<iostream>
using namespace std;
int num[1005];
bool used[1005];
int cnt ;
void dfs(int k)
{
	used[k] = true;
	cnt ++;
	if(!used[num[k]])
		dfs(num[k]);
}

void pre()
{
	double now[3];
	double next[3];
	int i,j;
	memset(now,0,sizeof(now));
	memset(next,0,sizeof(next));
	now[0] = 1.0;
	double ans = 0;
	for( i = 1 ; i <= 100000 ; i ++)
	{
		memset(next,0,sizeof(next));
		next[0] += now[0] /3;
		next[1] += now[0] /2;
		next[2] += now[0] /6;
		next[1] += now[1] /2;
		next[2] += now[1] /2;
		ans += i * next[2];
		for( j = 0 ; j < 3 ; j ++)
			now[j] = next[j];
	}
	cout << ans << endl;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
//	pre();
	int i;
	int t;
	scanf("%d",&t);
	int g = 1;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		int i;
		for( i = 1 ; i <= n ; i ++)
		{
			scanf("%d",&num[i]);
		}
		memset(used,false,sizeof(used));
		int ans = 0 ;

		for( i = 1 ; i <= n ; i ++)
			if(!used[i])
			{
				cnt = 0;
				dfs(i);
				if(cnt != 1)
					ans += cnt;
			}
		printf("Case #%d: %.6lf\n",g++ , ans * 1.0);
	}
	return 0;
}
/*
Case #3: 4.000000
Case #3: 4.000000
*/