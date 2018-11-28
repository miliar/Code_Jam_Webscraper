#include <cstdio>
#include <cstring>
#include <cassert>

struct trip
{
	int start;
	int end;
};

int main(int argc, char* argv[])
{
	int cases;
	FILE* f;
	int i, j, k;
	assert(argc > 1)
	f = fopen(argv[1], "r");
	assert(f);
	fscanf(f, "%d\n", &cases);
	for(i = 0; i < cases; i++)
	{
		int turn = 0;
		trip nat[100];
		trip nbt[100];
		int idlea = 0;
		int idleb = 0;
		int starta = 0;
		int startb = 0;
		fscanf(f, "%d\n", &turn);
		int na, nb;
		fscanf(f, "%d %d\n", &na, &nb);
		int i1, i2, i3, i4;
		for(j = 0; j < na; j++)
		{
			fscanf(f, "%d:%d %d:%d\n", &i1, &i2, &i3, &i4);
			nat[j].start = i1 * 60 + i2;
			nat[j].end = i3 * 60 + i4 + turn;
		}
		for(j = 0; j < nb; j++)
		{
			fscanf(f, "%d:%d %d:%d\n", &i1, &i2, &i3, &i4);
			nbt[j].start = i1 * 60 + i2;
			nbt[j].end = i3 * 60 + i4 + turn;
		}
		for(j = 0; j < 1440; j++)
		{
			for(k = 0; k < na; k++)
			{
				if(nat[k].end == j)
					idleb++;
			}
			for(k = 0; k < nb; k++)
			{
				if(nbt[k].end == j)
					idlea++;
			}
			for(k = 0; k < na; k++)
			{
				if(nat[k].start == j)
				{
					if(idlea == 0)
						starta++;
					else
						idlea--;
				}
			}
			for(k = 0; k < nb; k++)
			{
				if(nbt[k].start == j)
				{
					if(idleb == 0)
						startb++;
					else
						idleb--;
				}
			}
		}
		printf("Case #%d: %d %d\n", (i + 1), starta, startb);
	}
	fclose(f);
	return(0);
}