#include <stdio.h>

int main()
{
	long long tc,t,r=0,i,j,di,dj,k;
	char s[4][5];
	scanf("%lld\n",&t);
	for (tc=0;tc<t;++tc)
	{
		for (i=0;i<4;++i) scanf("%s",s[i]);
		r=0;
		for (i=0;i<4;++i) for (j=0;j<4;++j) 
		{
			char q=s[i][j];
			for (di=0;di<(i==0?2:1);++di) for (dj=(j==3?-1:0);dj<(j==0?2:1);++dj) if (di || dj)
			{
				char qq=q;
				if (q=='T') qq=s[i+di][j+dj];
				if (qq=='.') continue;
				for (k=0;k<4;++k) if (s[i+k*di][j+k*dj]!=qq && s[i+k*di][j+k*dj]!='T') break;
				if (k==4) r=qq;
			}
		}
		printf("Case #%lld: ",tc+1);
		if (r==0)
		{
			for (i=0;i<4;++i) for (j=0;j<4;++j) if (s[i][j]=='.') ++r;
			if (r==0) printf("Draw\n"); else printf("Game has not completed\n");
		} else
		{
			printf("%c won\n",(char)r);
		}
	}
	return 0;
}
