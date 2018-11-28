#include <stdio.h>

int T;
int H, W;
int map[100][100];
int direction[100][100];
int result[100][100];
enum {NONE, NORTH, WEST, EAST, SOUTH};

int getDirection(int h, int w)
{
	int largeDiff = 0;
	int t;
	int d = NONE;
	if(h > 0)
	{
		t = map[h][w] - map[h-1][w]; // NORTH
		if(t > largeDiff)
		{
			largeDiff = t;
			d = NORTH;
		}
	}

	if(w > 0)
	{
		t = map[h][w] - map[h][w-1]; // WEST
		if(t > largeDiff)
		{
			largeDiff = t;
			d = WEST;
		}
	}

	if(w < W-1)
	{
		t = map[h][w] - map[h][w+1]; // EAST
		if(t > largeDiff)
		{
			largeDiff = t;
			d = EAST;
		}
	}

	if(h < H-1)
	{
		t = map[h][w] - map[h+1][w]; // SOUTH
		if(t > largeDiff)
		{
			largeDiff = t;
			d = SOUTH;
		}
	}

	return d;
}

void setLabel(int h, int w, char label)
{
	if( result[h][w] != 0) return;
	result[h][w] = label;
	if( direction[h][w] == NORTH) setLabel(h-1, w, label);
	else if(direction[h][w] == WEST) setLabel(h, w-1, label);
	else if(direction[h][w] == EAST) setLabel(h, w+1, label);
	else if(direction[h][w] == SOUTH) setLabel(h+1, w, label);

	if(h > 0)
	{
		if(direction[h-1][w] == SOUTH)
		{
			setLabel(h-1, w, label);
		}
	}

	if(w > 0)
	{
		if(direction[h][w-1] == EAST)
		{
			setLabel(h, w-1, label);
		}
	}

	if(w < W-1)
	{
		if(direction[h][w+1] == WEST)
		{
			setLabel(h, w+1, label);
		}
	}

	if(h < H-1)
	{
		if(direction[h+1][w] == NORTH)
		{
			setLabel(h+1, w, label);
		}
	}
}

int main()
{
	scanf("%d", &T);
	for(int i = 0; i < T; i++)
	{
		scanf("%d%d", &H, &W);
		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				scanf("%d", &map[h][w]);
			}
		}

		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				direction[h][w] = getDirection(h, w);
			}
		}
		
		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				result[h][w] = 0;
			}
		}
		char label = 'a';
		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				if(result[h][w] == 0)
				{
					setLabel(h, w, label);
					label++;
				}
			}
		}
		printf("Case #%d:\n", i+1);
		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				printf("%c%c", result[h][w], w == W-1 ? '\n' : ' ');
			}
		}
	}

	return 0;
}
