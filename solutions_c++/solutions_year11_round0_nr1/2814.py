#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <iostream>
using namespace std;
typedef struct Pace
{
	int pa, order;
};
int orange[20000], blue[20000];
Pace paceo[100], paceb[100];
int co, cb, po, pb, io, ib;
char ch;
int i, j, e, n, t, tmp, offset;
void move_blue()
{
	int m;
	for (m=cb+offset; m>=offset; m--)
	{
		blue[m]=blue[m-offset];
	}
	cb+=offset;
	pb+=offset;
}
void move_orange()
{
	int m;
	for (m=co+offset; m>=offset; m--)
	{
		orange[m]=orange[m-offset];
	}
	co+=offset;
	po+=offset;
}
void main()
{
	FILE *rFile=fopen("D:\\A-large.in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\A-out.txt", "w"); e=ferror(rFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=0; i<t; i++)
	{
		fscanf(rFile, "%d", &n);
		co=0; cb=0;
		for (j=0; j<20000; j++)
		{
			orange[j]=0;
			blue[j]=0;
		}
		for (j=0; j<n; j++)
		{
			ch=' ';
			while(ch==' ') fscanf(rFile, "%c", &ch);
			fscanf(rFile, "%d", &tmp);
			if (ch=='O')
			{
				paceo[co].pa=tmp;
				paceo[co].order=j+1;
				co++;
			}
			else
			{
				paceb[cb].pa=tmp;
				paceb[cb].order=j+1;
				cb++;
			}
		}
		
		po=1; pb=1; io=-1; ib=-1;
		for (j=0; j<co; j++)
		{
			io+=abs(paceo[j].pa-po)+1;
			orange[io]=paceo[j].order;
			po=paceo[j].pa;
		}
		for (j=0; j<cb; j++)
		{
			ib+=abs(paceb[j].pa-pb)+1;
			blue[ib]=paceb[j].order;
			pb=paceb[j].pa;
		}
		
		po=0;
		for (j=0; j<co; j++)
		{
			while (orange[po]==0) po++;
			po++;
		}
		orange[po]=-1;
		pb=0;
		for (j=0; j<cb; j++)
		{
			while (blue[pb]==0) pb++;
			pb++;
		}
		blue[pb]=-1;
		co=po; cb=pb;
		
		po=0; pb=0;
		while (orange[po]==0) po++;
		while (blue[pb]==0) pb++;
		while (po!=co && pb!=cb)
		{
			if (po<pb&&orange[po]<blue[pb])
			{
				po++;
				while (orange[po]==0) po++;
			}
			else if (pb<po&&blue[pb]<orange[po])
			{
				pb++;
				while (blue[pb]==0) pb++;
			}
			else if (pb<=po&&blue[pb]>orange[po])
			{
				offset=po-pb+1;
				move_blue();
			}
			else
			{
				offset=pb-po+1;
				move_orange();
			}
		}//while

		cout << "result:" << max(co, cb) << endl;
		fprintf(wFile, "Case #%d: %d\n", i+1, max(co, cb));
	}//for i=0; i<t
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}