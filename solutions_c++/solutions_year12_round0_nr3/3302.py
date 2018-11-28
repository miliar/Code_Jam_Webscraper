#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("shift.out");
	int N;
	cin >> N;
	int s=0,k=0;
	for(int M = 1; M <= N; M++)
	{
		int C,I,r=0;		
		int a[7],b[7];
		cin>>C>>I;    
		k=0; 		
	for( int c=C;c<=I;c++)
	{
	    int t=1;
		for(int i=0;i<=6;i++)
		{
			a[i]=c/t%10;
			t=t*10;		
		}
		for(i=6;i>=0;i--)
		{
			if(a[i]!=0)
			{
				r=i;
				break;
			}
		}
	    for(int j=0;j<=r;j++ )
		 {  		
			s=0;
			for(i=r;i>=0;i--)
			{ 				
				s+=a[(i+j)%(r+1)];
		        s*=10;
			 }

			 s=s/10;
		     b[j]=s;
		
			 if (c<s&&s<=I)
			 {
				 k++;
			 }    
		 }
	for(i=0;i<=r;i++) 
		 for(int j=i+2;j<=r;j++)
		 if(b[i]==b[j])
		     {
				 if(c<b[i]&&b[i]<=I)
				   k--;
		      }
	  }
		cout<<"Case #"<<M<<": "<<k<<endl;	
	}	
	return 0;
}