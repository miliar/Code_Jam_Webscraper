#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef struct{
	int b, e, w;
}tipo;

#define MAX 1024

tipo v[MAX];

int fc (const void *e1, const void *e2)
{
	tipo *p1 = (tipo *)e1;
	tipo *p2 = (tipo *)e2;
	
	return (p1->w - p2->w);
}

int main()
{
	int cas, casos;
	int x, s, r, T, n;
	double t;
	int i;
	int anda;
	
	double resp;
	 double temp;
	
	scanf("%d", &casos);
	
	for (cas = 1; cas <= casos; cas++)
	{
		printf("Case #%d: ", cas);
		
		scanf("%d %d %d %d %d", &x, &s, &r, &T, &n);
		t = T;
		anda = x;
		resp = 0.0;
		
	
		
		for (i=0; i<n; i++)
		{
			scanf("%d %d %d", &v[i].b, &v[i].e, &v[i].w);
			anda -= v[i].e-v[i].b;
		}

		qsort(v, n, sizeof(v[0]), fc);

		if (t > 0)
		{
			temp = anda / (double) r;
			if (temp <= t)
			{
				resp += temp;
				t-=temp;
				anda = 0;
			}
			else {
				anda -= r*t;
				resp += t + anda/(double)s;
				t = 0;
				anda = 0;
			}

		}
		else
			resp += anda / (double) s;
		

		for (i=0; i<n; i++)
		{
			if (t > 0)
			{
				temp = ((double) (v[i].e-v[i].b) )/(v[i].w + r);
				if (temp <= t)
				{
					t -= temp;
					resp+= temp;
				}
				else {
					resp += t + ((double) (v[i].e-v[i].b) - t*(v[i].w + r))/(v[i].w + s);
					t = 0.0;
				}

			}
			else {
				resp += ((double) (v[i].e-v[i].b) )/(v[i].w + s); 
			}

		}
		printf("%.9f\n", resp);

	}
	
	return 0;
}
