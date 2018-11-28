#include<iostream>
using namespace std;
int main()
{
	FILE *fin,*fout;
	fin=fopen("in.in","r");
	fout=fopen("out.in","w");
	int t;
	char a[51][51];
	fscanf(fin,"%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int r,c;
		char ch;
		fscanf(fin,"%d%d",&r,&c);
		int i,j;
		for(i=0;i<r;i++)
		{
			ch=fscanf(fin,"%c",&ch);
			for(j=0;j<c;j++)
				fscanf(fin,"%c",&a[i][j]);
		}
		for(i=0;i<r-1;i++)
		{
			for(j=0;j<c-1;j++)
			{
				if(a[i][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j]=='#'&&a[i+1][j+1]=='#')
				{
				a[i][j]=a[i+1][j+1]='/';
				a[i+1][j]=a[i][j+1]='\\';
				j++;
				}
			}
		}
		bool tag=true;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(a[i][j]=='#')
				{
					tag=false;
					break;
				}
			}
			if(!tag)
				break;
		}
		fprintf(fout,"Case #%d:\n",tt);
		if(tag)
		{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					fprintf(fout,"%c",a[i][j]);
				}
				fprintf(fout,"\n");
			}
		}
		else
		{
			fprintf(fout,"Impossible\n");
		}
	}
	return 0;
}