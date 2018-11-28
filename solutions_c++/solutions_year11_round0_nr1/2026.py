#include <cstdio>
#include <cstdlib>

int BO[200][2], BB[200][2];

int main()
{
	int cases;
	int N;
	scanf("%d", &cases);
	for (int C = 0; C < cases; C++)
	{
		int aux, o = 0, b = 0;
		char r;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%*c%c%d", &r, &aux);
			if (r == 'O')
			{
				BO[o][0] = i;
				BO[o][1] = aux;
				o++;
			}
			else
			{
				BB[b][0] = i;
				BB[b][1] = aux;
				b++;
			}
		}
		int bp = 1, op = 1;
		int bi = 0, oi = 0;
		int bd = 0, od = 0;
		int dist;
		int time = 0;
		for (int i = 0; i < N; i++)
		{
			if (bi != b && (oi == o || BB[bi][0] < BO[oi][0]))
			{
				dist = abs(bp - BB[bi][1]);
				bp = BB[bi][1];
				if (dist < bd)
				{
					od += 1;
					time += 1;
				}
				else 
				{
					od += dist - bd + 1;
					time += dist - bd + 1;
				}
				bi++;
				bd = 0;
			}
			else
			{
				dist = abs(op - BO[oi][1]);
				op = BO[oi][1];
				if (dist < od)
				{
					bd += 1;
					time += 1;
				}
				else 
				{
					bd += dist - od + 1;
					time += dist - od + 1;
				}
				oi++;
				od = 0;
			}
		}
		printf("Case #%d: %d\n", C+1, time);
	}
	return 0;
}