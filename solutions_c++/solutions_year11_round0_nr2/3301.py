#include <iostream>
#define MAX_COMBINE 40
#define MAX_OPPOSED 40
#define MAX_INVOKE 100

using namespace std;

struct Combine
{
	char a, b, c;	
};

struct Opposed
{
	char a, b;
};

void clear();

int T, N, C, D;
int currentTC = 1;

Combine combs[MAX_COMBINE];
Opposed opps[MAX_OPPOSED];
char invoke[MAX_INVOKE];
int invokedElements[100] = {0};

void clean()
{
	for (int i = 0; i < 100; ++i)
	{
		invokedElements[i] = 0;
	}
}

int main()
{
	freopen("magicka.in", "r", stdin);
	freopen("magicka.out", "w", stdout);
	
	scanf("%d", &T);
	for(int i = 0; i < T; ++i)
	{
		scanf("%d", &C);
		for(int j = 0; j < C; ++j)
		{
			Combine c;
			scanf(" %c%c%c", &c.a, &c.b, &c.c);
			combs[j] = c;
		}
		
		scanf("%d", &D);
		for(int j = 0; j < D; ++j)
		{
			Opposed o;
			scanf(" %c%c", &o.a, &o.b);
			opps[j] = o;
		}
		
		char c;
		scanf("%d", &N);
		scanf("%c", &c); // Ready empty space
		int currentPos = -1;
		clean();
		for(int j = 0; j < N; ++j)
		{
			bool opDone = false;
			scanf("%c", &c);
			invokedElements[(int) c]++;
			
			// check for combinations
			for(int k = 0; k < C && currentPos != -1; ++k)
			{
				if ((c == combs[k].a && invoke[currentPos] == combs[k].b) ||
					(c == combs[k].b && invoke[currentPos] == combs[k].a))
				{
					invoke[currentPos] = combs[k].c;
					invokedElements[(int) combs[k].a]--;
					invokedElements[(int) combs[k].b]--;
					opDone = true;
					break;
				}
			}
			if (opDone) continue;
			
			// check for opposites
			for(int k = 0; k < D && currentPos != -1; ++k)
			{
				if (invokedElements[(int) opps[k].a] && invokedElements[(int) opps[k].b])
				{
					currentPos = -1;
					clean();
					opDone = true;
					break;
				}
			}
			
			if (!opDone)
			{
				invoke[++currentPos] = c;
			}
		}
		
		printf("Case #%d: [", currentTC++);
		if (currentPos >= 0) printf("%c", invoke[0]);
		for(int j = 1; j <= currentPos; ++j)
		{
			printf(", %c", invoke[j]);
		}
		printf("]\n");
	}
}