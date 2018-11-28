#pragma warning( disable : 4786 )
#include<stdio.h>
#include<string.h>
#include<string>
#include<map>

using namespace std;
char str[105], tmp[105];

map<string,int> S;

int main()
{
	int t,n,m,i,j,k,res,cnt,len,cas=1;


	//freopen("A-large(2).in","r",stdin);
	//freopen("A-large(2).txt","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		res = 0;
		cnt = 0;
		S.clear();
		scanf("%d%d",&n,&m);
		getchar();

		for(i=1; i<=n; i++)
		{
			gets(str);
			S[str]=1;
		}

		for(i=1; i<=m; i++)
		{
			gets(str);

			len = strlen(str);
			tmp[0] = '/';

			for(j=1,k=1; j<=len; j++)
			{
				if(str[j] == '/' || str[j] == '\0')
				{
					//cnt++;
					tmp[k] = '\0';

					if(S[tmp] == 0)
					{
						S[tmp] = 1;
						res++;
					}
				}
				tmp[k] = str[j];
				k++;
			
			}
		}

		printf("Case #%d: %d\n",cas++,res);
	}
	return 0;
}