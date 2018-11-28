#include<cstdio>
#include<cstdlib>
#include<vector>

using namespace std;

typedef struct {
	int x, y;
} XY;

#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)>(b)?(a):(b))
void solve()
{
	int M, N;
	scanf("%d%d", &M, &N);
	
	int c[512][512];	// c[y][x]
	char hex[200];
	for(int y=0;y<M;y++)
	{
		scanf("%s", hex);
		for(int x=0;x<N/4;x++)
		{
			int val = 0;
			if(hex[x] >= 'A' && hex[x] <= 'F')
				val = hex[x]+10-'A';
			else
				val = hex[x]-'0';
			c[y][x*4] = (val & 8) == 8;
			c[y][x*4+1] = (val & 4) == 4;
			c[y][x*4+2] = (val & 2) == 2;
			c[y][x*4+3] = (val & 1) == 1;
		}
	}
/*for(int y=0;y<M;y++)
	{
		for(int x=0;x<N;x++)
		{
			printf("%d", c[y][x]);
		}
		printf("\n");
	}*/
	int size = min(M, N);
	int sizecount[513] = {0};
	int diffsize = 0;
	while(size > 0)
	{
		//printf("searcning at %d\n", size);
		vector<XY> foundat;
		for(int y=0;y<M-size+1;y++)
		{
			for(int x=0;x<N-size+1;x++)
			{
				int found = 1;
				for(int k=0;k<size;k++)
				{
					for(int j=0;j<size;j++)
					{
						if(c[y+k][x+j] == -1)
						{
							found = 0;
							break;
						}
						// within row comparison
						if(j < size-1)
						{
							if(c[y+k][x+j] == c[y+k][x+j+1])
							{
								found = 0;
								break;
							}
						}

						// previous row comparison
						if(k < size-1)
						{
							if(c[y+k][x+j] == c[y+k+1][x+j])
							{
								found = 0;
								break;
							}
						}
					}
					if(!found) break;
				}
				if(found)
				{
					XY pos;
					pos.x = x;
					pos.y = y;
					foundat.push_back(pos);
				}
			}
		}
		// remove
		sizecount[size] = foundat.size();
		//printf("found = %d\n", foundat.size());
		for(int i=0;i<foundat.size();i++)
		{
			int ok = 1;
			for(int y=foundat[i].y; y<foundat[i].y+size; y++)
			{
				for(int x=foundat[i].x; x<foundat[i].x+size; x++)
				{
					if(c[y][x] == -1)
					{
						ok = 0;
						break;
					}
				}
				if(!ok) break;
			}
			if(ok)
			{
				for(int y=foundat[i].y; y<foundat[i].y+size; y++)
				{
					for(int x=foundat[i].x; x<foundat[i].x+size; x++)
					{
						c[y][x] = -1;
					}
				}

			} else sizecount[size]--;
		}
		if(sizecount[size] > 0)
			diffsize++;

		--size;
	}
	printf("%d\n", diffsize);
	for(int k=min(M, N); k >= 1; k--)
	{
		if(sizecount[k] > 0)
		{
			printf("%d %d\n", k, sizecount[k]);
		}
	}
/*	for(int y=0;y<M;y++)
	{
		for(int x=0;x<N;x++)
		{
			printf("%d", c[y][x]);
		}
		printf("\n");
	}*/
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}

