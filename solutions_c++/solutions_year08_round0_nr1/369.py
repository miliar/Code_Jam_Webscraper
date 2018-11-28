#include <iostream>
#include <map>
#include <string>
using namespace std;
int s[110],n,m,bw[110];
int dp(int t)
{
	if (t == m) return -1;
	if (bw[t] != -1) return bw[t];
	int mi = 200,tmp,i,j;
	for (i = 0 ; i < n ; i++)
	{
		if (s[t]==i) continue;
		for (j = t ; j < m ; j++)
		{
			if (s[j]==i)
				break;
		}
		tmp = dp(j)+1;
		if (tmp < mi) mi = tmp;
	}
	return bw[t] = mi;
}

int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);
	map<string,int> st;
	int i,ca,T;
	scanf("%d",&T);
	char go[110];
	for (ca = 1 ; ca <= T ; ca++)
	{
		st.clear();
		scanf("%d\n",&n);
		for (i = 0 ; i < n ; i++)
		{
			gets(go);
			st[go]=i;
		}
		scanf("%d\n",&m);
		for (i = 0 ; i < m ; i++)
		{
			bw[i] = -1;
			gets(go);
			s[i] = st[go];
		}
		if (m == 0)
			printf("Case #%d: %d\n",ca,0);
		else
			printf("Case #%d: %d\n",ca,dp(0));
	}
	return 0;
}