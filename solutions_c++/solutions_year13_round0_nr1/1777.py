#include<cstdio>
#include<cstring>

char m[5][5];

int cal()
{
	int i,j,a,b,ret=3;
	for(i=0;i<4;i++)
	{
		a=b=0;
		for(j=0;j<4;j++)
			switch(m[i][j])
			{
				case 'X': a++;break;
				case 'O': b++;break;
				case 'T': a++;b++;break;
				case '.': ret=4;
			}
		if(a>=4) return 1;
		if(b>=4) return 2;
	}
	for(i=0;i<4;i++)
	{
		a=b=0;
		for(j=0;j<4;j++)
			switch(m[j][i])
			{
				case 'X': a++;break;
				case 'O': b++;break;
				case 'T': a++;b++;break;
				case '.': ret=4;
			}
		if(a>=4) return 1;
		if(b>=4) return 2;
	}
	a=b=0;
	for(i=0;i<4;i++)
		switch(m[i][i])
		{
			case 'X': a++;break;
			case 'O': b++;break;
			case 'T': a++;b++;break;
			case '.': ret=4;
		}
	if(a>=4) return 1;
	if(b>=4) return 2;
	a=b=0;
	for(i=0;i<4;i++)
		switch(m[i][3-i])
		{
			case 'X': a++;break;
			case 'O': b++;break;
			case 'T': a++;b++;break;
			case '.': ret=4;
		}
	if(a>=4) return 1;
	if(b>=4) return 2;
	return ret;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
		int i;
		for(i=0;i<4;i++)
			scanf("%s",m[i]);
		int ans=cal();
		printf("Case #%d: ",cnt);
		switch(ans)
		{
			case 1: printf("X won");break;
			case 2: printf("O won");break;
			case 3: printf("Draw");break;
			case 4: printf("Game has not completed");
		}
		printf("\n");
	}
}
