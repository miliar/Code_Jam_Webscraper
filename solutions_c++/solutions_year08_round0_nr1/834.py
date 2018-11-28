#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

#define nmax 101
#define qmax 1001
#define INF 100000
using namespace std;

int N, S, Q;

string query[qmax];
string engine[nmax];
char tStr[nmax];
int implode[qmax][nmax];
int turn[qmax][nmax];
int i, j, k,l;
map<string, int> sMap;

void init()
{
     for(j=0; j<qmax; j++)
        for(k=0; k<nmax; k++)
           turn[j][k] = implode[j][k] = 0;
     sMap.clear();
     scanf("%d\n", &S);
     for(j=0; j<S; j++)
     {
         gets( tStr );
         string str(tStr); 
         sMap[str] = j+1;
         engine[j] = str;
     }
    
     scanf("%d\n", &Q);
     for(j=0; j<Q; j++)
     {
         gets( tStr );
         string str(tStr);
         query[j] = str;
         int index = sMap[str];
         if (index > 0)
            implode[j][index-1] = INF;
     }
 }
 
 int solve()
 {
     turn[0][sMap[query[0]]-1] = INF;
     for(j=1; j<Q; j++)
     {
		 for(l=0; l < S; l++)
		 {
			 int min = INF;
			 int minIndex = -1;
			 int index = sMap[query[j]]-1;

			 if (implode[j][l] != INF)
			 {
				 for(k=0; k < S; k++)
				 {
					 if (l == k)
					 {
						 if (turn[j-1][k] < min)
						 {
							 min = turn[j-1][k];
							 minIndex = k;
						 }
					 }
					 else
					 {
						 if ( (turn[j-1][k]+1) < min)
						 {
							 min = turn[j-1][k]+1;
							 minIndex = k;
						 }
					 }
				 }
			 }
			 turn[j][l] = min;
           //  printf("%d ", turn[j][l]);
		 }
                 
      //   printf("\n");

     }

	 int min = INF;
	 for(k=0; k<S; k++)
	 {
		if (turn[Q-1][k] < min)
			min = turn[Q-1][k];
	 }
	 return min;
 }

int main()
{
 //   freopen("1.in", "r", stdin);
   // freopen("1.out", "w", stdout);
     
     scanf("%d", &N);

     for(i=0; i<N; i++)
     {
         init();
         int res = solve();
         printf("Case #%d: %d\n", i+1, res);		 
     }
    
    return 0;
}
