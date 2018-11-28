#include "stdafx.h"
#include <iostream> 
#include <math.h>
#include <stdio.h> 
#include <string.h>

using namespace std;



 int main ()
{
	long long int  n_raod, i, l, k, j, indic;
	long long int min_snap;
	long long int Number,N,K;
	
    cin >> n_raod;  

	for (l=0; l<n_raod; l++)
	{
		 cin >> N >> K;
	
		 min_snap=0;
	
		 for (i=1; i<=N; i++)
		{
			min_snap =  2*min_snap+1;
		}

	indic = 0;
	if (K<min_snap) 
		{
			indic = 1;
		}
	else if ((K-min_snap)%(min_snap+1)!=0 ) {indic = 1;}

	

	  if (indic == 0) 
	 {
		 cout << "Case #"<<l+1 <<": ";
		 cout <<"ON";
		 cout << "\n";
	 }
	 else 
	 {
		cout << "Case #"<<l+1 <<": ";
		cout <<"OFF";
		cout << "\n";
	 }

	indic = 0;	 
	// cout << "Case #"<<l+1 <<": ";
	// cout <<N<< " " <<K;
	// cout << "\n";
	  
	
}
	 return 0;

}
 