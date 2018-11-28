#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
using namespace std;

const int NMAX=100;

int main()
{
	int m[NMAX][NMAX];

	FILE *f=fopen("a.in","r");
	FILE *g=fopen("a.out","w");

	int t;
	fscanf(f,"%i\n",&t);
	for(int u=0;u<t;u++)
	{
		int r,c;
		fscanf(f,"%i%i\n",&r,&c);
		printf("r=%i\n",r);
		printf("c=%i\n",c);
		char ch;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				fscanf(f,"%c",&ch);
				if(ch=='.')
					m[i][j]=0;
				else
					m[i][j]=1;
			}
			fscanf(f,"%c",&ch);
		}
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
				if(m[i][j]==1)
				{
					if(j+1<c && i+1<r && m[i][j+1]==1 && m[i+1][j]==1 && m[i+1][j+1]==1)
					{
						m[i][j]=2;
						m[i][j+1]=3;
						m[i+1][j]=4;
						m[i+1][j+1]=5;
					}
				}
			}
		int found=0;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
				if(m[i][j]==1)
				{
					found=1;
					break;
				}
			}
		if(found==1)
			fprintf(g,"%s%i%s\n%s\n","Case #",u+1,":","Impossible");
		else
		{
			fprintf(g,"%s%i%s\n","Case #",u+1,":");
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
				{
					if(m[i][j]==0)
						fprintf(g,"%c",'.');
					if(m[i][j]==2)
						fprintf(g,"%c",'/');
					if(m[i][j]==3)
						fprintf(g,"%c",'\\');
					if(m[i][j]==4)
						fprintf(g,"%c",'\\');
					if(m[i][j]==5)
						fprintf(g,"%c",'/');
				}
				fprintf(g,"%s","\n");
			}
		}
	}
	fclose(f);
	fclose(g);
}







						
					

		
	

