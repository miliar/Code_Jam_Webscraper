#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	freopen("d:\\data\\A-large.in","r",stdin);
	freopen("d:\\data\\A-large.out","w",stdout);
	int t,n,m,i,j,c=0;
	char s[105][105],ss[105][105];
	scanf("%d",&t);
	while(t--)
	{
		int x=0,y=0;
		scanf("%d%d",&n,&m);
		//printf("%d %d\n",n,m);//
		for(i=0;i<n;i++)
		{
			scanf("%s",s[i]);
			//printf("%s\n",s[i]);//
			for(j=0;j<m;j++)
				if(s[i][j]=='#')
					x++;
		}
		int f=1;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(s[i][j]=='#')
				{
					s[i][j]='/';
					y++;
					if(j+1<m&&s[i][j+1]=='#')
					{
						s[i][j+1]='\\';
						y++;
					}
					else
						f=0;
					if(i+1<n&&s[i+1][j]=='#')
					{
						s[i+1][j]='\\';
						y++;
					}
					else
						f=0;
					if(i+1<n&&j+1<m&&s[i+1][j+1]=='#')
					{
						s[i+1][j+1]='/';
						y++;
					}
					else
						f=0;
				}
		printf("Case #%d:\n",++c);
		if(!f)
			puts("Impossible");
		else
		{
			for(i=0;i<n;i++)
				puts(s[i]);
		}
	}
}
