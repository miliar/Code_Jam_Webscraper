#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<complex>
#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>


using namespace std;

char s[120][120];
int n,m;

int go[120][120];
int main()
{
	freopen("C:\\GGGG\\ooo.txt","w",stdout);
	int i,j,k;
	int c,h,g;
	scanf("%d",&h);
	for (c=1;c<=h;c++)
	{
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
		{
			scanf("%s",s[i]);
		}
		int oo=1;
		while (oo)
		{
			memset(go,0,sizeof(go));
			oo=0;
			for (i=0;i<n-1;i++)
			{
				for (j=0;j<m-1;j++)
				{
					if (go[i][j]||go[i+1][j]||go[i][j+1]||go[i+1][j+1])continue;
					if (s[i][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j]=='#'&&s[i+1][j+1]=='#')
					{
						go[i][j]=go[i+1][j]=go[i+1][j+1]=go[i][j+1]=1;
						s[i][j]='/';
						s[i][j+1]='\\';
						s[i+1][j]='\\';
						s[i+1][j+1]='/';
						oo=1;
					}
				}
			}
		}
		oo=1;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (s[i][j]=='#')oo=0;
			}
		}
		printf("Case #%d:\n",c);
		if (oo==0)
		{
			printf("%s\n","Impossible");
			continue;
		}
		for (i=0;i<n;i++)
		{
			printf("%s\n",s[i]);
		}
	}
	return 0;
}
			
						
	
