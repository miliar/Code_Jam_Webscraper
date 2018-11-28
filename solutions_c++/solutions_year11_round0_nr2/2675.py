#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ORANGE (0)
#define BLUE (1)

int C, D, N;

char Combine[30][30];
char Oppose[30][30];
char Seq[120];
char Answer[120];
int A_size;
int len;

int getidx(char c)
{
	return c - 'A' + 1;
}

void Input()
{
	int i, j;
	int a, b;
	char str[5];
	
	memset(Combine, 0, sizeof(Combine));
	memset(Oppose, 0, sizeof(Oppose));
	
	scanf("%d", &C);
	
	for(i = 1; i <= C; ++i)
	{
		scanf("%s", str);
		a = getidx(str[0]);
		b = getidx(str[1]);
		Combine[a][b] = Combine[b][a] = str[2];
	}
	
	scanf("%d", &D);
	
	for(i = 1; i <= D; ++i)
	{
		scanf("%s", str);
		a = getidx(str[0]);
		b = getidx(str[1]);
		Oppose[a][b] = Oppose[b][a] = 1;
		
	}
	
	scanf("%d", &N);
	
	scanf("%s", Seq);
	
#ifdef __DBGx
	for(i = 1; i <= 26; ++i)
	{
		for(j = 1; j <= 26; ++j)
		{
			printf("%c ",Combine[i][j]);
		}
		puts("");
	}
	
	puts("===================================");
	
	for(i = 1; i <= 26; ++i)
	{
		for(j = 1; j <= 26; ++j)
		{
			printf("%d ",Oppose[i][j]);
		}
		puts("");
	}
	
	puts("===================================");
	
#endif
}

int Counter[30];

void reset()
{
	int i;
	
	A_size = 0;
	
	for(i =0; i < 30; ++i)
		Counter[i] = 0;
}

void push(char c)
{
	Counter[ getidx(c) ]++;
	Answer[A_size++] = c;
}

void pop()
{
	Counter[ getidx(Answer[A_size - 1]) ]--;
	A_size --;
}

void Solve()
{
	int i, j, k;
	
	len = strlen(Seq);
	
	A_size = 0;
	reset();
	
	for(i = 0; i < len; ++i)
	{
		push(Seq[i]);
		
		/* combine */
			
		while( A_size > 1 )
		{
			int a, b;
			a = getidx(Answer[A_size-1]);
			b = getidx(Answer[A_size-2]);
			if( Combine[a][b] == 0 )
				break;
			
			pop();
			pop();
			push( Combine[a][b] );
		}
		
		/* oppose */
		
		bool flag = false;
		
		for(k = 1; k <= 26 && !flag; ++k)
		{
			if( Counter[k] == 0 )	continue;
			
			for(j = k+1; j <= 26 && !flag; ++j)
			{
				if( Counter[j] == 0 )	continue;
				
				if( Oppose[k][j] == 1 )
				{
					flag = true;
				}
			}
		}
			
		if( flag )
			reset();
			
	}
}

void Output(int t)
{
	printf("Case #%d: [", t);
	
	if( A_size > 0 )
		putchar(Answer[0]);
	for(int i = 1; i < A_size; ++i)
	{
		printf(", %c",Answer[i]);
	}
	puts("]");
}

int main()
{
	freopen("B-large.in","r",stdin);

	int turn, T;
	
	scanf("%d", &T);
	
	for(turn = 1; turn <= T; ++turn)
	{
		Input();
		
		Solve();
		
		Output(turn);
	}
}
