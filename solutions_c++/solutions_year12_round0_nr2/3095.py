	#include <iostream>
	#include <stdio.h>
	using namespace std;
	int main()
	{
	int tab[100];
	int t,n,s,p;
	scanf ("%d", &t);
	for (int j=1;j<=t;j++)
	{
		int ile=0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
		for (int i=0;i<n;i++)
		{
		scanf("%d",&tab[i]);
		if (s)
		{
			//cout<<"sprawdzam "<<tab[i]<<" w s"<<endl;
			
			if (tab[i]/3+tab[i]%3>=p && tab[i]%3<2)
			{
				//cout<<"sprawdzam "<<tab[i]<<" bez odejmowania"<<endl;
				
			ile++;	
			}
			else if (tab[i]/3+1>=p && tab[i]%3==2)
			ile++;
			else if (tab[i]/3+tab[i]%3>=p)
			{
				if (tab[i]%3==2)
				s--;
			ile++;	
			}
			
			else if (tab[i]/3>=p-1 && tab[i]%3==0 && tab[i]/3)
			{
				ile++;
				s--;
				
			}
				
		}
		else
		{
			if (tab[i]/3+tab[i]%3>=p && tab[i]%3<2)
			{
				//cout<<"sprawdzam "<<tab[i]<<" bez odejmowania"<<endl;
				
			ile++;	
			}
			else if (tab[i]/3+1>=p && tab[i]%3==2)
			ile++;
			
		}
		
	}
	printf("Case #%d: %d\n",j,ile);
		
		
		
		
		
	}
	
	
	}
	
