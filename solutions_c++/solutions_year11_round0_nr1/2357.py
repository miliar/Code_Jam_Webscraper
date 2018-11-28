#include <cstdio>

int main()
{
	int T, t, q_len, op_len, bp_len, i, O_pos, B_pos, O_act, B_act, seconds;
	bool b;
	char Q[110];
	short OP[110], BP[110];

	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &q_len);
		op_len = bp_len = 0;
		for (i = 0; i < q_len; i++)
		{
			scanf("%s", &Q[i]);
			if (Q[i] == 'O')
			{
				scanf("%d", &OP[op_len++]);
			}
			else
			{
				scanf("%d", &BP[bp_len++]);
			}
		}

		O_act = B_act = 0;
		O_pos = B_pos = 1;
		seconds = 0;
		for (i = 0; i < q_len; i++)
		{
			b = true;
			for (;b ; seconds++)
			{
				if (Q[i] == 'O' && OP[O_act] == O_pos)
				{
					O_act++;
					b = false;
				}
				else
				{
					if (OP[O_act] < O_pos)
					{
						O_pos--;
					}
					else if (OP[O_act] > O_pos)
					{
						O_pos++;
					}
				}

				if (Q[i] == 'B' && BP[B_act] == B_pos)
				{
					B_act++;
					b = false;
				}
				else
				{
					if (BP[B_act] < B_pos)
					{
						B_pos--;
					}
					else if (BP[B_act] > B_pos)
					{
						B_pos++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", t, seconds);
	}

	return 0;
}
