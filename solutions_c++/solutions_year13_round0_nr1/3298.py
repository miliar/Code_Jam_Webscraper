#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int n,i,j,k,a,b,nr,o,x,t,nul;
char s[5][5];
int main()
{
	bool ok=false;
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	scanf("%d\n",&n);
	for (int l=1;l<=n;l++)
	{
		ok=false;
		for (i=1;i<=4;i++) gets(s[i]+1);
		scanf("\n");
		nul=0;
		for (i=1;i<=4;i++)
		{
			x=o=t=0;
			for (j=1;j<=4;j++)
				if (s[i][j]=='O') o++;else
					if (s[i][j]=='X') x++;else
						if (s[i][j]=='T') t++;
							else nul++;
			if (!ok) if (o==4 || (o==3 && t==1)) { printf("Case #%d: O won\n",l);ok=true;}
			if (!ok) if (x==4 || (x==3 && t==1)) { printf("Case #%d: X won\n",l);ok=true;}
		}
		for (j=1;j<=4;j++)
		{
			x=o=t=0;
			for (i=1;i<=4;i++)
				if (s[i][j]=='O') o++;else
					if (s[i][j]=='X') x++;else
						if (s[i][j]=='T') t++;
			if (!ok) if (o==4 || (o==3 && t==1)) { printf("Case #%d: O won\n",l);ok=true;}
			if (!ok) if (x==4 || (x==3 && t==1)) { printf("Case #%d: X won\n",l);ok=true;}
		}
		x=t=o=0;
		for (i=1;i<=4;i++)
			if (s[i][i]=='O') o++;else
					if (s[i][i]=='X') x++;else
						if (s[i][i]=='T') t++;
		if (!ok) if (o==4 || (o==3 && t==1)) { printf("Case #%d: O won\n",l);ok=true;}
		if (!ok) if (x==4 || (x==3 && t==1)) { printf("Case #%d: X won\n",l);ok=true;}
		x=t=o=0;
		for (i=1;i<=4;i++)
			if (s[i][5-i]=='O') o++;else
					if (s[i][5-i]=='X') x++;else
						if (s[i][5-i]=='T') t++;
		if (!ok) if (o==4 || (o==3 && t==1)) { printf("Case #%d: O won\n",l);ok=true;}
		if (!ok) if (x==4 || (x==3 && t==1)) { printf("Case #%d: X won\n",l);ok=true;}
		if (!ok) {if (nul==0) {printf("Case #%d: Draw\n",l);ok=true;}else
		{printf("Case #%d: Game has not completed\n",l);ok=true;}}
	}
	return 0;
}