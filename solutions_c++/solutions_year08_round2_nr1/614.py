#include <stdio.h>
#include <iostream>
using namespace std;

long long X[100];
long long Y[100];
int main()
   {
      int N;
	  scanf("%d", &N);
	  for(int caso=1;caso<=N;caso++)
	     {
		    long long n,A,B,C,D,x0,y0, M;
			cin>>n>>A>>B>>C>>D>>x0>>y0>> M;
			//scanf("%ld%ld%ld%ld%ld%ld%ld%ld", &n,&A,&B,&C,&D,&x0,&y0,&M);
			X[0]=x0;
			Y[0]=y0;
			for(int i=1;i<n;i++)
			   {
			      X[i]=(A*X[i-1]+B)%M;
				  Y[i]=(C*Y[i-1]+D)%M;
			   }
			int count=0;
			for(int i=0;i<n;i++)
			   for(int j=i+1;j<n;j++)
			      for(int k=j+1;k<n;k++)
				    {
					   long long cx=X[i]+X[j]+X[k];
					   long long cy=Y[i]+Y[j]+Y[k];
					   if((cx%3==0) && (cy%3==0))
					      count++;
 					}
			printf("Case #%d: %d", caso, count);
			if(caso<N)
			   printf("\n");
		 }
      return 0;
   }
