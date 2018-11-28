
#include <stdio.h>
#include <stdlib.h>

enum
{
	Orange = 0,
	Blue = 1,
	cNumCol
};

int search_next_pos(int curr_seq, int color, int N, int *seq_col, int *seq_idx)
{
	while (curr_seq < N)
	{
		if (seq_col[curr_seq] == color) return seq_idx[curr_seq];
		++curr_seq;
	}

	return -1;
}

int solve(int N, int *seq_col, int *seq_idx)
{
	int pos[cNumCol];
	pos[Orange] = 1; 
	pos[Blue] = 1;

	int step = 0;

	for (int seq=0; seq<N; ++seq)
	{
		int curr_color= seq_col[seq];
		int other_color = (curr_color == Orange) ? Blue : Orange;

		int next_pos[cNumCol];
		next_pos[Orange]	= search_next_pos(seq, Orange, N, seq_col, seq_idx);
		next_pos[Blue]		= search_next_pos(seq, Blue, N, seq_col, seq_idx);

		//

//		printf("| %3d | %3d |", pos[Orange], pos[Blue]);

		// move 

		int src = pos[curr_color];
		int dst = next_pos[curr_color];
		int move = (src > dst) ? src - dst : dst - src;

//		printf(" move %d\n", move);

		// move current color to destination and push button

		int cost = move + 1;

		{
			step += cost;
			pos[curr_color] = dst;
		}

		// move other color to destination by "cost"

		if (next_pos[other_color] != -1)
		{
			int dist = next_pos[other_color] - pos[other_color];
			if (dist < 0) dist = -dist;

			if (dist <= cost)
			{
				pos[other_color] = next_pos[other_color];
			}
			else
			{
				if (next_pos[other_color] > pos[other_color]) pos[other_color] += cost;
				else pos[other_color] -= cost;
			}
		}
	}

	return step;
}

int main()
{
	int T = 0;
	scanf("%d", &T);

	for (int t=0; t<T; ++t)
	{
		int N = 0;
		scanf("%d ", &N);

		// read sequence

		int seq_col[100];
		int seq_idx[100];

		for (int n=0; n<N; ++n)
		{
			char color = 0;
			int idx = 0;
			scanf("%c %d ", &color, &idx);

			seq_col[n] = (color == 'O') ? Orange : Blue;
			seq_idx[n] = idx;
		}

		// solve

		printf("Case #%d: %d\n", t+1, solve(N, seq_col, seq_idx));
	}
}
