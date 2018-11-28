#include <stdio.h>
#include <string.h>
int calc(char x[][10])
{
	int st[10];
	int sst[10];
	int nx=0,no=0,nt=0,sx,so;
	int i,j;
	char t;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			//putchar(x[i][j]);
			switch(x[i][j])
			{
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
			}
		}
	//puts("");
		//printf("%d %d %d\n",nx,no,nt);
		if(nx==no)
		{
			so=(16-nx-no-nt)/2;
			sx=16-nx-no-nt-so;
		}
		else
		{
			sx=(16-nx-no-nt)/2;
			so=16-nx-no-nt-sx;
		}
		//ºâ
		for(i=0;i<4;i++)
		{
			nx=no=nt=0;
			for(j=0;j<4;j++)
				switch(x[i][j])
			{
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
			}
			if(nx&&no)st[i]=-1;
			else if(nx+nt==4)return 'X';
			else if(no+nt==4)return 'O';
			else st[i]=4-nt-nx-no;
			sst[i]=nx!=0 ? 'X' : (no!=0 ? 'O' : 0);
		}

		for(i=0;i<4;i++)
		{
			nx=no=nt=0;
			for(j=0;j<4;j++)
				switch(x[j][i])
			{
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
			}
			if(nx&&no)st[i+4]=-1;
			else if(nx+nt==4)return 'X';
			else if(no+nt==4)return 'O';
			else st[i+4]=4-nt-nx-no;
			sst[i+4]=nx!=0 ? 'X' : (no!=0 ? 'O' : 0);
		}

		nx=no=nt=0;
		for(j=0;j<4;j++)
			switch(x[j][j])
		{
			case 'X':
				nx++;
				break;
			case 'O':
				no++;
				break;
			case 'T':
				nt++;
		}
		if(nx&&no)st[8]=-1;
		else if(nx+nt==4)return 'X';
		else if(no+nt==4)return 'O';
		else st[8]=4-nt-nx-no;
		sst[8]=nx!=0 ? 'X' : (no!=0 ? 'O' : 0);

		nx=no=nt=0;
		for(j=0;j<4;j++)
			switch(x[j][3-j])
		{
			case 'X':
				nx++;
				break;
			case 'O':
				no++;
				break;
			case 'T':
				nt++;
		}
		if(nx&&no)st[9]=-1;
		else if(nx+nt==4)return 'X';
		else if(no+nt==4)return 'O';
		else st[9]=4-nt-nx-no;
		sst[9]=nx!=0 ? 'X' : (no!=0 ? 'O' : 0);

		if(so==0&&sx==0)return -1;
		return 0;

		//for(i=0;i<10;i++)
		//{
		//	if(st[i]!=-1)
		//	{
		//		//printf("%d %d\n",i,sst[i]);
		//		if(sst[i]==0)
		//		{
		//			if(st[i]>sx&&st[i]>so)sst[i]=-1;
		//			else if(st[i]>sx)sst[i]='O';
		//			else if(st[i]>so)sst[i]='X';
		//			else sst[i]=0;
		//		}
		//		else if(sst[i]=='X')
		//		{
		//			if(st[i]>sx)sst[i]=-1;
		//		}
		//		else
		//		{
		//			if(st[i]>so)sst[i]=-1;
		//		}
		//	}
		//	else sst[i]=-1;
		//}

		//bool yx=0,yo=0;
		//for(i=0;i<10;i++)
		//{
		//	if(sst[i]=='X')yx=1;
		//	if(sst[i]=='O')yo=1;
		//	if(sst[i]==0)return 0;
		//}

		//if(yx&&yo)return 0;
		//else if(yx)return 'X';
		//else if(yo)return 'O';
		//else return -1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int k,i,j;
	char m[10][10];
	scanf("%d",&cas);
	for(k=1;k<=cas;k++)
	{
		if(k!=1)gets(m[0]);
		for (i=0;i<4;i++)
			scanf("%s",m[i]);
		int r=calc(m);
		printf("Case #%d: ",k);
		switch(r)
		{
		case 'X':
			puts("X won");
			break;
		case 'O':
			puts("O won");
			break;
		case 0:
			puts("Game has not completed");
			break;
		case -1:
			puts("Draw");
		}
	}
	return 0;
}