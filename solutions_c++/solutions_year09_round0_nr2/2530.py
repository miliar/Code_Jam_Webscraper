#include<stdio.h>
#include<stdlib.h>

int area[100][100];
int x=0;
int y=0;

main()
{
	int z;
	int i,j;
	int maps;

	FILE *fp;
	fp=fopen("in","r");

	FILE *fp2=fopen("output.txt","w");

	fscanf(fp,"%d",&maps);
	
	int area[100][100];
	char assign[100][100];
	char label='a';

	for(int i=0;i<100;i++)
	{
		for(int j=0;j<100;j++)
			assign[i][j]='1';
	}

	for(z=0;z<maps;z++)
	{
		label='a';
		int length,width;
		fscanf(fp,"%d %d",&length,&width);
		for(i=0;i<length;i++)
		{
			for(j=0;j<width;j++)
				fscanf(fp,"%d",&area[i][j]);
		}
		for(i=0;i<length;i++)
		{
			for(j=0;j<width;j++)
			{

//
	int current=area[i][j];
	x=i;
	y=j;

	if((i+1)<length)  //south
	{
		if(area[i+1][j]<=current)
		{
			
			current=area[i+1][j];
			x=i+1;
			y=j;
		}
	}

	if((j+1)<width) //east
	{
		if(area[i][j+1]<=current)
		{
			current=area[i][j+1];
			x=i;
			y=j+1;
		}
	}

	if((j-1)>=0)  //west
	{
		if(area[i][j-1]<=current)
		{
			current=area[i][j-1];
			x=i;
			y=j-1;
		}
	}

	if((i-1)>=0)   //north
	{
		if(area[i-1][j]<=current)
		{
			current=area[i-1][j];
			x=i-1;
			y=j;
		}
	}
	
	if(area[x][y]==area[i][j])
	{
		x=i;
		y=j;
	}

//

				if((i==x)&(j==y))
				{
					if(assign[x][y]=='1')
					{
						assign[x][y]=label;
						label++;
					}
				}
				else if(assign[x][y]=='1'&assign[i][j]=='1')
				{
					assign[x][y]=label;
					assign[i][j]=label;
					label++;
				}
				else if(assign[i][j]!='1'&assign[x][y]=='1')
				{
					//printf("Assigned %d,%d as %c",x,y,assign[i][j]);
					assign[x][y]=assign[i][j];
				}
				else if(assign[i][j]=='1'&assign[x][y]!='1')
				{
					//printf("Assigned %d,%d as %c",i,j,assign[x][y]);
					assign[i][j]=assign[x][y];
				}
				else
				{
					char a,b;
					if(assign[i][j]>assign[x][y])
					{
						a=assign[x][y];
						b=assign[i][j];
					}
					else
					{
						a=assign[i][j];
						b=assign[x][y];
					}
					assign[i][j]=a;
					assign[x][y]=a;
					int m,n;
					while(b!=label)
					{
						for(m=0;m<length;m++)
						{
							for(n=0;n<width;n++)
							{
								if(assign[m][n]==b)
									assign[m][n]=a;
							}
						}
						b++;
						a++;
					}
					label--;
				}
			}
		}
		fprintf(fp2,"Case #%d:\n",z+1);
		for(i=0;i<length;i++)
		{
			for(j=0;j<width;j++)
			{
				fprintf(fp2,"%c ",assign[i][j]);
			}
			fprintf(fp2,"\n");
		}
	for(int i=0;i<100;i++)
	{
		for(int j=0;j<100;j++)
			assign[i][j]='1';
	}		
	}
}
