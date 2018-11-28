#include <cstdlib>
#include <iostream>

using namespace std;

long long vine[10000][2];
bool bReach[10000][10000];

int cmp(const void* a, const void* b)
{
 	if (((int*)a)[0] >((int*)b)[0]) return 1;
 	return -1;
}

int queue[5000000][2];
int h, t;

int main(int argc, char *argv[])
{
 	int nc;
 	scanf("%d", &nc);
 	for (int cid = 1; cid <= nc; cid++)
 	{
	 	printf ("Case #%d: ", cid);
	 	int N;
        long long D;
	 	scanf("%d", &N);
	 	for (int i =0 ; i < N; i++)
	 	{
		 	scanf ("%lld%lld", &vine[i][0], &vine[i][1]);
		}
	 	scanf("%lld", &D);
	 	qsort(vine, N, sizeof(long long) * 2, cmp);
	 	
	 	memset(bReach, 0, sizeof(bReach));
	 	h = 0; t = 1;
	 	queue[0][0] = 0;	// at which x
	 	queue[0][0] = 0;	// hold which vine
	 	bool bDone = false;
	 	
	 	while(h < t && !bDone)
	 	{
	 		int x = queue[h][0];
	 		int vId = queue[h][1];
	 		long long vX = vine[vId][0];
	 		
	 		//printf ("x %d v %lld %lld\n", x, vine[vId][0], vine[vId][1]);
	 		h++;
	 		
	 		if (vX + vX - x >= D)
	 		{
			   	   bDone = true;
			   	   break;
			}
	 		
	 		for (int i = vId+1; i < N; i++)
	 		{
			 	if (vine[i][0] <= vX + (vX - x))
			 	{
	    		   if (!bReach[i][vId])
	    		   {
		   			   bReach[i][vId] = true;
		   			   if (vine[i][0] - vX <= vine[i][1])
		   			   {
		   			   	  queue[t][0] = vX;
					   }
					   else
					   {
					   	   queue[t][0] = vine[i][0] - vine[i][1];
					   }
		   			   queue[t][1] = i;
		   			   t++;
				   }
				}
				else
				{
				 	break;
				}
			}
 		}
 		if (bDone)
 		{
    	  puts ("YES");
        }
        else
        {
		 	puts ("NO");
		}
	}
    return EXIT_SUCCESS;
}
