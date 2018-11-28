#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()

{
	FILE *fi,*fo;
	
	int i,j,t,tt,x,o,cx,co,dot;
	
	char m[5][5];
	
	
	fi=fopen("A.in","r");
	fo=fopen("A.out","w");
	
	fscanf(fi,"%d\n",&t);
	
	for (tt=0;tt<t;tt++)
	{	
		for (i=0;i<4;i++) fscanf(fi,"%s",m[i]);
		
		cx=co=dot=0;
		for (i=0;i<4;i++)
		{
			x=o=0;
			for (j=0;j<4;j++)
			{
				if (m[i][j]=='X' || m[i][j]=='T') x++;
				if (m[i][j]=='O' || m[i][j]=='T') o++;
				if (m[i][j]=='.') dot++;
			}
			if (x==4) cx++;
			if (o==4) co++;
			x=o=0;
			for (j=0;j<4;j++)
			{
				if (m[j][i]=='X' || m[j][i]=='T') x++;
				if (m[j][i]=='O' || m[j][i]=='T') o++;
			}			
			if (x==4) cx++;
			if (o==4) co++;
			
		}
		x=o=0;
		for (i=0;i<4;i++) 
		{
				if (m[i][i]=='X' || m[i][i]=='T') x++;
				if (m[i][i]=='O' || m[i][i]=='T') o++;			
		}
		if (x==4) cx++;
		if (o==4) co++;
		x=o=0;
		for (i=0;i<4;i++) 
		{
				if (m[i][3-i]=='X' || m[i][3-i]=='T') x++;
				if (m[i][3-i]=='O' || m[i][3-i]=='T') o++;			
		}
		if (x==4) cx++;
		if (o==4) co++;
		if (cx>0) fprintf(fo,"Case #%d: X won\n",tt+1);
		else if (co>0) fprintf(fo,"Case #%d: O won\n",tt+1);
		else if (dot>0) fprintf(fo,"Case #%d: Game has not completed\n",tt+1);
		else fprintf(fo,"Case #%d: Draw\n",tt+1);
		
	}
	
	fclose(fi);
	fclose(fo);

	return 0;
}
