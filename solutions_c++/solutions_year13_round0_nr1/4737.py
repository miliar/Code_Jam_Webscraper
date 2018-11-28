#include <cstdio>
#include <cstring>

using namespace std;

FILE *fin,*fout;
char a[4][4];
char ch,x;
int j;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	scanf("%d", &t);
	ch=getchar();
	for (int ii = 1; ii <= t; ++ii)
	{
		char ans='D';
		bool dot=false;
		memset(a,0,sizeof(a));
		for (int i = 0; i < 4; ++i)
		{
			for (j = 0; j < 4; ++j)
			{
				a[i][j]=getchar();
				if(a[i][j]=='.')
					dot=true;
			}
			ch=getchar();
		}
		/*for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				printf("%c", a[i][j]);
			}
			printf("\n");
		}*/
		printf("Case #%d: ", ii);

		for (int i = 0; i < 4; ++i)
		{
			if(a[i][0]!='T')x=a[i][0];
			else x=a[i][1];		
			if(x!='.')
			{		
				for (j = 0; j < 4; ++j)
				{
					if(a[i][j]!=x&&a[i][j]!='T')break;
				}
				if(j==4)j--;
				//printf("%c:%d %d,%c\n", x,i,j,a[i,j]);
				if(a[i][j]==x||a[i][j]=='T')ans=x;
			}

			if(a[0][i]!='T') x=a[0][i];
			else x=a[1][i];			
			if(x!='.')
			{
				for (j = 0; j < 4; ++j)
				{
					if(a[j][i]!=x&&a[j][i]!='T')break;
				}
				if(j==4)j--;
				if(a[j][i]==x||a[j][i]=='T')ans=x;
			}	

			//printf("%c\n", ans);
			if(ans!='D')break;				
		}

		if(a[0][0]!='T')x=a[0][0];
		else x=a[1][1];		
		if (x!='.')
		{
			for (j = 0; j < 4; ++j)
			{
				if(a[j][j]!=x&&a[j][j]!='T')break;
			}
			if(j==4)j--;
			if(a[j][j]==x||a[j][j]=='T')ans=x;
		}

		if(a[0][3]!='T')x=a[0][3];
		else x=a[1][2];		
		if(x!='.')
		{
			for (j = 0; j < 4; ++j)
			{
				if(a[j][3-j]!=x&&a[j][3-j]!='T')break;
			}
			if(j==4)j--;
			if(a[j][3-j]==x||a[j][3-j]=='T')ans=x;			
		}

		if (ans!='D') printf("%c won\n", ans);
		else
			if(dot) printf("Game has not completed\n");
			else printf("Draw\n");
		ch=getchar();
	}
	return 0;
}