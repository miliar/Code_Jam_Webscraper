#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MaxT = 100;
const int MaxH = 100;
const int MaxW = 100;

int dir[4][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}};

int alt[MaxH][MaxW];
int basinCount = 0;
int basin[MaxH][MaxW];
int basinRemap[26];
int backTraceCount[MaxH][MaxW];
int backTraceDirs[MaxH][MaxW][4];
char completed[MaxH][MaxW];
int t, h, w;

void backtrace(int r, int c, int b)
{
	basin[r][c] = b;
	for (int i = 0; i < backTraceCount[r][c]; i++)
	{
		int di = backTraceDirs[r][c][i];

		int ir = r - dir[di][0];
		int ic = c - dir[di][1];
		backtrace(ir, ic, b);
	}
}

void main()
{
	scanf("%d", &t);

	for (int it = 1; it <= t; it++)
	{
		memset(basin, 0, sizeof(basin));
		memset(completed, 0, sizeof(completed));

		scanf("%d %d", &h, &w);
		for (int ih = 0; ih < h; ih++)
		{
			for (int iw = 0; iw < w; iw++)
			{
				scanf("%d", &alt[ih][iw]);
				backTraceCount[ih][iw] = 0;
			}
		}

		basinCount = 0;
		for (int ih = 0; ih < h; ih++)
		{
			for (int iw = 0; iw < w; iw++)
			{
				int minAlt = 99999;

				for (int id = 0; id < 4; id++)
				{
					int r = ih + dir[id][0];
					int c = iw + dir[id][1];

					if (r >= 0 && r < h && c >= 0 && c < w)
					{
						if (alt[r][c] < alt[ih][iw])
						{
							if (alt[r][c] < minAlt)
							{
								minAlt = alt[r][c];
							}
						}
					}
				}

				if (minAlt == 99999)
				{
					basinCount++;
					basin[ih][iw] = -basinCount;
				}
				else
				{
					for (int id = 0; id < 4; id++)
					{
						int r = ih + dir[id][0];
						int c = iw + dir[id][1];

						if (r >= 0 && r < h && c >= 0 && c < w)
						{
							if (alt[r][c] == minAlt)
							{
								int count = backTraceCount[r][c]++;
								backTraceDirs[r][c][count] = id;
								//printf("add bt of %d %d to count %d dir %d\n", 
								//	r, c, count, id
								//	);
								break;
							}
						}
					}
				}
			}
		}

		for (int ih = 0; ih < h; ih++)
		{
			for (int iw = 0; iw < w; iw++)
			{
				if (basin[ih][iw] < 0)
				{
					int b = -basin[ih][iw];
					backtrace(ih, iw, b);
				}
			}
		}

		int basinRemapCount = 0;
		memset(basinRemap, 0, sizeof(basinRemap));
		for (int ih = 0; ih < h; ih++)
		{
			for (int iw = 0; iw < w; iw++)
			{
				if (basinRemap[basin[ih][iw] - 1] == 0)
				{
					basinRemapCount++;
					basinRemap[basin[ih][iw] - 1] = basinRemapCount;
				}
			}
		}

		printf("Case #%d:\n", it);
		for (int ih = 0; ih < h; ih++)
		{
			for (int iw = 0; iw < w; iw++)
			{
				printf("%c%c", 
					'a' + basinRemap[basin[ih][iw] - 1] - 1, 
					iw < w - 1 ? ' ' : '\n');
			}
		}
	}
}
