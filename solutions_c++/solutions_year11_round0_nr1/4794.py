# include <cstdio>
using namespace std;

static const int MAX = 101;

struct BOT
{
	int dest[MAX], current, n;
}

ORANGE, BLUE;

long TIME;
bool type[MAX];


int sign(int val)
{
	if (val > 0)
		return 1;
	
	else
		return -1;
}

int abs(int val)
{
	if (val < 0)
		val = -val;
	
	return val;
}


void processTime(BOT *A, BOT *I)
{
	if (abs(I->dest[I->current]) > 1)
	{
		if (abs(I->dest[I->current]) > abs(A->dest[A->current]))
			I->dest[I->current] -= abs(A->dest[A->current]) * sign(I->dest[I->current]);
		
		else
			I->dest[I->current] = sign(I->dest[I->current]);
	}
	
	TIME += abs(A->dest[A->current]);
	A->current++;
}



int main()
{
	int T, N, i, p, k = 1;
	char ch[2];
	
	scanf("%d", &T);
	while (T--)
	{
		ORANGE.dest[0] = BLUE.dest[0] = 1;
		ORANGE.current = BLUE.current = 1;
		ORANGE.n = BLUE.n = 1;
		TIME = 0;
		
		scanf("%d", &N);
		for (i = 0; i < N; ++i)
		{
			scanf("%s", ch);
			scanf("%d", &p);
			
			if (ch[0] == 'O')
			{
				ORANGE.dest[ORANGE.n++] = p;
				type[i] = 1;
			}
			
			else
			{
				BLUE.dest[BLUE.n++] = p;
				type[i] = 0;
			}
		}
		
		for (i = ORANGE.n - 1; i > 0; --i)
			ORANGE.dest[i] = ORANGE.dest[i] - ORANGE.dest[i - 1] + sign(ORANGE.dest[i] - ORANGE.dest[i - 1]);
		
		for (i = BLUE.n - 1; i > 0; --i)
			BLUE.dest[i] = BLUE.dest[i] - BLUE.dest[i - 1] + sign(BLUE.dest[i] - BLUE.dest[i - 1]);
		
		for (i = 0; i < N; ++i)
		{
			if (type[i])
				processTime(&ORANGE, &BLUE);
			
			else
				processTime(&BLUE, &ORANGE);
		}
		
		printf("Case #%d: %ld\n", k, TIME);
		k++;
	}
	
	return 0;
}
