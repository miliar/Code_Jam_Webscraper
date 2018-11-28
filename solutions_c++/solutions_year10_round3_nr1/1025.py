#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>


#include <stdio.h>
using namespace std;

#define rep(i,m) for( i=0;i<m;i++)
#define rep2(i,x,m) for(i=x;i<m;i++)
#define T_Max  15


int main ()
{
	int i,ii,j,iii,k,y,z;
	int N[T_Max],A[1000],B[1000];


  
    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
  
	int sum,temp,nodes;
	int T;//test cases number
	cin>>T;
     
	    rep(i,T)
		
			
		{
			
			cin>>N[i];

			nodes=0;

		rep(j,N[i])
		{cin>>A[j];cin>>B[j];}

		for(y=0;y<N[i];y++)
			for(z=0;z<y;z++)
				if(  ( A[y]>A[z] && B[y]<B[z] ) || ( A[y]<A[z] && B[y]>B[z] )  )
					nodes++;


		 cout<<"Case #"<<i+1<<": "<<nodes<<endl;

		}





		



   
  return 0;
}


