

#if 1
#include <iostream>

using namespace std;

#define MAX_COUNT  30

typedef struct _SWITCHER
{
	int power;
	int state;
}SWITCHER;

void init(SWITCHER array[], int n)
{
	int i = 0;

	for(; i<n; i++)
	{
		array[i].power = 0;
		array[i].state = 0;
	}

	array[0].power = 1;
}

int main()
{

	freopen ("A-small-attempt3.in", "r", stdin);
    freopen ("A-small-attempt3.out", "w", stdout);

	int times = 0;
	int index = 1;

	scanf("%d", &times);
	
	SWITCHER chain[MAX_COUNT];

	while(times--)
	{
		int n = 0;
		int k = 0;
		int i, j;

		scanf("%d%d", &n, &k); 
		
		init(chain, n);

		for(i=0; i<k; i++)
		{
			for(j=0; j<n; j++)
			{
				if(chain[j].power)
					chain[j].state = chain[j].state ? 0 : 1;
			}

			for(j=0 ;j<n; j++)
			{
				if(chain[j].state && chain[j].power)
					chain[j + 1].power = 1;
				else
					chain[j + 1].power = 0;
			}
		}

		if(chain[n - 1].power && chain[n - 1].state)
			printf("Case #%d: ON\n", index++);
		else
			printf("Case #%d: OFF\n", index++);
	}
	return 0;
}
#endif

