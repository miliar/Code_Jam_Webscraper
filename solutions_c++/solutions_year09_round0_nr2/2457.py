#include<stdio.h>

#define MH 100
#define MW 100

int alttd[MH][MW];
char map[MH][MW];
int height;
int width;
int sinkIndex;
bool tftable[MH][MW];
char cdata[26];
int conIndex;

void convert(int x, int y)
{
	int target=map[y][x]-'A';
	if(cdata[target]=='.')
	{
		cdata[target]=conIndex+'a';
		conIndex++;
	}
	map[y][x]=cdata[target];
}

void chkSink(int y, int x)
{
	bool isSink=true;
	if(x>0&&alttd[y][x-1]<alttd[y][x])	isSink=false;
	if(x<width-1&&alttd[y][x+1]<alttd[y][x])	isSink=false;
	if(y>0&&alttd[y-1][x]<alttd[y][x])	isSink=false;
	if(y<height-1&&alttd[y+1][x]<alttd[y][x])	isSink=false;
	if(isSink)
	{
		map[y][x]='A'+sinkIndex++;
		tftable[y][x]=true;
	}
	else
	{
		map[y][x]='.';
		tftable[y][x]=false;
	}
}

int fill(int i, int j, char target)
{
	int minAlttd, direction, N, E, W, S;
	minAlttd=alttd[i][j];
	N=E=W=S=100000;
	direction=0;

	if(i<0||j<0||i>=height||j>=width)	return 0;

	if(i<height-1)
	{
		S=alttd[i+1][j];
		if(S<minAlttd)	direction=1;
	}
	if(j<width-1)
	{
		E=alttd[i][j+1];
		if(E<minAlttd&&E<=S)	direction=2;
	}
	if(j>0)
	{
		W=alttd[i][j-1];
		if(W<minAlttd&&W<=S&&W<=E)	direction=3;
	}
	if(i>0)
	{
		N=alttd[i-1][j];
		if(N<minAlttd&&N<=S&&N<=E&&N<=W)	direction=4;
	}

	switch(direction)
	{
	case 1:	if(map[i+1][j]==target)	map[i][j]=map[i+1][j];
		break;
	case 2:	if(map[i][j+1]==target)	map[i][j]=map[i][j+1];
		break;
	case 3:	if(map[i][j-1]==target)	map[i][j]=map[i][j-1];
		break;
	case 4:	if(map[i-1][j]==target)	map[i][j]=map[i-1][j];
		break;
	}
	if(map[i][j]=='.')	return 0;
	return 1;
}

void flooding(int x, int y, char target)
{
	int count, length, i, j, k;
	i=y;
	j=x;
	length=0;
	do
	{
		i++;
		count=0;
		length++;
		for(k=0; k<length; k++)	count+=fill(--i, --j, target);
		for(k=0; k<length; k++)	count+=fill(--i, ++j, target);
		for(k=0; k<length; k++)	count+=fill(++i, ++j, target);
		for(k=0; k<length; k++)	count+=fill(++i, --j, target);
	}while(length<200);
}

void solve(int caseNum)
{
	int i, j;
	bool hit;
	
	scanf("%d %d", &height, &width);
	sinkIndex=0;
	for(i=0; i<26; i++)	cdata[i]='.';
	conIndex=0;
	for(i=0; i<height; i++)	for(j=0; j<width; j++)	scanf("%d", &alttd[i][j]);
	
	for(i=0; i<height; i++)	for(j=0; j<width; j++)	chkSink(i, j);

	for(i=0; i<height; i++)	for(j=0; j<width; j++)	if(tftable[i][j])	flooding(j, i, map[i][j]);
	bool repeat;
	do
	{
		repeat=false;
		for(i=0; i<height; i++)
		{
			for(j=0; j<width; j++)
			{
				if(map[i][j]<'A'||map[i][j]>'Z')	repeat=true;
				if(tftable[i][j])	flooding(j, i, map[i][j]);
			}
		}
	}while(repeat);
	for(i=0; i<height; i++)	for(j=0; j<width; j++)	convert(j, i);

	printf("Case #%d:\n", caseNum+1);
	for(i=0; i<height; i++)
	{
		for(j=0; j<width; j++)	printf("%c ", map[i][j]);
		printf("\n");
	}
}

int main()
{
	int i, n;
	scanf("%d", &n);
	for(i=0; i<n; i++)	solve(i);
	return 0;
}