#include<cstdio>
#include<cstring>
#define inRange(x,y) (x>=0 && y>=0 && x<w && y<h)
int move[4][2]={{0,-1},{-1,0},{1,0},{0,1}};
int map[100][100];
int p[100][100];
char result;
int w,h;
int getP(int x,int y)
{
if(p[y][x]>-1)
	return p[y][x];
int i,min=map[y][x],newX,newY;
int target[2]={x,y};
for(i=0;i<4;++i)
	{
	newX=x+move[i][0],newY=y+move[i][1];
	if(inRange(newX,newY) && min>map[newY][newX])
		min=map[newY][newX],target[0]=newX,target[1]=newY;
	}
if(target[0]==x && target[1]==y)
	return p[y][x]=y*w+x;
return p[y][x]=getP(target[0],target[1]);
}
int main()
{
int nT,t,i,j;
char hash[100*100];
char ch;
scanf("%d",&nT);
for(t=1;t<=nT;++t)
	{
	memset(hash,0,sizeof(hash));
	memset(p,-1,sizeof(p));
	scanf("%d%d",&h,&w);
	for(i=0;i<h;++i)
		for(j=0;j<w;++j)
			scanf("%d",&map[i][j]);
	for(i=0;i<h;++i)
		for(j=0;j<w;++j)
			getP(j,i);
	printf("Case #%d:\n",t);
	ch='a';
	for(i=0;i<h;++i)
		{
		for(j=0;j<w;++j)
			{
			if(hash[p[i][j]]=='\0')
				{
				hash[p[i][j]]=ch++;
				if(ch>'z')
					ch='a';
				}
			putc(hash[p[i][j]],stdout);
			if(j<w-1)
				putc(' ',stdout);
			}
		putc('\n',stdout);
		}
	}
}