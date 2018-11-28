#include<stdio.h>

char flood_fill(char table[][50], int N, int sx, int sy, int xdir, int ydir, int K)
{
	int B = 0;
	int R = 0;
	for(int k=0;k<K;k++)
	{
		if(sx+k*xdir >= 0 && sy+k*ydir >= 0 && sx+k*xdir < N && sy+k*ydir <N)
		{
		char c = table[sx+k*xdir][sy+k*ydir] ;
		if(c== 'B')
			B++;
		if(c == 'R')
			R++;
			}
	}
	if(B == K && R == K)
	{	
		return 'T';
	} else if(B== K)
		return 'B';
	else if(R == K)
		return 'R';
	return ' ';
}

void solve()
{
	int N, K;
	scanf("%d%d", &N, &K);

//	char table[50][50] = {{0}};		// table[x][y]
	char rotated[50][50] = {{0}};
	int ptr[50] = {0};				// pointer for each column
	char str[51];
	
	for(int i=0;i<N;i++) ptr[i] = N-1;	// fill from bottom

	for(int y=0;y<N;y++)
	{
		scanf("%s", str);
		for(int x=N-1;x>=0;x--)
		{
//			table[N-y-1][x] = str[x];
			if(str[x] != '.')
				rotated[N-y-1][ptr[N-y-1]--] = str[x];
		}
	}

/*	printf("\n");
	for(int y=0;y<N;y++)
	{
		for(int x=0;x<N;x++)
		{	
			printf("%c", rotated[x][y]);
		}
		printf("\n");
	}*/
	int Bwin = 0, Rwin=0;
	for(int y=0; y < N; y++)
	{
		for(int x=0;x<N;x++)
		{
			char t = flood_fill(rotated, N, x, y, 0, -1, K);	// up
			Bwin |= (t == 'T' | t == 'B');
			Rwin |= (t == 'T' | t == 'R');
			t =flood_fill(rotated, N, x, y, 1, 0, K);	// right
			Bwin |= (t == 'T' | t == 'B');
			Rwin |= (t == 'T' | t == 'R');
			t=flood_fill(rotated, N, x, y, 1, -1, K);	// 
			Bwin |= (t == 'T' | t == 'B');
			Rwin |= (t == 'T' | t == 'R');
			t= flood_fill(rotated, N, x, y, -1, -1, K);	// 
			Bwin |= (t == 'T' | t == 'B');
			Rwin |= (t == 'T' | t == 'R');
		}
	}
	if(Rwin && Bwin)
		printf("Both\n");
	else if(Rwin)
		printf("Red\n");
	else if(Bwin)
		printf("Blue\n");
	else
		printf("Neither\n");
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
