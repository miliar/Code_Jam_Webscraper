#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

long test,cases=1,N,K;
char graph[100][100];

void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}


bool win(char b)
{
	long k,m;
    for(long i=0;i<N;i++)
	   for(long j=0;j<N;j++)
	   {
		   if(graph[i][j]!=b)
			   continue;
		   if(j+K<N)
		   {
			   for(k=j;k<=j+K;k++)
			 {
				 if(graph[i][k]!=b)
					 break;
			 }
			   if(k==j+K+1)
				   return true;
		   }




		   if(i+K<N)
		   {
			   for(k=i;k<=i+K;k++)
			 {
				 if(graph[k][j]!=b)
					 break;
			 }
			   if(k==i+K+1)
				   return true;
		   }



		   if(i+K<N && j+K<N)
		   {
			   for(k=i,m=j;k<=i+K;k++,m++)
			 {
				 if(graph[k][m]!=b)
					 break;
			 }
			   if(k==i+K+1)
				   return true;
		   }


		   if(i+K<N && j-K>=0)
		   {
			   for(k=i,m=j;k<=i+K;k++,m--)
			 {
				 if(graph[k][m]!=b)
					 break;
			 }
			   if(k==i+K+1)
				   return true;
		   }




	   }


	   return false;
}

int main()
{
	SetInputFile();
	
	char tempGraph[100][100];

	scanf("%ld",&test);
	while(test--)
	{
		scanf("%ld%ld",&N,&K);

		memset(graph,0,sizeof(graph));
		memset(tempGraph,0,sizeof(tempGraph));
		for(long i=0;i<N;i++)
			scanf("%s",tempGraph[i]);

		
			for(long j=0;j<N;j++)
				for(long i=0;i<N;i++)
			{
				graph[j][i] = tempGraph[N-i-1][j];
			}

			
			bool exists = false;
			for(long j=0;j<N;j++)
			for(long i=N-1;i>=0;)
			{				
				if(graph[i][j] == '.')
				{
					exists = false;
					for(long k=i;k>0;k--)
					{
						if(graph[k-1][j]!='.')
							exists = true;
						graph[k][j] = graph[k-1][j];
					}
					graph[0][j] = '.';

					if(!exists)
						i=-1;
				}
				else
				{
					i--;
				}
			}

			K--;
			bool winB = win('B');
			bool winR = win('R');

			if(winB & winR) printf("Case #%ld: Both\n",cases);
			else if(winB)printf("Case #%ld: Blue\n",cases);
			else if(winR)printf("Case #%ld: Red\n",cases);
			else printf("Case #%ld: Neither\n",cases);


			cases++;

	}

	return 0;
}
