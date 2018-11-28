#include <stdio.h>

#define min(a,b) ((a) < (b) ? (a) : (b))

int T, P, finals;
int M[1024];

typedef struct match_s
{
	int price;
	int ticket;
	match_s* winner;
	match_s* left;
	match_s* right;
} match;

match matches[1023];

void clear()
{
	for (int i = 0; i < 1023; i++)
	{
		matches[i].price = 0;
		matches[i].ticket = 0;
		matches[i].winner = NULL;
		matches[i].left = NULL;
		matches[i].right = NULL;
	}
}

void tree()
{
	int k = 0;
	for (int i = 0; i < P; i++)
	{
		for (int j = 0; j < (1 << (P - i - 1)); j++)
		{
			int m;
			scanf("%d", &m);
			matches[k].price = m;
			
			int next = (k / 2) + (1 << (P - 1));
			matches[k].winner = &(matches[next]);
			
			k++;
		}
	}
	finals = k - 1;
	matches[finals].winner = NULL;
}

void leftright(match* m, match* pointer)
{
	if (m == NULL)
		return;
	if (m->left == NULL)
		m->left = pointer;
	else //if (m.right == NULL)
		m->right = pointer;
	leftright(m->winner, m);
}

int visit(match* m, int number)
{
	if (m == NULL)
		return 0;
	int v = visit(m->winner, number);
	int todo = number - v;
	if (m->ticket == 1 || todo <= 0)
		return v;
	
	m->ticket = 1;
	return v + 1;
}

int price(match* m)
{
	if (m == NULL)
		return 0;
	int p = m->price * m->ticket;
	p += price(m->left);
	p += price(m->right);
	return p;
}

int numVisits(match* m)
{
	if (m == NULL)
		return 0;
	int v = m->ticket;
	v += numVisits(m->winner);
	return v;
}

void solve(int n)
{
	clear();
	tree();
	for (int i = 0; i < (1 << (P - 1)); i++)
	{
		leftright(&(matches[i]), NULL);
	}
	for (int i = 0; i < P; i++)
	{
		for (int j = 0; j < (1 << (P - 1)); j++)
		{
			if (M[2 * j] == i)
			{
				visit(&(matches[j]), P - M[2 * j] - numVisits(&(matches[j])) );
				//printf("   %d %d\n", i, j); for debugging info
			}
		}
	}
	int p = price(&(matches[finals]));
	printf("Case #%d: %d\n", n, p);
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &P);
		for (int j = 0; j < (1 << P); j++)
		{
			scanf("%d", &(M[j]));
			if (j % 2 == 1)
			{
				M[j - 1] = min(M[j], M[j - 1]);
			}
		}
		solve(i + 1);
	}
	return 0;
}

