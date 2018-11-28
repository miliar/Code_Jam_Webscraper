#include<stdio.h>
#include<stdlib.h>


int w, h;
int count;
FILE *in, *out, *check;

void changeMap(int **map)
{
	int k, i;
	char a = 'a';
	char basin[30] = {0,};
	for( k = 0; k < h; k++)
	{
		for( i = 0; i < w; i++)
		{
			if( basin[map[i][k]] == 0 )
			{
				basin[map[i][k]] = a;
				map[i][k] = a;
				a++;
			}
			else
			{
				map[i][k] = basin[map[i][k]];
			}
		}
	}
}

int go(int **map, int **cpy, int x, int y)
{
	if( cpy[x][y] != 0 )
		return cpy[x][y];

	int min = 100000;
	int dir;

	if( y != 0 )
	{
		if( map[x][y] > map[x][y-1] && map[x][y-1] < min )
		{
			min = map[x][y-1];
			dir = 0;
		}
	}
	if( x != 0 )
	{
		if( map[x][y] > map[x-1][y] && map[x-1][y] < min )
		{
			min = map[x-1][y];
			dir = 1;
		}
	}
	if( x != w-1 )
	{
		if( map[x][y] > map[x+1][y] && map[x+1][y] < min )
		{
			min = map[x+1][y];
			dir = 3;
		}
	}
	if( y != h-1 )
	{
		if( map[x][y] > map[x][y+1] && map[x][y+1] < min )
		{
			min = map[x][y+1];
			dir = 2;
		}
	}
	if( min == 100000)
	{
		cpy[x][y] = count;
		count++;
		return cpy[x][y];
	}
	else
	{
		switch(dir)
		{
		case 0:
			cpy[x][y] = go(map,cpy,x,y-1);
			return cpy[x][y];
		case 1:
			cpy[x][y] = go(map,cpy,x-1,y);
			return cpy[x][y];
		case 2:
			cpy[x][y] = go(map,cpy,x,y+1);
			return cpy[x][y];
		case 3:
			cpy[x][y] = go(map,cpy,x+1,y);
			return cpy[x][y];
		}
	}
}


int **start(int w, int h)
{
	count = 1;
	int **map = (int**)calloc(w,sizeof(int*));
	int **cpy = (int**)calloc(w,sizeof(int*));
	int k;
	for( k = 0; k < w; k++)
	{
		map[k] = (int*)calloc(h,sizeof(int));
		cpy[k] = (int*)calloc(h,sizeof(int));
	}
	int i;
	for( k = 0; k < h; k++)
	{
		for( i = 0; i < w; i++)
		{
			fscanf(in,"%d",&map[i][k]);
			fprintf(check,"%d ",map[i][k]);
		}
		fprintf(check,"\n");
	}

	for( k = 0; k < h ; k++)
	{
		for( i = 0; i < w; i++)
		{
			cpy[i][k] = go(map,cpy,i,k);
		}
	}
	free(map);
	return cpy;
}

int main()
{
	
	in = fopen("B-large.in","r");
	out = fopen("outputt.txt","w");
	check = fopen("check.txt","w");
	int n;
	fscanf(in,"%d",&n);
	int k;
	fprintf(check,"%d\n",n);


	int i, j;
	int **map;
	for( k = 0; k < n; k++)
	{
		fscanf(in,"%d",&h);
		fscanf(in,"%d",&w);
		fprintf(check,"%d %d\n",h,w);
		map = start(w,h);
		changeMap(map);		
		fprintf(out,"Case #%d:\n",k+1);
		for( i = 0; i < h; i++)
		{
			fprintf(out,"%c",(char)map[0][i]);
			for( j = 1; j < w; j++)
			{
				fprintf(out," %c",(char)map[j][i]);
			}
			fprintf(out,"\n");
		}
		free(map);
	}
	system("pause");
	return 0;
}