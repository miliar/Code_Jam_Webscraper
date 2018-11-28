#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdlib>
#include <cstdio>

typedef struct Cell
{
	int elevation;
	Cell* flow;
	char basin;
} Cell;

int main(int argc, char* argv[])
{
	if(argc < 2)
	{
		printf("Usage: %s inputfile\n", argv[0]);
		return(0);
	}
	FILE* finput = fopen(argv[1], "r");
	if(finput == 0)
	{
		printf("Input file could not be opened\n");
		return(0);
	}

	int cases;
	fscanf(finput, "%d", &cases);
	for(int i = 0; i < cases; i++)
	{
		printf("Case #%d:\n", i + 1);

		Cell map[10000];

		int height;
		int width;
		fscanf(finput, "%d%d", &height, &width);

		for(int j = 0; j < height; j++)
		{
			for(int k = 0; k < width; k++)
			{
				fscanf(finput, "%d", &map[j * width + k].elevation);
				map[j * width + k].basin = 0;
				map[j * width + k].flow = 0;
			}
		}

		for(int j = 0; j < height; j++)
		{
			for(int k = 0; k < width; k++)
			{
				int top;
				int left;
				int right;
				int bottom;
				int here = map[j * width + k].elevation;
				if(j > 0)
					top = map[(j - 1) * width + k].elevation;
				else
					top = 10001;
				if(j < height - 1)
					bottom = map[(j + 1) * width + k].elevation;
				else
					bottom = 10001;
				if(k > 0)
					left = map[j * width + k - 1].elevation;
				else
					left = 10001;
				if(k < width - 1)
					right = map[j * width + k + 1].elevation;
				else
					right = 10001;
				if(here <= top && here <= left && here <= right && here <= bottom)
				{
					map[j * width + k].flow = 0;
					continue;
				}
				int low = top;
				if(left < low)
					low = left;
				if(right < low)
					low = right;
				if(bottom < low)
					low = bottom;
				if(low == top)
					map[j * width + k].flow = map + (j - 1) * width + k;
				else if(low == left)
					map[j * width + k].flow = map + j * width + k - 1;
				else if(low == right)
					map[j * width + k].flow = map + j * width + k + 1;
				else
					map[j * width + k].flow = map + (j + 1) * width + k;
			}
		}

		char next = 'a';

		for(int j = 0; j < height; j++)
		{
			for(int k = 0; k < width; k++)
			{
				Cell* cell = map + j * width + k;
				if(cell->basin != 0)
					continue;
				while(cell->basin == 0)
				{
					if(cell->flow == 0)
						cell->basin = next++;
					else
						cell = cell->flow;
				}
				char basin = cell->basin;
				cell = map + j * width + k;
				while(cell->basin == 0)
				{
					cell->basin = basin;
					cell = cell->flow;
				}
			}
		}

		for(int j = 0; j < height; j++)
		{
			for(int k = 0; k < width; k++)
			{
				if(k != 0)
					printf(" ");
				printf("%c", map[j * width + k].basin);
			}
			printf("\n");
		}
	}

	fclose(finput);
	return(0);
}