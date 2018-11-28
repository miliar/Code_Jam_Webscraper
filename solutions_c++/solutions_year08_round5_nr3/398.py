//CODEJAM - C

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

int best;
int sy,sx;
bool field[15][15];

void rec(int y,int x,int c)
{
	//cout << y << ' ' << x << ' ' << c << endl;
	//next row
	if (y==sy)
	{
		rec(0,x+1,c);
		return;
	}
	//done?
	if (x==sx)
	{
			if (c>best)
				best=c;
		return;
	}
	//nothing
		if (field[y][x])
		{
			rec(y+1,x,c);
			return;
		}
	//find this column
	int y2=y,y3;
	bool field2[15][15];
	memcpy(field2,field,sizeof(field));
		while ((y2<sy) && (!field[y2][x]))
			y2++;
	//fill it
		if (y>0)
			field[y-1][x+1]=true;
		for (y3=y; y3<y2; y3++)
			field[y3][x+1]=true;
	field[y2][x+1]=true;
	rec(y2,x,c+(y2-y));
	memcpy(field,field2,sizeof(field));
	//don't fill it
	rec(y2,x,c);
}

int main()
{
	//vars
	ifstream f ("C.in");
	ofstream g ("C.out");
	int t,tt;
	int a,b;
	char ch;
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> sy >> sx;
				for (a=0; a<sy; a++)
					for (b=0; b<sx; b++)
					{
						f >> ch;
						field[a][b]=(ch=='x');
					}
			//recursive
			best=0;
			rec(0,0,0);
			//output
			cout << "Case #" << t << ": ";
			cout << best << endl;
			g << "Case #" << t << ": ";
			g << best << endl;
		}
	return(0);
}