#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int cn=1,L,n,m;
char s[5005][20],tt[10000];
bool hs[23][27];

bool check(int x)
{
	for(int i=0;s[x][i];i++)
	{
		if(!hs[i][s[x][i]-'a']) return 0;
	}
	return 1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-out.txt", "w", stdout);
	int i,j;
	scanf("%d%d%d",&L,&n,&m);
	for(i=0;i<n;i++){
		scanf("%s",s[i]);
	}
	for(i=1;i<=m;i++)
	{
		scanf("%s",tt);
		memset(hs,0,sizeof(hs));
		int pn = 0;
		for(j=0;tt[j];j++){
			if(tt[j]=='(')
			{
				int k = j+1;
				while(tt[k] != ')')
				{
					hs[pn][tt[k++]-'a'] = 1;
				}
				j = k;
				pn++;
			}
			else if(tt[j]>='a' && tt[j]<='z')
			{
				hs[pn][tt[j]-'a'] = 1;
				pn++;
			}
		}
		int ans = 0;
		for(j=0;j<n;j++)
		{
			if(check(j))
				ans++;
		}
		printf("Case #%d: %d\n",cn++,ans);
	}
}
