#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int a[4][4],n,i,x,y,c,cp,j,end;
int main()
	{
		FILE *fin,*fout;
		fin = fopen("text.in","r");
		fout = fopen("text.out", "w");
		fscanf(fin,"%d",&n);
		fscanf(fin,"%c",&c);
		for (j=0;j<n;j++)
		{
		fprintf(fout,"Case #%d: ",j+1);
		cp = 0;
		end = 0;
		memset(a,sizeof(a),0);
		for (i=0;i<20;i++)
		{
			fscanf(fin,"%c",&c);
			//fprintf(fout,"%c",c);
			if ((i % 5) != 4){
			if (c == '.') {a[i/5][i%5]=0; cp = 1;}
			if (c == 'X') a[i/5][i%5]=1;
			if (c == 'O') a[i/5][i%5]=2;
			if (c == 'T') {x = i/5; y = i%5;}}
		}
		a[x][y] = 1;
		if ((a[0][0]==1)&&(a[0][1]==1)&&(a[0][2]==1)&&(a[0][3]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[1][0]==1)&&(a[1][1]==1)&&(a[1][2]==1)&&(a[1][3]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[2][0]==1)&&(a[2][1]==1)&&(a[2][2]==1)&&(a[2][3]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[3][0]==1)&&(a[3][1]==1)&&(a[3][2]==1)&&(a[3][3]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[0][0]==1)&&(a[1][0]==1)&&(a[2][0]==1)&&(a[3][0]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[0][1]==1)&&(a[1][1]==1)&&(a[2][1]==1)&&(a[3][1]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[0][2]==1)&&(a[1][2]==1)&&(a[2][2]==1)&&(a[3][2]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[0][3]==1)&&(a[1][3]==1)&&(a[2][3]==1)&&(a[3][3]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[0][0]==1)&&(a[1][1]==1)&&(a[2][2]==1)&&(a[3][3]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		if ((a[0][3]==1)&&(a[1][2]==1)&&(a[2][1]==1)&&(a[3][0]==1)&&(end != 1)) {fprintf(fout,"X won\n"); end = 1;}
		a[x][y] = 2;
		if ((a[0][0]==2)&&(a[0][1]==2)&&(a[0][2]==2)&&(a[0][3]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[1][0]==2)&&(a[1][1]==2)&&(a[1][2]==2)&&(a[1][3]==2)&&(end != 1)){fprintf(fout,"O won\n"); end = 1;}
		if ((a[2][0]==2)&&(a[2][1]==2)&&(a[2][2]==2)&&(a[2][3]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[3][0]==2)&&(a[3][1]==2)&&(a[3][2]==2)&&(a[3][3]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[0][0]==2)&&(a[1][0]==2)&&(a[2][0]==2)&&(a[3][0]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[0][1]==2)&&(a[1][1]==2)&&(a[2][1]==2)&&(a[3][1]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[0][2]==2)&&(a[1][2]==2)&&(a[2][2]==2)&&(a[3][2]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[0][3]==2)&&(a[1][3]==2)&&(a[2][3]==2)&&(a[3][3]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[0][0]==2)&&(a[1][1]==2)&&(a[2][2]==2)&&(a[3][3]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((a[0][3]==2)&&(a[1][2]==2)&&(a[2][1]==2)&&(a[3][0]==2)&&(end != 1)) {fprintf(fout,"O won\n"); end = 1;}
		if ((cp == 1)&&(end == 0)) fprintf(fout,"Game has not completed\n");
		if ((cp == 0)&&(end == 0)) fprintf(fout,"Draw\n");
		fscanf(fin,"%c",&c);
		}
		return 0;
	}
