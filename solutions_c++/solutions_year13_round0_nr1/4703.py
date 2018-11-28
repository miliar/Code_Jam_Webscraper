#include<stdio.h>
#include<cstringt.h>
int t,tpos[2];
char x[4][4];
bool xwin,owin,draw,empty,begin;
int main()
{
	FILE *in=fopen("A.in","r");
	FILE *out=fopen("A.out","w");
	int i,j,k;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		for(j=0;j<4;j++)
				fscanf(in,"%s",x[j]);
		empty=0;
		tpos[0]=tpos[1]=-1;
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
			{
				if(x[j][k]=='.')empty=1;
				if(x[j][k]=='T')tpos[0]=j,tpos[1]=k;
			}
		
		xwin=0,owin=0;
		x[tpos[0]][tpos[1]]='O';
		for(j=0;j<4;j++)
		{
			if(x[j][0]=='X')begin=0;
			else if(x[j][0]=='O')begin=1;
			else continue;
			k=0;
			while(((begin&&(x[j][k]=='O'))||(!begin&&(x[j][k]=='X')))&&k<4)k++;
			if(k==4)
			{
				if(begin)owin=1;
				else xwin=1;
			}
		}
		for(j=0;j<4;j++)
		{
			if(x[0][j]=='X')begin=0;
			else if(x[0][j]=='O')begin=1;
			else continue;
			k=0;
			while(((begin&&(x[k][j]=='O'))||(!begin&&(x[k][j]=='X')))&&k<4)k++;
			if(k==4)
			{
				if(begin)owin=1;
				else xwin=1;
			}
		}
		if((x[0][0]==x[1][1])&&(x[2][2]==x[3][3])&&(x[2][2]==x[1][1]))
			if(x[0][0]=='O')owin=1;
			else if(x[0][0]=='X')xwin=1;
		if((x[0][3]==x[1][2])&&(x[2][1]==x[3][0])&&(x[2][1]==x[1][2]))
			if(x[0][3]=='O')owin=1;
			else if(x[0][3]=='X')xwin=1;

		x[tpos[0]][tpos[1]]='X';
		for(j=0;j<4;j++)
		{
			if(x[j][0]=='X')begin=0;
			else if(x[j][0]=='O')begin=1;
			else continue;
			k=0;
			while(((begin&&(x[j][k]=='O'))||(!begin&&(x[j][k]=='X')))&&k<4)k++;
			if(k==4)
			{
				if(begin)owin=1;
				else xwin=1;
			}
		}
		for(j=0;j<4;j++)
		{
			if(x[0][j]=='X')begin=0;
			else if(x[0][j]=='O')begin=1;
			else continue;
			k=0;
			while(((begin&&(x[k][j]=='O'))||(!begin&&(x[k][j]=='X')))&&k<4)k++;
			if(k==4)
			{
				if(begin)owin=1;
				else xwin=1;
			}
		}
		if((x[0][0]==x[1][1])&&(x[2][2]==x[3][3])&&(x[2][2]==x[1][1]))
			if(x[0][0]=='O')owin=1;
			else if(x[0][0]=='X')xwin=1;
		if((x[0][3]==x[1][2])&&(x[2][1]==x[3][0])&&(x[2][1]==x[1][2]))
			if(x[0][3]=='O')owin=1;
			else if(x[0][3]=='X')xwin=1;
		if(empty&&xwin==owin){fprintf(out,"Case #%d: Game has not completed\n",i);continue;}
		if(!empty&&xwin==owin){fprintf(out,"Case #%d: Draw\n",i);continue;}
		if(xwin){fprintf(out,"Case #%d: X won\n",i);continue;}
		if(owin){fprintf(out,"Case #%d: O won\n",i);continue;}
	}
	return 0;
}