#include <stdio.h>
#include <iostream>
using namespace std;
int tab[1000];
#define rep(I,N) for(I = 0; I < N; I++)
int main()
{
	int Z,N,L,H;
	cin>>Z;
	int i,j,l;
	rep(i,Z)
	{
		cin>>N>>L>>H;
		rep(j,N)
		{
			 cin>>tab[j];
		}
		j = L;
		bool good = 0;
		int numb = 0;
		for(j = L; j <= H; j++)
		{
			rep(l,N) 
			{
				if((tab[l] % j) == 0 || (j % tab[l]) == 0) 
				{
					good = 1;							
				}
				else
				{
					 good = 0;
					break;
				}	
			}
			if(good)
			{
				 numb = j;
				break;
			}
			
		}
		cout<<"Case #"<<i + 1<<": ";
		if(numb == 0) cout<<"NO"<<endl;
		else cout<< numb<<endl;
	}
	return 0;
}
				
				


