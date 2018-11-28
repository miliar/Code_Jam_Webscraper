#include <iostream>
#include <stdio.h>
using namespace std;
#define  MAX  10000000

//void sink( int** map, int i, int j, int r, int c,int height,int width);
void sink( int** map, int i, int j, int& r, int& c,int height,int width);
void main()
{

	int h,w, num;
	
	FILE * pFile;
	FILE*  out;
	pFile = fopen ("E:\\B-large.in","r+");
	out = fopen("E:\\out_large.out","w+");

	fscanf (pFile, "%d", &num);
	
	for(int t=0;t<num;t++)
	{				
					//printf("%s%d%s\n","Case #",t+1,":");
					fprintf(out,"%s%d%s\n","Case #",t+1,":");
					fscanf (pFile, "%d", &h);
					fscanf (pFile, "%d", &w);
					
					int** map = new int*[h];
					int** label = new int*[h];
					for (int i=0;i<h;i++)
					{
						map[i] = new int[w];
						label[i] = new int[w];
					}

					for (int i=0;i<h;i++)
					{
						for (int j=0;j<w;j++)
						{
							fscanf (pFile, "%d", &map[i][j]);
							label[i][j] = 0;
						}
					}

					int region = 0;
					for (int i=0;i<h;i++)
					{
						for (int j=0;j<w;j++)
						{
							int r=0,c=0;
							
							sink(map,i,j,r,c,h,w);
							if (label[r][c] == 0)
							{
								region++;
								label[i][j] = region;
								label[r][c] = region;
							}
							else
							{
								label[i][j] = label[r][c];
							}
						}
					}

					for (int i=0;i<h;i++)
					{
						for (int j=0;j<w;j++)
						{
							//cout<<label[i][j]<<'\t';
							fprintf(out,"%c\t",'a'+label[i][j]-1);
						}
						//cout<<endl;
						fprintf(out,"\n");
					}
					for (int i=0;i<h;i++)
					{
						delete[] map[i];
						delete[] label[i];
					}
					
		}

	fclose (pFile);
}

void sink( int** map, int i, int j, int& row, int& col,int height,int width)
{
	int u, d, l,r;
	u = (i>=1)?map[i-1][j]:MAX;
	d = (i<=(height-2))?map[i+1][j]:MAX;
	l = (j>=1)?map[i][j-1]:MAX;
	r = (j<=width-2)?map[i][j+1]:MAX;
	
	int c = map[i][j];
	if (u>=c && d>=c && l>=c && r>=c)
	{
		row = i;
		col =j;
		return;
	}
	int minimun = min(min(min(u,d),l),r);
	if (minimun == u)
	{
		i = i-1;
		sink(map,i,j,row,col,height,width);
		return;
	}
	if (minimun == l)
	{
		j = j-1;
		sink(map,i,j,row,col,height,width);
		return;
	}
	if (minimun == r)
	{
		j = j+1;
		sink(map,i,j,row,col,height,width);
		return;
	}
	if (minimun == d)
	{
		i = i+1;
		sink(map,i,j,row,col,height,width);
		return;
	}
	
}