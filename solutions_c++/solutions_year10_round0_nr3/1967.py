#include "stdafx.h"
#include <iostream> 
#include <math.h>
#include <stdio.h> 
#include <string.h>

using namespace std;



 int main ()
{
	long long int  n_raod, i, l,j, indic;
	long long int group [1001], sum[1001], next_ind[1001];
	long long int R,k,N,ind, answer, t;
	
    cin >> n_raod;  

	for (l=0; l<n_raod; l++)
	{
		 cin >> R >> k >> N;
		 
		 for (i=0; i<N; i++)
		 {
			 group[i]=0;
			 sum[i]=0;
			 next_ind[i]=0;
		 }
		 
		 for (i=0; i<N; i++)
		 {
			 cin >> group[i]; 
		 }
	
		 
		for (i=0; i<N; i++)
		{
			ind=i; sum[i]=group[i];
			while ((i!=(ind+1)%N) && sum[i]+group[(ind+1)%N]<=k)
			{sum[i]=sum[i]+group[(ind+1)%N]; ind++;}
			
			next_ind[i]=(ind+1)%N;
		}
		
		t=0; answer=0;
		for (i=0; i<R; i++)
		{
			answer=answer+sum[t];
			t=next_ind[t];
		}
		

		 cout << "Case #"<<l+1 <<": ";
		 cout <<answer;
		 cout << "\n";
		 
		 for (i=0; i<N; i++)
		 {
			 group[i]=0;
			 sum[i]=0;
			 next_ind[i]=0;
		 }
	 
		
	}
	 return 0;

}
 