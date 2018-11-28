#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

#define MAXN 1002
int t, n;
int c[MAXN];
inline int Rint() {int x; scanf("%d", &x); return x;}
int ans;
int cnt;	//¸ç¸çÊı 
int dfs(int cur, int l, int r)	//	1 ½áÊø	l = ¸ç¸ç
{
	if(cur == n)
	{
		if(l == r) return 1;
		else return 0;
	}
	int t = l;
	if(cur != n-1 || cnt<n-1)	//!!
	{
		l = l^c[cur];
		ans+=c[cur];
		cnt+=1;
		if(dfs(cur+1, l, r)) return 1;
		cnt-=1;
		ans-=c[cur];
	}
	if(cur !=n-1 || cnt != 0)	//!!
	{
		r = r^c[cur];
		if(dfs(cur+1, t, r)) return 1;
	}

	return 0;
}

int cmp(const int& a, const int& b)
{
	return a>=b? 1: 0;
}
int main()
{
	t = Rint();
	for(int i=1; i<=t; i++)
	{
		cnt=0;
		ans=0;
		printf("Case #%d: ", i);
		n = Rint();
		for(int j=0; j<n; j++)
			c[j] = Rint();
		sort(c, c+n, cmp);	//½µĞò
		if(dfs(0, 0, 0))	printf("%d\n", ans);
		else printf("NO\n");
//		solve();
	}
}