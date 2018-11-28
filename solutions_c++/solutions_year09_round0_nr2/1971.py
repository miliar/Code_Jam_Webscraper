// Watersheds.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "iostream"
using namespace std;

#define INFILE "B-large.in"
#define OUTFILE "B-large.out"

struct Point
{
	int x,y;
};
int h,w;
int map[100][100];
int numfill;
char mapout[100][100];
int row[] = {-1, 0, 0, 1};
int col[] = {0 ,-1, 1, 0};
Point queue[10001];
int qfront, qrear;
int tmpi;

Point popQueue()
{
	Point result=queue[qfront];
	qfront++;
	return result;
}

void pushQueue(Point p)
{
	qrear++;
	queue[qrear]=p;
	//cout<<qrear<<":"<<p.x<<" "<<p.y<<" --> "<<(int)mapout[p.x][p.y]<<endl;
}

int isConnected(int i, int j, int x, int y)
{
	int min=map[i][j];
	int kmin=-1;
	int ro,co;
	for (int k=0; k<4; k++)
	{
		ro = i + row[k];
		co = j + col[k];
		if ((ro>=0)&&(ro<h)&&(co>=0)&&(co<w))
			{
				if (map[ro][co]<min)
				{
					min=map[ro][co];
					kmin=k;
				}
			}
	}
	ro = i+row[kmin];
	co = j+col[kmin];
	if ((ro==x)&&(co==y))
		return 1;
	return 0;
	
}

void go(int i, int j, char c)
{
	mapout[i][j]=c;
	int min=map[i][j];
	int kmin=-1;
	for (int k=0; k<4; k++)
	{
		int ro = i + row[k];
		int co = j + col[k];
		if ((ro>=0)&&(ro<h)&&(co>=0)&&(co<w))
			//if (mapout[ro][co]==0)
			{
				if (map[ro][co]<min)
				{
					min=map[ro][co];
					kmin=k;
				}
				else
					if ((map[ro][co]>map[i][j])&&(mapout[ro][co]==0))
						if (isConnected(ro,co,i,j))
						{
							//go(ro,co,c);
							mapout[ro][co]=1;
							Point p;
							p.x=ro;
							p.y=co;
							pushQueue(p);
						}
			}
	}
	if (kmin!=-1)
		if (mapout[i+row[kmin]][j+col[kmin]]==0)
		{
			//go(i+row[kmin], j+col[kmin], c);
			Point p;
			p.x=i+row[kmin];
			p.y=j+col[kmin];
			mapout[p.x][p.y]=1;
			pushQueue(p);
		}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	int t;
	infile>>t;
	for (int i=0; i<t; i++)
	{
		tmpi=i;
		infile>>h>>w;
		for (int j=0; j<h; j++)
			for (int k=0; k<w; k++)
				infile>>map[j][k];

		memset(mapout,0,sizeof(char)*sizeof(mapout));
		numfill = 0;
		char cfill='a';
			for (int j=0; j<h; j++)
				for (int k=0; k<w; k++)
					if (mapout[j][k]==0)
					{
						qfront=0;
						qrear=-1;
						Point start;
						start.x=j;
						start.y=k;
						pushQueue(start);
						while (qfront<=qrear)
						{
							Point p = popQueue();
							go(p.x,p.y,cfill);
						}
						//cout<<"----"<<endl;
						cfill++;
					}

		
		
		outfile<<"Case #"<<i+1<<":"<<endl;
		for (int j=0; j<h; j++)
		{
			for (int k=0; k<w; k++)
				outfile<<mapout[j][k]<<" ";
			outfile<<endl;
		}

	}
	infile.close();
	outfile.close();
	return 0;
}

