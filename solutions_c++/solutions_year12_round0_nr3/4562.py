#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

int no_of_digits(int n)
{   int cnt=0;
	if(n==0)
		return 1;
	while(n)
	{
		cnt++;
		n=n/10;
	}
   return cnt;		  
}
int main()
{
	ifstream fin("C-small-attempt0.in",ios::in);
	ofstream fout("outputcs.txt",ios::out);

	int A,B,n,m,mod,d,t,count[55]={},flag=1,tst=0;

	fin>>t;
	
	while(fin>>A>>B)
	{
		
		
		if(no_of_digits(A)==no_of_digits(B))
		{	d=no_of_digits(A);
		    flag=0;
		}

		for(int i=A;i<=B;i++)
		{
			
			n=i;
		    if(flag)
				d=no_of_digits(n);
			for(int j=1;j<=d;j++)
			{
				mod=n%int((pow(10.0,j)));

				mod=mod*int(pow(10.0,(d-j)));

				m = mod+n/int(pow(10.0,j));
				
				if(m<=B&&m>n&&n!=m)
						count[tst]++;
				}
		}
		tst++;
	}
	
	for(int i=0;i<t;i++)
		fout<<"Case #"<<i+1<<": "<<count[i]<<endl;

	
}