#include<stdio.h>
char map[5][5];
bool chx(int j)
{
	if(j==4)
	{
		printf("X won\n");
		return 1;
	}
	return 0;
}
bool cho(int j)
{
	if(j==4)
	{
		printf("O won\n");
		return 1;
	}
	return 0;
}
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("pla.txt","w",stdout);
	int a,b,c,n,i,j;
	bool ch,ck;
	scanf("%d",&n);
	for(a=0;a<n;a++)
	{
		scanf("\n");
		for(b=0;b<4;b++)
			scanf("%s",map[b]);
		printf("Case #%d: ",a+1);
		for(b=0,ch=0,ck=0;b<4;b++)
		{
			for(c=0;c<4;c++)
			{
				// X checker
				for(i=0,j=0;i<4;i++)
					if(c+i<4 && (map[b][c+i]=='X' || map[b][c+i]=='T'))
						j++;
				ch=chx(j);	if(ch)	break;
				
				for(i=0,j=0;i<4;i++)
					if(b+i<4 && (map[b+i][c]=='X' || map[b+i][c]=='T'))
						j++;
				ch=chx(j);	if(ch)	break;
				
				for(i=0,j=0;i<4;i++)
					if(b+i<4 && c+i<4 && (map[b+i][c+i]=='X' || map[b+i][c+i]=='T'))
						j++;
				ch=chx(j);	if(ch)	break;
				
				for(i=0,j=0;i<4;i++)
					if(b+i<4 && c-i>=0 && (map[b+i][c-i]=='X' || map[b+i][c-i]=='T'))
						j++;
				ch=chx(j);	if(ch)	break;

				//O checker
				for(i=0,j=0;i<4;i++)
					if(c+i<4 && (map[b][c+i]=='O' || map[b][c+i]=='T'))
						j++;
				ch=cho(j);	if(ch)	break;
				
				for(i=0,j=0;i<4;i++)
					if(b+i<4 && (map[b+i][c]=='O' || map[b+i][c]=='T'))
						j++;
				ch=cho(j);	if(ch)	break;
				
				for(i=0,j=0;i<4;i++)
					if(b+i<4 && c+i<4 && (map[b+i][c+i]=='O' || map[b+i][c+i]=='T'))
						j++;
				ch=cho(j);	if(ch)	break;
				
				for(i=0,j=0;i<4;i++)
					if(b+i<4 && c-i>=0 && (map[b+i][c-i]=='O' || map[b+i][c-i]=='T'))
						j++;
				ch=cho(j);	if(ch)	break;
			
				//'.' checker
				if(map[b][c]=='.')	ck=1;
			}
			if(ch)	break;
		}
		if(!ch && !ck)	printf("Draw\n");
		else if(!ch && ck)	printf("Game has not completed\n");
	}
	return 0;
}
