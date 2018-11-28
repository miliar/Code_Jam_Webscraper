#include <iostream>
#include <stdio.h>
#include <memory.h>
#define CHAR 30
#define DNum 30
#define NNum 105
char Cmap[CHAR][CHAR];
char C_in[10];
bool Dmap[CHAR][CHAR];
char D_in[10];
char N_in[NNum];
char ans[NNum];
int last;

void getC(int C)
{
	int a,b;
	char to;
	memset(Cmap,-1,sizeof(Cmap));
	while(C--)
	{
		scanf(" %s",&C_in);
		a=C_in[0]-'A';
		b=C_in[1]-'A';
		to=C_in[2];
		Cmap[a][b]=to;
		Cmap[b][a]=to;
	}
}

void getD(int D)
{
	int a,b;
	memset(Dmap,0,sizeof(Dmap));
	while(D--)
	{
		scanf(" %s",D_in);
		a=D_in[0]-'A';
		b=D_in[1]-'A';
		Dmap[a][b]=1;
		Dmap[b][a]=1;
	}
}



void myinsert(char c)
{
	int a,b,i;
	last++;
	ans[last]=c;
	while(last)
	{
		a=ans[last]-'A';
		b=ans[last-1]-'A';
		if(Cmap[a][b]==-1) break;
		last--;
		ans[last]=Cmap[a][b];
	}
	a=ans[last]-'A';
	for(i=0;i<last;i++)
	{
		b=ans[i]-'A';
		if(Dmap[a][b])
		{
			last=-1;
			break;
		}
	}
}
void slove(int n)
{
	last=-1;
	int i;
	for(i=0;i<n;i++)
		myinsert(N_in[i]);
	printf("[");
	if(last>=0) printf("%c",ans[0]);
	for(i=1;i<=last;i++)
	{
		printf(", %c",ans[i]);
	}
	printf("]\n");
}
int main()
{
	int T,Case=1;
	int C,D,N;
	//freopen("B-large.in","r",stdin);
	//freopen("B-my.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&C);
		getC(C);
		scanf("%d",&D);
		getD(D);
		scanf("%d",&N);
		scanf(" %s",&N_in);
		printf("Case #%d: ",Case++);
		slove(N);
	}
	return 0;
}