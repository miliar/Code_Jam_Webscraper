#include "utils.h"
#include <iostream>
#include <string>

using namespace std;
void flood(char c,int *map,char *str,int x, int y, int H,int W);

bool fromTo(int *map,int x1,int y1,int x2,int y2,int H,int W)
{
	if(map[y1*W+x1]<=map[y2*W+x2])
		return false;
	int x=x1;
	int y=y1;
	int min=11000;
	if(y1!=0 && map[(y1-1)*W+x1]<min)
	{
		min=map[(y1-1)*W+x1];
		y=y1-1;
	}
	if(x1!=0 && map[y1*W+x1-1]<min)
	{
		min=map[y1*W+x1-1];
		x=x1-1;
		y=y1;
	}
	if((x1<W-1) && map[y1*W+x1+1]<min)
	{
		min=map[y1*W+x1+1];
		x=x1+1;
		y=y1;
	}
	if((y1<H-1) && map[(y1+1)*W+x1]<min)
	{
		min=map[(y1+1)*W+x1];
		y=y1+1;
		x=x1;
	}
	return (x==x2 && y==y2);
}

void isSB(int *map,int x1,int y1,int x2,int y2,int H,int W,char *str,char c) //Same basin
{
	if(x2<0 || x2>=W)
		return;
	if(y2<0 || y2>=H)
		return;
	if(str[y2*W+x2]!=0)
		return;
	int x,y;
	
	if(fromTo(map,x1,y1,x2,y2,H,W) || fromTo(map,x2,y2,x1,y1,H,W))
	{
		str[y2*W+x2] = c;
		flood(c,map,str,x2,y2,H,W);
	}
}

void flood(char c,int *map,char *str,int x, int y, int H,int W)
{
	isSB(map,x,y,x-1,y,H,W,str,c);
	isSB(map,x,y,x+1,y,H,W,str,c);
	isSB(map,x,y,x,y-1,H,W,str,c);
	isSB(map,x,y,x,y+1,H,W,str,c);
}

void process(int index,int *map,int H,int W)
{
	char *str;
	str=new char[H*W];
	memset(str,0,H*W);

	char c='a';
	for(int i=0;i<H*W;i++)
	{
		if(str[i]==0)
		{
			str[i]=c;			
			flood(c,map,str,i%W,i/W,H,W);
			c++;
		}
	}

	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			cout<<str[i*W+j];
			if(j!=W-1)
				cout<<" ";
		}
		cout<<endl;
	}
}

int main(int argc, char **argv)
{
	if(argc!=2)
	{
		cout<<"Usage: <prog> <input_file>"<<endl;
		return 1;
	}

	argument arg(argv[1]);
	argLine a = arg.getLine(0);
	int numMap = a.getInt();
	int lc=1;
	int *map;
	for(int mp=0;mp<numMap;mp++)
	{
		cout<<"Case #"<<mp+1<<":"<<endl;
		argLine fl=arg.getLine(lc++);
		int H = fl.getInt();
		int W = fl.getInt();
		map = new int[H*W];
		memset(map,0,H*W);
		for(int h=0;h<H;h++)
		{
			argLine hl=arg.getLine(lc++);
			for(int w=0;w<W;w++)
			{
				map[h*W+w] = hl.getInt();
			}
		}
		process(mp+1,map,H,W);
		delete[] map;
	}
	
	return 0;
}