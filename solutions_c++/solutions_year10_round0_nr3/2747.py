//roller coaster

#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

uint32_t r, k, n;
uint32_t *g, *a, *c, *e;
uint64_t *b, *d;
void UpdateABC(uint32_t);
void UpdateDE(uint32_t);

int main()
{
	uint32_t t;
	uint32_t i, j, delta, q, caseno;
  uint64_t dollars;
	
	std::cin>>t;
	
	for (caseno = 1; caseno <= t; ++caseno)
	{

		std::cin >> r >> k >> n;
		g = (uint32_t*) malloc(n * sizeof(uint32_t));
		a = (uint32_t*) malloc(n * sizeof(uint32_t));
		b = (uint64_t*) malloc(n * sizeof(uint64_t));
		c = (uint32_t*) malloc(n * sizeof(uint32_t));
		d = (uint64_t*) malloc(n * sizeof(uint64_t));
		e = (uint32_t*) malloc(n * sizeof(uint32_t));

		memset(a, 0, (n * sizeof(uint32_t)));
		memset(b, 0, (n * sizeof(uint64_t)));
		memset(c, 0, (n * sizeof(uint32_t)));
		memset(d, 0, (n * sizeof(uint64_t)));
		memset(e, 0, (n * sizeof(uint32_t)));

		for(i=0;i<n;i++)
			std::cin >> g[i];

		dollars = 0;
		i = 0; j = 1;
		while (j<=r)
		{
			if (a[i] == 0)
			{
				UpdateABC(i);
				dollars += b[i];
				i = c[i];
				j++;
			}
			else
			{
				if (d[i] == 0)
					UpdateDE(i);

				delta =  r-j+1;
				if (e[i] <=  delta)
				{
					q = (delta / e[i]);
					dollars += q * d[i];
					j += q * e[i];
        }
				while (j <= r)
				{
					dollars += b[i];
					i = c[i];
					j++;
				}
			}
		}

		std::cout << "Case #" << caseno << ": " <<  dollars << "\n";
		
		free(a);
		free(b);
		free(c);
		free(d);
		free(e);			
		free(g);			
	}
	return 0;
}

void UpdateABC(uint32_t i)
{
	uint32_t sum = 0;
  uint64_t j = i, w = 0, v;
	while (w < n)
	{
		v = sum + g[j];
		if (v <= k)
		{
			sum = v;
			j = (j+1) % n;
			w++;
		}
		else
			break;
	}
	a[i] = (n+j-i) % n;
	b[i] = sum;
	c[i] = j;
}

void UpdateDE(uint32_t i)
{
	uint32_t j = i;
	do
	{
		d[i] += b[j];
		j = c[j];
		e[i]++;
	}
	while (j != i);
}

