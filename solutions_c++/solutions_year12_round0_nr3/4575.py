#include<iostream.h>
#include<math.h>
int main()
{
	int a,b,t,i,j,l,p,rem,d,qu,count=0,m,n;
	cin>>t;
	for(m=1;m<=t;m++)
	{   count=0; 
		cin>>a>>b;
		n=a;
		for(i=0;n>0;i++)
		n=n/10;
		
		l=i;
		
		
		for(i=a;i<=b;i++)
 	{       n=i; 
			p=10; d=pow(10,l-1);
			for(j=1;j<l;j++)
			{rem=n%p;
			qu=n/p;
			if(rem*d+qu<=b&&i<rem*d+qu)
			{count++;
			
			}
			p=p*10;
			d=d/10;
			}
 	}
 	cout<<"Case #"<<m<<": "<<count<<endl;
	}
	return 0;
}
