#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
char buffer[200];
bool A[1000][100];
int M[1000][100];
int main()
   {
	   int N;
		scanf("%d", &N);
		for(int caso=1;caso<=N;caso++)
		    {
			    int S,Q;
				 scanf("%d\n", &S);
				 vector<string> engines;
				 for(int i=0;i<S;i++)
				    {
					    gets(buffer);
						 engines.push_back(buffer);
					 }
				 scanf("%d\n", &Q);
				 for(int i=0;i<Q;i++)
				    for(int j=0;j<S;j++)
					    A[i][j]=true;
				 for(int i=0;i<Q;i++)
				    {
					    gets(buffer);
						 string s=buffer;
						 for(int j=0;j<S;j++)
						    if(engines[j]==s)
							    {
								    A[i][j]=false;
									 break;
								 }
					 }
				 if(Q==0)
					 {
				       printf("Case #%d: %d", caso, 0);
						 if(caso<N)
				          printf("\n");
						 continue;
					 }
				 
				 for(int j=0;j<S;j++)
				    M[Q-1][j]=1-A[Q-1][j];
				 for(int i=Q-2;i>=0;i--)
				    for(int j=0;j<S;j++)
					    {
						    M[i][j]=Q;
							 for(int k=0;k<S;k++) if(A[i][k])
							    M[i][j]=MIN(M[i][j], M[i+1][k]+((j!=k)?1:0));
						 }
				 int best=M[0][0];
				 for(int i=1;i<S;i++)
				    best=MIN(best, M[0][i]);
				 printf("Case #%d: %d", caso, best);
				 if(caso<N)
				    printf("\n");
			 }
	   return 0;
	}






