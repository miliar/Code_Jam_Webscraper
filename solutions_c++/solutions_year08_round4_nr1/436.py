#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <limits.h>

using namespace std;

#define LEFT(x) (2*(x))
#define RIGHT(x) (2*(x)+1)

#define MAX 20000

enum { GATE_AND, GATE_OR, TERMINAL};

struct node {
	int value;
	int gate;
	bool changeable;
};
node heap[MAX];

void init () {
}

//given a value, this returns the minimum number of switches
//we have to make on this node so that this becomes = value
//or -1 if impossible
int cache[MAX][2];
int getMin (int node, int value) {
	int result;
	if (heap[node].gate == TERMINAL) {
		if (value == heap[node].value)
			result = 0;
		else
			result = MAX+1;
	}

	else {
		if (cache[node][value] != -1) return cache[node][value];

		if (value == 0) {
			int min_and = min(
					getMin (LEFT(node), 0) + getMin (RIGHT(node), 0),
					min(getMin (LEFT(node), 1) + getMin (RIGHT(node), 0),
						getMin (LEFT(node), 0) + getMin (RIGHT(node), 1))
					);
			int min_or = getMin (LEFT(node), 0) + getMin (RIGHT(node), 0);

			if (heap[node].gate == GATE_AND) {
				if (!heap[node].changeable)
					min_or = MAX+1;
				else
					min_or++;
			}
			else {
				if (!heap[node].changeable)
					min_and = MAX+1;
				else
					min_and++;

			}

			result =  min(min_and, min_or);
		}
		if (value == 1) {
			int min_and = getMin (LEFT(node), 1) + getMin (RIGHT(node), 1);
			int min_or = min(
					getMin (LEFT(node), 1) + getMin (RIGHT(node), 1),
					min(getMin (LEFT(node), 0) + getMin (RIGHT(node), 1),
						getMin (LEFT(node), 1) + getMin (RIGHT(node), 0))
					);


			if (heap[node].gate == GATE_AND) {
				if (!heap[node].changeable)
					min_or = MAX+1;
				else
					min_or++;
			}
			else {
				if (!heap[node].changeable)
					min_and = MAX+1;
				else
					min_and++;

			}

			result = min(min_and, min_or);

		}

	}
	return cache[node][value] = result;
}


void solve (int _nn) {
	int m, v;
	scanf ("%d %d",&m,&v);

	memset (cache, -1, sizeof(cache));

	int k = 1;
	for (int i = 0; i < (m-1)/2; i++)
	{
		int g, c;
		scanf ("%d %d",&g,&c);
		if (g == 1) heap[k].gate = GATE_AND;
		else heap[k].gate = GATE_OR;
		heap[k].changeable = c;
		k++;
	}
	for (int i = 0; i < (m+1)/2; i++) {
		int l;
		scanf ("%d",&l);
		heap[k].value = l;
		heap[k].gate = TERMINAL;
		k++;
	}
	printf ("Case #%d: ",_nn);
	int res = getMin(1,v);
	if (res >= MAX+1) printf ("IMPOSSIBLE\n");
	else
		printf ("%d\n",res);
}

int main () {
	int cases;

	scanf ("%d",&cases);
	for (int i = 1; i <= cases; i++)
		solve (i);
}
