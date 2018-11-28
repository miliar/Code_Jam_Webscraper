#include <stdio.h>
#include <stdlib.h>

struct q
{
	int a;
	struct q *next;
}	*head, *curr, *tail;

void push(int a)
{
	curr = (struct q*)malloc(sizeof(struct q));
	curr -> a = a;
	if (!head)
		head = tail = curr;
	else
	{
		tail -> next = curr;
		tail = curr;
	}
	tail -> next = head;
}

void popall()
{
	tail -> next = NULL;
	while (head)
	{
		curr = head;
		head = head -> next;
		free(curr);
	}
}

int main()
{
	int x, n, jml, p, it, q, r, k;
	
	scanf("%d", &q);
	for (int f = 0; f < q; f++)
	{
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &x);
			push(x);
		}
		curr = head;
		p = 0; it = 0;
		while (it < r)
		{
			jml = 0; x = 0;
			while (x < n)
			{
				jml += curr -> a;
				if (jml > k)
				{
					jml -= curr -> a;
					break;
				}
				else
					curr = curr -> next;
				x++;
			}
			p += jml;
			it++;
		}
		printf("Case #%d: %d\n", f+1, p);
		popall();
	}
	return 0;
}
