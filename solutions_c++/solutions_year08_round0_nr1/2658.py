#include <cstdio>
#include <cstring>
#include <cassert>

const int infinite = 99999;

inline void relax(int* node, int source, int target, int weight)
{
	if(node[target] > node[source] + weight)
		node[target] = node[source] + weight;
}

int main(int argc, char* argv[])
{
	int cases;
	int engines;
	int queries;
	char engine[100][101];
	int query[1000];
	int node[99001];
	FILE* f;
	int i, j, k;
	char temp[101];
	int len;
	f = fopen("A-small-attempt3.in", "r");
	//f = fopen("wat.in", "r");
	assert(f);
	fscanf(f, "%d\n", &cases);
	for(i = 0; i < cases; i++)
	{
		fscanf(f, "%d\n", &engines);
		for(j = 0; j < engines; j++)
		{
			fgets(engine[j], 100, f);
			len = strlen(engine[j]);
			if(engine[j][len - 1] == '\n')
				engine[j][len - 1] = 0;
		}
		fscanf(f, "%d\n", &queries);
		for(j = 0; j < queries; j++)
		{
			query[j] = -1;
			fgets(temp, 100, f);
			len = strlen(temp);
			if(temp[len - 1] == '\n')
				temp[len - 1] = 0;
			for(k = 0; k < engines; k++)
			{
				if(strcmp(temp, engine[k]) == 0)
				{
					query[j] = k;
					break;
				}
			}
			assert(query[j] != -1);
		}
		int low = infinite;
		if(queries > 0)
		{
			int n = 1 + queries * (engines - 1);
			node[0] = 0;
			for(j = 1; j < n; j++)
				node[j] = infinite;
			for(j = 0; j < n; j++)
			{
				for(k = 1; k < engines; k++)
					relax(node, 0, k, 0);
				for(int q = 0; q < (queries - 1); q++)
				{
					int si = 1 + q * (engines - 1);
					for(int se = 0; se < engines; se++)
					{
						if(se != query[q])
						{
							int ti = 1 + (q + 1) * (engines - 1);
							for(int te = 0; te < engines; te++)
							{
								int w;
								if(se == te)
									w = 0;
								else
									w = 1;
								if(te != query[q + 1])
								{
									relax(node, si, ti, w);
									ti++;
								}
							}
							si++;
						}
					}
				}
			}
			/*for(j = 0; j < n; j++)
			{
				printf("node %d value %d\n", j, node[j]);
			}*/
			for(j = n - engines + 1; j < n; j++)
			{
				//printf("node %d value %d\n", j, node[j]);
				if(node[j] < low)
					low = node[j];
			}
		}
		else
			low = 0;
		printf("Case #%d: %d\n", (i + 1), low);
	}
	fclose(f);
	return(0);
}