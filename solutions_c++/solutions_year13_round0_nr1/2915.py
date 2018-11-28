#include<cstdio>
#include<cstring>

#define M 1000
#define N 4

char tab[N][N];
int casN;

int test()
{
	int i,j;
	int cnto,cntx;
	for(i=0;i<N;i++)
	{
		cntx=0;cnto=0;
		for(j=0;j<N;j++)
		{
			if(tab[i][j]=='X'||tab[i][j]=='T')cntx++;
			if(tab[i][j]=='O'||tab[i][j]=='T')cnto++;
		}
		if(cntx==4)return 0;
		if(cnto==4)return 1;
	}
	for(i=0;i<N;i++)
	{
		cntx=0;cnto=0;
		for(j=0;j<N;j++)
		{
			if(tab[j][i]=='X'||tab[j][i]=='T')cntx++;
			if(tab[j][i]=='O'||tab[j][i]=='T')cnto++;
		}
		if(cntx==4)return 0;
		if(cnto==4)return 1;
	}
	cntx=0;cnto=0;
	for(i=0;i<N;i++)
	{
		if(tab[i][i]=='X'||tab[i][i]=='T')cntx++;
		if(tab[i][i]=='O'||tab[i][i]=='T')cnto++;
	}
	if(cntx==4)return 0;
	if(cnto==4)return 1;
	cntx=0;cnto=0;
	for(i=0;i<N;i++)
	{
		if(tab[i][N-1-i]=='X'||tab[i][N-1-i]=='T')cntx++;
		if(tab[i][N-1-i]=='O'||tab[i][N-1-i]=='T')cnto++;
	}
	if(cntx==4)return 0;
	if(cnto==4)return 1;
	int cnta=0;
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			if(tab[i][j]!='.')cnta++;
	if(cnta==N*N)return 2;//draw;
	else return 3;
}

int main()
{
	scanf("%d",&casN);
	int cas;
	char tmp[10];
	for(cas=1;cas<=casN;cas++)
	{
		int i;
		for(i=0;i<N;i++)
		{
			scanf("%s",tmp);
			int j;
			for(j=0;j<N;j++)tab[i][j]=tmp[j];
		}
		int ret=test();
		char str[50];
		switch(ret)
		{
			case 0:strcpy(str,"X won");break;
			case 1:strcpy(str,"O won");break;
			case 2:strcpy(str,"Draw");break;
			case 3:strcpy(str,"Game has not completed");break;
			default:strcpy(str,"Error");break;
		}
		printf("Case #%d: %s\n",cas,str);
	}
	return 0;
}
