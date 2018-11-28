#include <iostream.h>
#include <fstream.h>
#include <string.h>
int main()
{
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("out.txt");
	int i,j,k,m=0,n=0,L,D,N,result=1,tem=1,start=0,end=0;
	infile>>L>>D>>N;
	int d[75000];
	char *a[75000];
	char*b = new char[75000];
	char*c = new char[75000];
	for( i = 0 ;i<D;i++ )
	{
		a[i]=new char[L+1];
		infile>>a[i];
	}
	
	for(j=0; j<N ; j++)
	{		
		infile>>b;	

		result=0;
		
		for(i=0;i<D;i++)
		{
			start=0;
			end=0;
			m=0;
			tem=0;
			for(k=0;k<500;k++)
				d[k]=0;

			for( k=0; k<strlen(b) ; k++)
			{										
				if(b[k] == a[i][m])
					d[m]=1;	
				
				if(b[k] == '(' )
				{			
					start=1;
				}
				if(b[k] == ')' )
				{			
					end=1;
				}
				if(start == end)
				{
					start=0;
					end=0;
					m++;
				}		
			}
			for(n=0;n<L;n++)
				tem+=d[n];
			if(tem == L) result++;
		}
		outfile<<"Case #"<<j+1<<": "<<result<<endl;
		
	}
	infile.close();
	outfile.close();
	return 0;
}
