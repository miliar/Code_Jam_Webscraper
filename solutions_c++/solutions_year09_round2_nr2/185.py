#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<algorithm>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

int main()
{
	int i, T, cas;
	char s[100], ans[100];
	scanf("%d", &T);
	//freopen("B.in", "r", stdin);
	//freopen("B.out", "w", stdout);
	rep(cas,T)
	{
		scanf("%s", s);
		if(next_permutation(s, s+strlen(s)))
		{
			strcpy(ans, s);
		}
		else {
			ans[0] = s[0];
			ans[1] = '0';
			for(i = 1; s[i] != '\0'; i ++)
			{
				ans[i+1] = s[i];
			}
			ans[i+1] = '\0';
			if(ans[0] == '0')
			{
				for(i = 1; ans[i] == '0'; i ++);
				ans[0] = ans[i];
				ans[i] = '0';
				//puts(ans);
			}
		}
		printf("Case #%d: %s\n", cas+1, ans);
	}
	return 0;
}
