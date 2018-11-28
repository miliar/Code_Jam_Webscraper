#include<stdio.h>

class Solver
{
private:
	int parent[12000];
	int rank[12000];
	char name[12000];	// name of basin
	int alt[120][120];
	int H, W, ID;
	int Find(int a)	// with Path Compression
	{
		if(parent[a] == a)
			return a;
		parent[a] = Find(parent[a]);
		return parent[a];
	}
	void Union(int a, int b)	// by rank
	{
		a = Find(a);
		b = Find(b);
		if(rank[a] < rank[b])
		{
			parent[a] = parent[b];
			++rank[b];
		} else {
			parent[b] = parent[a];
			++rank[a];
		}
	}
public:
	Solver(int H, int W, int ID)
	{
		this->H = H;
		this->W = W;
		this->ID = ID;
		// initialize union-find data structure
		for(int i=0;i<H*W;i++)
		{
			parent[i] = i;
			rank[i] = 0;
			name[i] = 0;
		}
	}
	int FindNeighbor(int x, int y)	// return cell id (Y*W + X)
	{
		int min_alt = alt[y][x];
		int id = y*W+x;
		if(y-1 >= 0)	// north
		{
			if(alt[y-1][x] < min_alt)
			{
				min_alt = alt[y-1][x];
				id = (y-1)*W+x;
			}
		}
		if(x-1 >= 0) 	// west
		{
			if(alt[y][x-1] < min_alt)
			{
				min_alt = alt[y][x-1];
				id = y*W+x-1;
			}
		}
		if(x+1 < W)		// east
		{
			if(alt[y][x+1] < min_alt)
			{
				min_alt = alt[y][x+1];
				id = y*W+x+1;
			}
		}
		if(y+1 < H)		// south
		{
			if(alt[y+1][x] < min_alt)
			{
				min_alt = alt[y+1][x];
				id = (y+1)*W+x;
			}
		}
		return id;
	}
	void Solve()
	{
		// Input
		for(int y=0;y<H;y++)
		{
			for(int x=0;x<W;x++)
			{
				scanf("%d", &(alt[y][x]));
			}
		}
		// unions
		for(int y=0;y<H;y++)
		{
			for(int x=0;x<W;x++)
			{
				// find min altitude neighbors
				int min_id = FindNeighbor(x, y);
				if(min_id != y*W+x)	// cell is not sink
				{
					Union(y*W+x, min_id);	
				}
			}
		}
		// print result
		char cur = 'a';
		printf("Case #%d:\n", ID+1);
		for(int y=0;y<H;y++)
		{
			for(int x=0;x<W;x++)
			{
				int id = Find(y*W+x);
				if(name[id] == 0)	// no name assigned
				{
					name[id] = cur++;
				}
				printf("%c", name[id]);
				if(x < W-1)
					printf(" ");
			}
			printf("\n");
		}
	}
};

int main()
{
	int T, W, H;
	scanf("%d", &T);
	for(int i=0;i<T;i++)
	{
		scanf("%d%d", &H, &W);
		Solver x(H, W, i);
		x.Solve();
	}
	return 0;
}
