#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>


using namespace std;

struct cell
{
	char basin;
	int group;
	int flowto;
	int toalt;
	int alt;
	cell()
	{
		basin = 0;
		flowto = -1;
		group = 0;
	}
};

int main()
{
	ifstream fsi("new2.in");
	ofstream fso("prb1.out");
	
	int tc;
	fsi >> tc;

	cout << "No of Test Cases -> " << tc << endl; 
	
	for ( int tcn =1;tcn<=tc ;tcn++ )
	{
		char basin = 'a';
		int group = 1;
		int h, w;
		fsi >> h >> w;

		cell *land = new cell [h*w];

		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				fsi >> land[i*w+j].alt;
				printf("%d ",land[i*w+j].alt);
			}
			printf("\n");
		}
		printf("\n");

		
		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				int flowto[4];
				int toalt[4];
				int ni, nj;
				 
				 //printf("i-> %d, j->%d\t",i,j);
				 // North
				 ni = i-1;
				 nj = j;
				 flowto[0] = ni*w+nj;
				 if(ni < 0 || ni == h || nj < 0 || nj == w)  
				 toalt[0] = land[i*w+j].alt;
				 else
				 toalt[0] = land[ni*w+nj].alt;
				// printf("N i-> %d, j->%d toalt->%d\t",ni,nj,toalt[0]);

				 //West
				 ni = i;
				 nj = j-1;
				 if(ni < 0 || ni == h || nj < 0 || nj == w)  
				 toalt[1] = land[i*w+j].alt;
				 else
				 toalt[1] = land[ni*w+nj].alt;
				 flowto[1] = ni*w+nj;
				 //printf("W i-> %d, j->%d toalt->%d\t",ni,nj,toalt[1]);

				 //East
				 ni = i;
				 nj = j+1;
				 if(ni < 0 || ni == h || nj < 0 || nj == w)  
				 toalt[2] = land[i*w+j].alt;
				 else
				 toalt[2] = land[ni*w+nj].alt;
				 flowto[2] = ni*w+nj;
				 //printf("E i-> %d, j->%d toalt->%d\t",ni,nj,toalt[2]);

				//South
				 ni = i+1;
				 nj = j;
				 if(ni < 0 || ni == h || nj < 0 || nj == w)  
				 toalt[3] = land[i*w+j].alt;
				 else
				 toalt[3] = land[ni*w+nj].alt;
				 flowto[3] = ni*w+nj;
				 //printf("S i-> %d, j->%d toalt->%d\t",ni,nj,toalt[3]);

				land[i*w+j].flowto = flowto[0];
				int toaltt = toalt[0];
				land[i*w+j].toalt = toaltt;
				for (int k = 0; k<4 ;k++ )
				{
					if(toaltt > toalt[k])
					{
						toaltt = toalt[k];
						land[i*w+j].toalt = toaltt;
						land[i*w+j].flowto = flowto[k];
					}
				}
				// printf("FINAL toalt-> %d\n",toaltt);

			}
		}

		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				printf("%d,%d ",land[i*w+j].flowto,land[i*w+j].toalt);
			}
			printf("\n");
		}
		printf("\n");

		for(int z= 0;z< h*w ;z++)
		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				//printf("i-> %d, j->%d\t",i,j);

				if(land[i*w+j].toalt >= land[i*w+j].alt)
				{
					if(land[i*w+j].group == 0)
					{
						land[i*w+j].group = group;
						group++;
					}
					//printf("Sink\n");
				}
				else
				{
					land[i*w+j].group = land[land[i*w+j].flowto].group;
				}
			}
		}

		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				printf("%d ",land[i*w+j].group);
			}
			printf("\n");
		}
		printf("\n");

		
		char gb[27];
		for (int i = 0; i<27;i++ )
		{
			gb[i] = 0;
		}

		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				if(i==0&&j==0)
				{
					land[i*w+j].basin = basin;
					gb[land[i*w+j].group] = basin;
					basin++;
				}
				else
				{
					if(gb[land[i*w+j].group] == 0)
					{
						land[i*w+j].basin = basin;
						gb[land[i*w+j].group] = basin;
						basin++;
					}
					else
					{
						land[i*w+j].basin = gb[land[i*w+j].group];
					}
				}
			}
		}

		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				printf("%c ",land[i*w+j].basin);
			}
			printf("\n");
		}
		printf("\n");
		//OutPutting to File

		fso << "Case #"<< tcn << ":"<<endl;
		for (int i = 0; i< h; i++)
		{
			for (int j = 0; j<w; j++)
			{
				if(j == w-1)
					fso << land[i*w+j].basin;
				else
					fso << land[i*w+j].basin << " ";

			}
			fso << endl;
		}
		printf("\n");


	}
}
