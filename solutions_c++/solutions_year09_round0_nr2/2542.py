// QRB.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <conio.h>

using namespace std;
FILE * fp;
FILE * fpout;
typedef struct _tagPoint
{
	int x;
	int y;
}point;

point nextPoint(point a,int w,int h,int ** map)
{
	point min;
	min.x=-1;
	min.y=-1;
	if(a.x<0||a.x>w||a.y<0||a.y>h)
		return min;
	min.x=a.x;
	min.y=a.y;
	if(a.y>0)
	{
		if(map[a.y-1][a.x]<map[min.y][min.x])
		{
			min.x=a.x;
			min.y=a.y-1;
		}
	}
	if(a.x>0)
	{
		if(map[a.y][a.x-1]<map[min.y][min.x])
		{
			min.x=a.x-1;
			min.y=a.y;
		}

	}
	if(a.x<w-1)
	{
		if(map[a.y][a.x+1]<map[min.y][min.x])
		{
			min.x=a.x+1;
			min.y=a.y;
		}
	}
	if(a.y<h-1)
	{
		if(map[a.y+1][a.x]<map[min.y][min.x])
		{
			min.x=a.x;
			min.y=a.y+1;
		}
	}
	return min;
}

void findway(point pt,int w,int h,int ** map,char ** labels)
{
	point tmp,result;
	if(pt.y>0)
	{
		tmp.x=pt.x;
		tmp.y=pt.y-1;
		result=nextPoint(tmp,w,h,map);
		if(result.x==pt.x && result.y==pt.y&&labels[tmp.y][tmp.x]=='\0')
		{
			labels[tmp.y][tmp.x]=labels[pt.y][pt.x];
			findway(tmp,w,h,map,labels);
		}
	}
	if(pt.x>0)
	{
		tmp.x=pt.x-1;
		tmp.y=pt.y;
		result=nextPoint(tmp,w,h,map);
		if(result.x==pt.x && result.y==pt.y&&labels[tmp.y][tmp.x]=='\0')
		{
			labels[tmp.y][tmp.x]=labels[pt.y][pt.x];
			findway(tmp,w,h,map,labels);
		}
	}
	if(pt.x<w-1)
	{
		tmp.x=pt.x+1;
		tmp.y=pt.y;
		result=nextPoint(tmp,w,h,map);
		if(result.x==pt.x && result.y==pt.y&&labels[tmp.y][tmp.x]=='\0')
		{
			labels[tmp.y][tmp.x]=labels[pt.y][pt.x];
			findway(tmp,w,h,map,labels);
		}
	}
	if(pt.y<h-1)
	{
		tmp.x=pt.x;
		tmp.y=pt.y+1;
		result=nextPoint(tmp,w,h,map);
		if(result.x==pt.x && result.y==pt.y&&labels[tmp.y][tmp.x]=='\0')
		{
			labels[tmp.y][tmp.x]=labels[pt.y][pt.x];
			findway(tmp,w,h,map,labels);
		}
	}

	result=nextPoint(pt,w,h,map);
	if(result.x>=0&&result.y>=0)
		if((result.x!=pt.x||result.y!=pt.y)&&labels[result.y][result.x]=='\0')
		{
			labels[result.y][result.x]=labels[pt.y][pt.x];
			findway(result,w,h,map,labels);
		}
}
void OneCase(int h,int w)
{
	int ** map=new int *[h];
	char ** labels=new char *[h];
	int i,j;
	for(i=0;i<h;i++)
	{
		map[i]=new int[w];
		memset(map[i],0,w*4);
		
		labels[i]=new char[w];
		memset(labels[i],0,w);
		
		for(j=0;j<w;j++)
		{
			fscanf(fp,"%d",&map[i][j]);
		}
	}
	point pt;
	pt.x=0;pt.y=0;
	char ch='a';
	for(pt.y=0;pt.y<h;pt.y++)
	{
		for(pt.x=0;pt.x<w;pt.x++)
		{
			if(labels[pt.y][pt.x]=='\0')
			{
				labels[pt.y][pt.x]=ch;
				findway(pt,w,h,map,labels);
				ch++;
			}
		}
	}
	for(i=0;i<h;i++)
	{
		for(j=0;j<w;j++)
		{
			printf("%c ",labels[i][j]);
			fprintf(fpout,"%c ",labels[i][j]);
		}
		fprintf(fpout,"\n");
		printf("\n");
	}
}
int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	printf("Input filename:");
	char fn[256]="";
	memset(fn,0,255);
	int i=0;
	do
	{
		fn[i++]=getch();
		putch(fn[i-1]);
		if(i>255)
		{
			printf("\ninput error!\n");
			return 0;
		}
	}while(fn[i-1]!='\r'&&fn[i-1]!='\n');
	fn[i-1]='\0';

	fp=fopen(fn,"r");
	fpout=fopen("out.txt","w");
	if(!fp)
	{
		printf("file error!");
		return 0;
	}
	int cases=0,count;
	fscanf(fp,"%d",&cases);
	int h=0,w=0;
	for(i=0;i<cases;i++)
	{
		fscanf(fp,"%d %d",&h,&w);
		printf("Case #%d:\n",i+1);
		fprintf(fpout,"Case #%d:\n",i+1);
		OneCase(h,w);
	}
	fclose(fpout);
	fclose(fp);
	return 0;
}
