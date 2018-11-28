#include <stdio.h>
#include <stdlib.h>
#define ORANGE (0)
#define BLUE (1)

int N;
int time;

int seq[100 + 10];
int Act[2][100];
int cnt[2];

int ABS(int x)
{
	if( x < 0 )
		return (-x);
	return x;
}

int getidx(char c)
{
	if( c=='O' )
		return ORANGE;
	else if ( c=='B')
		return BLUE;
	else	abort();
}

void Input()
{
	int i;
	char str[3];
	int x;
	int idx;
	
	scanf("%d", &N);
	
	cnt[ORANGE] = cnt[BLUE] = 0;
	
	for(i = 1; i <= N; ++i)
	{
		scanf("%s%d", str, &x);
		
		idx = getidx(str[0]);
		
		seq[i] = idx;
		Act[idx][cnt[idx]++] = x;
	}
}

void Solve()
{
	int i;
	int head[2], pos[2];
	int dx[2];
	int idx, rev;
	
	head[ORANGE] = head[BLUE] = 0;
	pos[ORANGE] = pos[BLUE] = 1;
	
	time = 0;
	
	for( i = 1; i <= N; ++i )
	{
	#ifdef __DBG
		printf("next actions:\n");
		printf("ORANGE: %d\nBLUE: %d\n",Act[ORANGE][head[ORANGE]], Act[BLUE][head[BLUE]]);
		printf("Acc_time = %d\n",time);
		
		puts("");
		printf("pos->\nORAGNE: %d\nBLUE: %d\n",pos[0], pos[1]);
		puts("----------------===");
	#endif
		idx = seq[i];
		
		dx[0] = 1 + ABS(pos[idx] - Act[idx][head[idx]]);
		time += dx[0];
		
		pos[idx] = Act[idx][head[idx]++];
		
		// another pipe
		rev = (idx ^ 1);
		
		if( head[rev] >= cnt[rev] )
			continue;
		
		dx[1] = ABS(pos[rev]- Act[rev][head[rev]]);
		if( dx[0] >= dx[1] )
		{
			pos[rev] = Act[rev][head[rev]];
		}
		else
		{
			if( pos[rev] < Act[rev][head[rev]] )
			{
				pos[rev] += dx[0];
			}
			else
			{
				pos[rev] -= dx[0];
			}
		}
		
	}
}

void Output(int t)
{
	printf("Case #%d: %d\n", t, time);
}

int main()
{
	freopen("A-large.in","r",stdin);

	int turn, T;
	
	scanf("%d", &T);
	
	for(turn = 1; turn <= T; ++turn)
	{
		Input();
		
		Solve();
		
		Output(turn);
	}
}
