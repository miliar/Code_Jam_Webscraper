#include <cstdlib>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>

using namespace std;

typedef struct {
		double x, y;
		bool bSet;
		int id;
		double r;
} ENTRY;

ENTRY e[1000];

int dcmp(const void* _a, const void* _b)
{
 	double a = ((ENTRY*)_a)->r;
 	double b = ((ENTRY*)_b)->r;
 	if (a > b) return -1;
 	if (a == b) return 0;
	return 1;
}

int icmp(const void* _a, const void* _b)
{
 	int a = ((ENTRY*)_a)->id;
 	int b = ((ENTRY*)_b)->id;
 	if (a > b) return 1;
 	if (a == b) return 0;
	return -1;
}

int main(int argc, char *argv[])
{
 	int nCase;
 	scanf("%d", &nCase);
 	for (int cId = 1; cId <= nCase; cId++)
 	{
	 	int N, W, L;
	 	scanf ("%d%d%d", &N, &W, &L);
	 	for (int i = 0; i < N; i++)
	 	{
		 	scanf ("%lf", &e[i].r);
		 	e[i].id = i;
		 	e[i].bSet = false;
		}
		qsort(e, N, sizeof(ENTRY), dcmp);
				
		printf ("Case #%d:", cId);
		
		int nPreSet = 1;
		e[0].x = e[0].y = 0;
		double lastX = 0, lastY = e[0].r;
		for (int i = nPreSet; i < N; i++)
	 	{
		 	if (lastY + e[i].r <= L)
		 	{
		       e[i].x = 0;
		       e[i].y = lastY + e[i].r;
		  	   nPreSet++;
		  	   lastY += 2*e[i].r;
		    }
		    else
		    {
			 	break;
			}
		}
		lastX = e[0].r, lastY = 0;
		for (int i = nPreSet; i < N; i++)
	 	{
		 	if (lastX + e[i].r <= W)
		 	{
		       e[i].x = lastX + e[i].r;
		       e[i].y = 0;
		  	   nPreSet++;
		  	   lastX += 2*e[i].r;
		    }
		    else
		    {
			 	break;
			}
		}
		//printf ("nPreSet %d N %d\n", nPreSet, N);
		
		srand(time(NULL));
		rand();
		while(true)
		{
            int count = 0;
			for (int i = nPreSet; i < N && count <= N * 1000; )
			{
			 	double x, y;
			 	x = W * ((double)rand() / RAND_MAX);
			 	y = L * ((double)rand() / RAND_MAX);
			 	
			 	bool bCrash = false;
			 	for (int j = 0; j < i; j++)
			 	{
				 	if (sqrt((e[j].x - x) * (e[j].x - x) + (e[j].y- y) * (e[j].y - y)) < e[i].r + e[j].r)
				 	{
 					   bCrash = true;
 					   break;
					}
				}
				
				count++;
				if (!bCrash)
				{
 				   e[i].x = x;
 				   e[i].y = y;
  	   			   i++;
				}
			}
			if (count <= N * 1000) break;
		}
		qsort(e, N, sizeof(ENTRY), icmp);
		for (int i =0 ; i < N; i++)
		{
		}
		for (int i =0 ; i < N; i++)
		{
		 	printf (" %f %f", e[i].x, e[i].y);
		}
	 	printf ("\n");
	}

//    system("PAUSE");
    return EXIT_SUCCESS;
}
