#include<stdio.h>

int GeoMap[300][300];
int map[300][300];
int foundpath = 0;
int rec(int,int);
int main()
{
	FILE *fin = fopen("small.in","r");
	FILE *fout = fopen("small.out","w");
	int N;
	fscanf(fin,"%d",&N);
	for(int i = 0;i < N;i++)
	{
		int h,w;
		fscanf(fin,"%d %d",&h,&w);
		for(int j = 0;j < 300;j++)
			for(int k = 0;k < 300;k++)
				map[j][k] = 999999999;
		for(int j = 1;j <= h;j++)
			for(int k = 1;k <= w;k++)
				fscanf(fin,"%d",&map[j][k]);
		int sinkcounter = 1;
		for(int j = 1;j <= h;j++)
		{
			for(int k = 1;k <= w;k++)
			{
				if (map[j][k] <= map[j - 1][k] && map[j][k] <= map[j + 1][k] && map[j][k] <= map[j][k - 1] && map[j][k] <= map[j][k + 1])
				{
					GeoMap[j][k] = sinkcounter;
					sinkcounter ++;
				}
				else
					GeoMap[j][k] = -1;
			}
		}
		for(int j = 1;j <= h;j++)
		{
			for(int k = 1;k <= w;k++)
			{
				if (GeoMap[j][k] == -1)
				{
					rec(j,k);
				}
			}
		}
		int drainsx[100];
		for(int j = 0;j <100;j++)
			drainsx[j] = -1;
		int now = 1;
		fprintf(fout,"Case #%d:\n",i+1);
		for(int j = 1;j <=h;j++)
		{
			for(int k = 1; k <= w;k++)
			{
				if (drainsx[GeoMap[j][k]] == -1)
				{
					drainsx[GeoMap[j][k]] = 96 + now;
					now ++;
				}
				fprintf(fout,"%c",drainsx[GeoMap[j][k]]);
				if (k != w)
					fprintf(fout," ");
			}
			fprintf(fout,"\n");
		}
	}
}

int rec(int j,int k)
{
	if (GeoMap[j][k] != -1)
	{
		foundpath = GeoMap[j][k];
		return 0;
	}
	int min = 999999999;
	char direction;
	if (map[j + 1][k] < map[j][k])
	{
		min = map[j+1][k];
		direction = 'S';
	}
	if (map[j][k + 1] <= min)
	{
		min = map[j][k + 1];
		direction = 'E';
	}
	if (map[j][k - 1] <= min)
	{
		min = map[j][k - 1];
		direction = 'W';
	}
	if (map[j - 1][k] <= min)
	{
		min = map[j-1][k];
		direction = 'N';
	}
	if (direction == 'N')
		rec(j - 1,k);
	else if (direction == 'E')
		rec(j,k+1);
	else if (direction == 'W')
		rec(j,k -1);
	else if (direction == 'S')
		rec(j + 1,k);
	GeoMap[j][k] = foundpath;
}