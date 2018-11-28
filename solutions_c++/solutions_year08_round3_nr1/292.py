#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int F[1000];
int main()
   {
      int N;
	  scanf("%d", &N);
	  for(int caso=1;caso<=N;caso++)
	     {
		    int P,K,L;
			scanf("%d%d%d", &P,&K,&L);
			for(int i=0;i<L;i++)
			   scanf("%d", &F[i]);
			sort(F,F+L);
			reverse(F,F+L);
			long long total=0;
			for(int i=0;i<L;i++)
			   {
			      total+=(long long)(F[i])*(long long)(1+i/K);
			   }
			cout<<"Case #"<<caso<<": "<<total;
			if(caso<N)
			   cout<<"\n";
		 }
      return 0;
   }
