#include<stdio.h>
int main()
{
	FILE *fp=fopen("A-small-attempt0.in","r");
	FILE *fp1=fopen("output.txt","w");
	int i,j,k,m,chk,zx,zy,chk1;
	char a[10][10];
	fscanf(fp,"%d",&k);
	for(i=1;i<=k;i++)
	{
		chk=0,zx=-1,zy=-1,chk1=0;
		fscanf(fp,"\n");
		for(j=0;j<4;j++)
			fscanf(fp,"%s\n",&a[j]);
		int zx,zy;
		for(j=0;j<4;j++)
			for(m=0;m<4;m++)
			{
				if(a[j][m]=='T')
					zx=j,zy=m;
				if(a[j][m]=='.')
					chk1=1;
			}

		if(zx>=0) a[zx][zy]='O';
		for(j=0;j<4;j++)
		{
			if(a[j][0]==a[j][1] && a[j][2]==a[j][1] && a[j][2]==a[j][3] && a[j][0]!='.')
			{
				fprintf(fp1,"Case #%d: %c won\n",i,a[j][0]);
				chk=1; break;
			}

			if(a[0][j]==a[1][j] && a[2][j]==a[1][j] && a[2][j]==a[3][j] && a[0][j]!='.')
			{
				fprintf(fp1,"Case #%d: %c won\n",i,a[0][j]);
				chk=1; break;
			}
		}
		if(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[0][0]!='.')
		{
			fprintf(fp1,"Case #%d: %c won\n",i,a[0][0]);
			chk=1;
		}
		if(a[3][0]==a[2][1] && a[2][1]==a[1][2] && a[0][3]==a[1][2] && a[3][0]!='.')
		{
			fprintf(fp1,"Case #%d: %c won\n",i,a[3][0]);
			chk=1;
		}
		if(chk==1) continue;

		if(zx>=0) a[zx][zy]='X';
		for(j=0;j<4;j++)
		{
			if(a[j][0]==a[j][1] && a[j][2]==a[j][1] && a[j][2]==a[j][3] && a[j][0]!='.')
			{
				fprintf(fp1,"Case #%d: %c won\n",i,a[j][0]);
				chk=1; break;
			}

			if(a[0][j]==a[1][j] && a[2][j]==a[1][j] && a[2][j]==a[3][j] && a[0][j]!='.')
			{
				fprintf(fp1,"Case #%d: %c won\n",i,a[0][j]);
				chk=1; break;
			}
		}
		if(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[0][0]!='.')
		{
			fprintf(fp1,"Case #%d: %c won\n",i,a[0][0]);
			chk=1;
		}
		if(a[3][0]==a[2][1] && a[2][1]==a[1][2] && a[0][3]==a[1][2] && a[3][0]!='.')
		{
			fprintf(fp1,"Case #%d: %c won\n",i,a[3][0]);
			chk=1;
		}
		if(chk==1) continue;
		if(chk1==1)
			fprintf(fp1,"Case #%d: Game has not completed\n",i);
		else
			fprintf(fp1,"Case #%d: Draw\n",i);
	}
	return 0;
}