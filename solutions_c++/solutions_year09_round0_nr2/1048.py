#include <iostream>
using namespace std;

#define h					first
#define w					second

typedef pair<int, int> PII;

const int MAX_H = 1 << 7;
const int MAX_W = 1 << 7;

const int INF = 1 << 20;

const int dh[4] = {- 1,   0,   0, + 1};
const int dw[4] = {  0, - 1, + 1,   0};

int T, H, W, B;
int a[MAX_H][MAX_W], b[MAX_H][MAX_W], m[32];


PII flow(int h, int w)
{
PII ret(h, w);
	
	for(int  i = 0; i < 4; i ++)
	{
		int new_h = h + dh[i];
		int new_w = w + dw[i];
		
		if(!(0 <= new_h && new_h < H) || !(0 <= new_w && new_w < W)) continue;
		
		if(a[new_h][new_w] < a[ret.h][ret.w]) ret = PII(new_h, new_w);
	}
	
	return ret;
}

void DFS(int h, int w)
{
	b[h][w] = B;
	
	for(int  i = 0; i < 4; i ++)
	{
		int new_h = h + dh[i];
		int new_w = w + dw[i];
		
		if(!(0 <= new_h && new_h < H) || !(0 <= new_w && new_w < W)) continue;
		
		PII f = flow(new_h, new_w);
		
		if(f == PII(h, w) && b[new_h][new_w] == 0) DFS(new_h, new_w);
	}
}

int main()
{
	scanf("%d", & T);
	
	for(int test = 1; test <= T; test ++)
	{
		B = 0;
		
		for(int  i = 0; i < 32; i ++)
			m[i] = - 1;
		
		for(int i = 0; i < MAX_H; i ++)
			for(int j = 0; j < MAX_W; j ++)
		{
			a[i][j] = 0;
			b[i][j] = 0;
		}
		
		scanf("%d %d", & H, & W);
		
		for(int i = 0; i < H; i ++)
			for(int j = 0; j < W; j ++)
				scanf("%d", & a[i][j]);
		
		for(int h = 0; h < H; h ++)
		{
			for(int w = 0; w < W; w ++)
			{
			PII f = flow(h, w);
				
				if(f == PII(h, w))
				{
					B ++;
					
					DFS(h, w);
				}
			}
		}
		
/*
		for(int i = 0; i < H; i ++)
		{
			for(int j = 0; j < W; j ++)
				printf("%d ", b[i][j]);
			
			printf("\n");
		}
//		system("pause");
*/
		
		B = 0;
		
		printf("Case #%d:\n", test);
		
		for(int i = 0; i < H; i ++)
		{
			for(int j = 0; j < W; j ++)
			{
			char c;
				
				if(m[b[i][j]] < 0) m[b[i][j]] = B ++;
				
				c = 'a' + m[b[i][j]];
				
				printf("%c", c);
				if(j + 1 < W) printf(" ");
			}
			
			printf("\n");
		}
	}
	
	return 0;
}

/*
TEST 0:
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8

*/
