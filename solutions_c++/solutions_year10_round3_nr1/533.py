#include <stdio.h>
#include <stdlib.h>

typedef struct wire
{
	int inicio;
	int fim;
	int posi;
	int posf;
}wire;

int comparai(const void * a, const void * b)
{
	wire * a1 = (wire *)a;
	wire * b1 = (wire *)b;
	return (a1->inicio - b1->inicio);
}


int comparaf(const void * a, const void * b)
{
	wire * a1 = (wire *)a;
	wire * b1 = (wire *)b;
	return (a1->fim - b1->fim);
}

wire wires[1000];

int main()
{
	int casos;
	scanf("%d", &casos);
	for (int c = 1; c <= casos; c++)
	{
		int N, res = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d %d", &wires[i].inicio, &wires[i].fim);
		}
		qsort(wires,  N, sizeof(wire), comparaf);
		for (int i = 0; i < N; i++)
		{
			wires[i]. posf = i;
		}
		qsort(wires,  N, sizeof(wire), comparai);
		for (int i = 0; i < N; i++)
		{
			if (i < wires[i].posf)
				res += wires[i].posf - i;
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
