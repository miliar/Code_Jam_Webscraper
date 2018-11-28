#include<iostream>
#include<fstream>
#include <vector>
#include <algorithm>

using namespace std;


int length(long num)
{
	int len=0;
	while(num!=0)
	{	
		num=num/10;	
		len++;
	}
	return len;
}

int main()
{
		
	freopen("C-large.in","rt",stdin);
	freopen("output3.out","wt",stdout);
	int totalCases;
	long A,B;
	long m,n,temp;
	scanf("%d",&totalCases);
	char ch;
	scanf("%c",&ch);
	for(int i=0;i<totalCases;i++)
	{
		scanf("%ld",&A);
		scanf("%c",&ch);
		scanf("%ld",&B);
		scanf("%c",&ch);
		int palCounter=0;
		int len=length(A);
		int counter=0;
		
		for(long n=A;n<B;n++)
		{
			m=n;
			palCounter=0;
			long pal[20];
			for(int k=0;k<len-1;k++)
			{
				
				int tempm=m%10;
				m=m/10;
				long temppow=1;				
				for(int x=0;x<len-1;x++)
					temppow=temppow*10;
			 
				m=m+temppow*tempm;	
		
				if((!(m<A || m > B)) && m > n)
				{
					
					     if(palCounter==0)
					     {
						pal[palCounter]=m;
						palCounter=palCounter+1;
						counter++;
					     }
					     else
					     {
						     bool flag=true;
						     for(int y=0;y<palCounter;y++)
						     {
								if(pal[y]==m)
								{ 
									flag=false;
									break; 
								}

						     }
						     if(flag)
						     {					         	
							    pal[palCounter++]=m;
							    counter++;
						     }
					     }

				}
								
			}
		}

		printf("Case #%d: %d",(i+1),counter);
		printf("\n");
	}
}













