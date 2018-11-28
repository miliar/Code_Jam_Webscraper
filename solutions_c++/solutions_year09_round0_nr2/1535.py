#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

#define MAX 10005 // adjust this properly (the max size of your set)

/* UNION-FIND library */
int p[MAX],rank[MAX];

// make a new set ID x
void make_set(int x)
{
	p[x] = x;
	rank[x] = 0;
}

// don't call link directly, rather, use union_set
void link(int x,int y)
{
	if(rank[x] > rank[y])
		p[y] = x;
	else
	{
		p[x] = y;
		if (rank[x] == rank[y])
			rank[y] = rank[y] + 1;
	}
}

// find the set ID of item x
int find_set(int x)
{
	if (x != p[x])
		p[x] = find_set(p[x]);
	
	return p[x];
}

// union two set containing item x and item y
// see, this one calls find_set first!
void union_set(int x,int y)
{
	link(find_set(x),find_set(y));
}



main()
{
	int map_res[105][105];
	int map[105][105];

	int i,j,count;
	int T,H,W,CASE=0;
	int min,min_index;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d %d",&H,&W);

		for(i=count=0; i<H; i++)
			for(j=0; j<W; j++)
			{
				scanf("%d",&map[i][j]);

				map_res[i][j] = count;
				make_set(count);
				count++;
			}


		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
			{
				min = map[i][j];
				min_index = 0;

				if(i-1 >= 0)
				{
					if(map[i-1][j] < min)
					{
						min = map[i-1][j];
						min_index = 1;
					}
				}
				
				if(j-1 >= 0)
				{
					if(map[i][j-1] < min)
					{
						min = map[i][j-1];
						min_index = 2;
					}
				}

				if(j+1 < W)
				{
					if(map[i][j+1] < min)
					{
						min = map[i][j+1];
						min_index = 3;
					}
				}

				if(i+1 < H)
				{
					if(map[i+1][j] < min)
					{
						min = map[i+1][j];
						min_index = 4;
					}
				}

				if(min_index == 1)
					union_set(map_res[i-1][j],map_res[i][j]);
				else if(min_index == 2)
					union_set(map_res[i][j-1],map_res[i][j]);
				else if(min_index == 3)
					union_set(map_res[i][j+1],map_res[i][j]);
				else if(min_index == 4)
					union_set(map_res[i+1][j],map_res[i][j]);

			}

		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
				map[i][j] = find_set(map_res[i][j]);

		int label[MAX];

		for(i=0; i<count; i++)
			label[i] = -1;

		int next_label = 0;
		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
				if(label[ map[i][j] ] == -1)
				{
					label[ map[i][j] ] = next_label;
					next_label++;
				}

		printf("Case #%d:\n",CASE);
		
		for(i=0; i<H; i++)
		{
			for(j=0; j<W; j++)
			{
				if(j)
					printf(" ");
				printf("%c",label[map[i][j]]+'a');
			}
			printf("\n");
		}
	}

}



