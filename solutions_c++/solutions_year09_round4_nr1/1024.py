#include <algorithm>
#include <cstdio>
#include <queue>
using namespace std;

main()
{
 int T;
 scanf("%d",&T);
 
 for(int t=1; t <= T; t++)
 {
   int N;
   scanf("%d",&N);
   vector<vector<int> > M(N,vector<int>(N,0));
   char buf[41]; 
   for(int i=0; i < N; i++)
    {
    scanf("%s\n",buf);
    for(int j=0; j < N; j++)
    M[i][j]=buf[j]-'0';
    }
	int c=0;	
	for(int i=0; i < N; i++)
	{
		int k=i+1;	
		for(; k < N; k++)
		if(M[i][k] == 1)
		break;
		if(k == N)
		continue;
		
		for(int j=i+1; j < N; j++)
		{
		   int kd=i+1;	
		   for(; kd < N; kd++)
		   if(M[j][kd] == 1)
		   break;
		   if(kd == N)
		   {
		   	c+=j-i;
		    vector<int> ls=M[j];
		    for(int d=j; d > i; d--)
		    M[d]=M[d-1]; 
		    M[i]=ls;
		    break;
     	   }	
		}
	}   
	printf("Case #%d: %d\n",t,c);
 }

 
}


