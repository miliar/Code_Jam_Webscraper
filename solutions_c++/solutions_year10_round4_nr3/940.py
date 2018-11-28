#include <stdio.h>
#include <stdlib.h>
bool a[500][500];
bool b[500][500];
int i,j,ii,jj;
bool flag;
void main()
{
	FILE *fp;
	if ((fp=fopen("C-small-attempt1.in", "r+"))==NULL)
	{
		printf("cannot open this file\n");
		exit(0);
	}
	FILE *fp2;
	if ((fp2=fopen("out.txt", "w+"))==NULL)
	{
		printf("cannot new this file\n");
		exit(0);
	}
	int c,r,x1,y1,x2,y2,t=0;
	fscanf(fp,"%d",&c);
	for (i=0;i<c;i++)
	{
		fscanf(fp,"%d",&r);
		for (ii=0;ii<500;ii++)
			for (jj=0;jj<500;jj++)
			{
				a[ii][jj]=0;
				b[ii][jj]=0;
			}
		t=0;
		for (j=0;j<r;j++)
		{
			fscanf(fp,"%d %d %d %d",&x1,&y1,&x2,&y2);
			for (ii=x1;ii<=x2;ii++)
				for (jj=y1;jj<=y2;jj++)
					a[ii][jj]=1;
		}
		flag=true;
		while (flag)
		{
			for (ii=1;ii<500;ii++)
				for (jj=1;jj<500;jj++)
					b[ii][jj]=((!a[ii][jj])&a[ii-1][jj]&a[ii][jj-1])|(a[ii][jj]&(a[ii-1][jj]|a[ii][jj-1]));
			for (ii=1;ii<500;ii++)
				for (jj=1;jj<500;jj++)
					a[ii][jj]=b[ii][jj];
			flag=false;
			for (ii=0;ii<500;ii++)
				for (jj=0;jj<500;jj++)
					if (a[ii][jj]==1)
						flag=true;
			t++;
		}
		fprintf(fp2,"Case #%d: %d\n", i+1, t);
	}
}
