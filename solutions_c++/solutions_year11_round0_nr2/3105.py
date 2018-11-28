#include<stdio.h>
#include<string.h>

#define MAX_LEN 1024
char Com[256][256];
char Opp[256][256];
char Inp[MAX_LEN];
int C, D, N;
char Result[MAX_LEN];
int NRes = 0;

void read_input()
{
	char c1, c2, c3;
	for (int x = 0; x < 256; x++)
		for (int y = 0; y < 256; y++)
		{
			Com[x][y] = 0;
			Opp[x][y] = 0;
		}
	for (int x = 0; x < MAX_LEN; x++)
		Inp[x] = 0;
	
	scanf("%d", &C);
	for (int c = 0; c < C; c++)
	{
		scanf(" %c%c%c", &c1, &c2, &c3);
		Com[c1 - 'A'][c2 - 'A'] = c3;
		Com[c2 - 'A'][c1 - 'A'] = c3;
	}

	scanf("%d", &D);
	for (int d = 0; d < D; d++)
	{
		scanf(" %c%c", &c1, &c2);
		Opp[c1 - 'A'][c2 - 'A'] = 1;
		Opp[c2 - 'A'][c1 - 'A'] = 1;
	}

	scanf("%d", &N);
	for (int n = 0; n < N; n++)
	{
		scanf(" %c", &c1);
		Inp[n] = c1;
	}
}

void invoke(char c)
{
	if (NRes == 0)
	{
		Result[0] = c;
		NRes++;
		return;
	}

	if (Com[Result[NRes-1] - 'A'][c - 'A'] != 0)
	{
		Result[NRes-1] = Com[Result[NRes-1] - 'A'][c - 'A'];
		return;
	}
	
	for (int x = 0; x < NRes; x++)
		if (Opp[Result[x] - 'A'][c - 'A'] == 1)
		{
			NRes = 0;
			return;
		}

	Result[NRes] = c;
	NRes++;
	return;
}

void show_current()
{
	for (int y = 0; y < NRes; y++)
		printf("%c", Result[y]);
	printf("\n");
}

void process()
{
	NRes = 0;
	for (int x = 0; x < N; x++)
	{
		//printf("\nCurrent: ");
		//show_current();
		//printf("     Invoking: %c\n", Inp[x]);
		invoke(Inp[x]);
	}
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++)
	{
		read_input();
		//if (t != 3) continue;
		process();
		printf("Case #%d: ", t);
		if (NRes == 0)
		{
			printf("[]\n");
			continue;
		}
		if (NRes == 1)
		{
			printf("[%c]\n", Result[0]);
			continue;
		}
		printf("[%c", Result[0]);
		for (int c = 1; c < NRes; c++)
			printf(", %c", Result[c]);
		printf("]\n");
	}
	return 0;
}
