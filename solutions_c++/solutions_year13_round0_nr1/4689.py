#include <cstdio>
#include <cstring>
#include <cstdlib>

int t,id;
char map[9][9];
int i,j,k,l,ans;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);id=0;
	while(t--)
	{
		id++;
		printf("Case #%d: ",id);
		for (i=0;i<4;i++)scanf("%s",map[i]);
		ans=0;
		for (i=0;i<4;i++)
		{
			l=k=0;
			for (j=0;j<4;j++)
			{
				if (map[i][j]=='X' || map[i][j]=='T')k++;
				if (map[i][j]=='O' || map[i][j]=='T')l++;
			}
			if (k==4)ans=1;
			if (l==4)ans=2;

			l=k=0;
			for (j=0;j<4;j++)
			{
				if (map[j][i]=='X' || map[j][i]=='T')k++;
				if (map[j][i]=='O' || map[j][i]=='T')l++;
			}
			if (k==4)ans=1;
			if (l==4)ans=2;

		}
			l=k=0;
			for (j=0;j<4;j++)
			{
				if (map[j][j]=='X' || map[j][j]=='T')k++;
				if (map[j][j]=='O' || map[j][j]=='T')l++;
			}
			if (k==4)ans=1;
			if (l==4)ans=2;
			
			l=k=0;
			for (j=0;j<4;j++)
			{
				if (map[j][3-j]=='X' || map[j][3-j]=='T')k++;
				if (map[j][3-j]=='O' || map[j][3-j]=='T')l++;
			}
			if (k==4)ans=1;
			if (l==4)ans=2;

		if (ans==1)printf("X won\n");
		else if (ans==2)printf("O won\n");
		else
		{
			for (i=0;i<4;i++)
				for (j=0;j<4;j++)
					ans+= (map[i][j]=='.');
			if (ans>0) printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
	return 0;
}