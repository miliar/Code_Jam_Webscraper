#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int test;
	FILE *fr=fopen("a-large.in","r");
	FILE *fw=fopen("out.txt","w");
	fscanf(fr,"%d",&test);
	for(int p=0;p<test;p++)
	{
		fprintf(fw,"Case #%d: ",p+1);
		char map[4][4];
		int cnt=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fscanf(fr," %c",&map[i][j]);
				if(map[i][j]!='.')
				{
					cnt++;
				}
			}
		}
		for(int i=0;i<4;i++)
		{
			int x=0,o=0,t=0;
			for(int j=0;j<4;j++)
			{
				if(map[i][j]=='X')
				{
					x++;
				}
				if(map[i][j]=='O')
				{
					o++;
				}
				if(map[i][j]=='T')
				{
					t++;
				}
			}
			if(x+t==4)
			{
				goto winx;
			}
			if(o+t==4)
			{
				goto wino;
			}
		}
		for(int i=0;i<4;i++)
		{
			int x=0,o=0,t=0;
			for(int j=0;j<4;j++)
			{
				if(map[j][i]=='X')
				{
					x++;
				}
				if(map[j][i]=='O')
				{
					o++;
				}
				if(map[j][i]=='T')
				{
					t++;
				}
			}
			if(x+t==4)
			{
				goto winx;
			}
			if(o+t==4)
			{
				goto wino;
			}
		}
		int x=0,o=0,t=0;
		for(int j=0;j<4;j++)
		{
			if(map[j][j]=='X')
			{
				x++;
			}
			if(map[j][j]=='O')
			{
				o++;
			}
			if(map[j][j]=='T')
	 		{
	 			t++;
	 		}
		}
	  	if(x+t==4)
		{
			goto winx;
		}
		if(o+t==4)
		{
			goto wino;
		}
		x=0;
		o=0;
		t=0;
		for(int j=0;j<4;j++)
		{
			if(map[3-j][j]=='X')
			{
				x++;
			}
			if(map[3-j][j]=='O')
			{
				o++;
			}
			if(map[3-j][j]=='T')
			{
				t++;
			}
		}
		if(x+t==4)
		{
			goto winx;
		}
		if(o+t==4)
		{
			goto wino;
		}
		if(false)
		{
winx:;
			fprintf(fw,"X won\n");
			continue;
		}
		if(false)
		{
wino:;
			fprintf(fw,"O won\n");
			continue;
		}
		if(cnt==16)
		{
			fprintf(fw,"Draw\n");
		}
		else
		{
			fprintf(fw,"Game has not completed\n");
		}
	}
}