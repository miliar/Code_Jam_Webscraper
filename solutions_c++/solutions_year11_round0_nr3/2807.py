#include <stdio.h>
#include <stdlib.h>
#define ORANGE (0)
#define BLUE (1)

const int MAX = 1000 + 10;

int N;
int seq[MAX];
bool answer;
int best;

void Input()
{
	int i;
	
	scanf("%d", &N);
	
	for(i = 1; i <= N; ++i)
	{
		scanf("%d", &seq[i]);
	}
}

int p_sum(int a, int b)
{
	return (a^b);
}

int calc(int s)
{
	int i = 1;
	int s1, s2;
	int real;
	
	#ifdef __DBG
		printf("%d\n",s);
	#endif
	
	s1 = s2 = 0;
	real = 0;
	
	for(i = 1; i <= N; ++i)
	{
		if( (s&1)==0 )
		{
			real += seq[i];
			s1 = p_sum(s1, seq[i]);
		}
		else
		{
			s2 = p_sum(s2, seq[i]);
		}
		s >>= 1;
	}
	
	//printf("(%d, %d)\nreal = %d\n",s1,s2,real);
	
	if( s1 == s2 )
		return real;
	return -1;
}

void Solve()
{
	int i, b;
	int temp;
	
	b = (1 << N) - 1;
	answer = false;
	best = 0;
	
	for(i = 1; i < b; ++i)
	{
		temp = calc(i);
		if( temp != -1 )
		{
			if( !answer || best < temp )
			{
				answer = true;
				best = temp;
			}
		}
	}
}

void Output(int t)
{
	printf("Case #%d: ", t);
	
	if( !answer )
		puts("NO");
	else
		printf("%d\n",best);
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);

	int turn, T;
	
	scanf("%d", &T);
	
	for(turn = 1; turn <= T; ++turn)
	{
		Input();
		
		Solve();
		
		Output(turn);
	}
}
