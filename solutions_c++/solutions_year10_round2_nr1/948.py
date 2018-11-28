#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<map>
#include<cstring>
#include<string>

using namespace std;

map<string,bool> M;
char s[110];

int main()
{
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);

	int T;
	scanf("%d",&T);
	for (int t=0; t<T; t++)
	{
		M.clear();
		int n,m;
		scanf("%d%d\n",&n,&m);

		int ans=0;
		for (int i=0; i<n; i++)
		{
			gets(s);
			M[s]=1;
		}

		for (int i=0; i<m; i++)
		{
			gets(s);
			int l=strlen(s)-1;

			while (1)
			{
				if (M[s]==1 || l==0) break;
				M[s]=1;
				ans++;
				while (s[l]!='/') l--;
				s[l]='\0';
			}
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
}