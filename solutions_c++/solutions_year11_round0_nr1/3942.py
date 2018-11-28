#include <stdio.h>

struct command
{
	char bot;
	int pos;
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	command comm[100];
	int cases, numCase, N, posB, posO, i, idxB, idxO, P, walkB, walkO, walkComm;
	int B[100], O[100], seconds;
	char R;
	bool push;

	scanf("%i", &cases);
	for(numCase = 1; numCase <= cases; numCase++)
	{
		scanf("%i\n", &N);
		idxB = idxO = 0;
		for(i = 0; i < N; i++)
		{
			scanf("%c %i\n", &R, &P);
			if(R == 'B') { B[idxB++] = P; }
			else { O[idxO++] = P; }
			comm[i].bot = R;
			comm[i].pos = P;
		}

		posB = posO = 1;
		walkComm = 0;
		walkB = walkO = 0;
		seconds = 0;
		while(walkComm < N)
		{
			push = false;

			if(posB < B[walkB]) posB++;
			else if(posB > B[walkB]) posB--;
			else if(comm[walkComm].bot == 'B' && comm[walkComm].pos == posB) { push = true; walkB++; }
			
			if(posO < O[walkO]) posO++;
			else if(posO > O[walkO]) posO--;
			else if(comm[walkComm].bot == 'O' && comm[walkComm].pos == posO) { push = true; walkO++; }

			if(push)
				walkComm++;
			seconds++;
		}

		printf("Case #%i: %i\n", numCase, seconds);
	}

	return 0;
}