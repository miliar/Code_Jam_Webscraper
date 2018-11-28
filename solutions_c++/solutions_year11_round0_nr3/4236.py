#include<iostream>

using namespace std;

int main()
{
	int t,val,min,sum;
	int n,i;
	
	unsigned int a[2000];
	
	cin>>t;
	int 
	t1=1;
	while(t1<=t)
	{
		cin>>n;
		sum=val=0;
		min=1000000;
		
		
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			val^=a[i];
			if(min>a[i])
				min=a[i];
			
			sum+=a[i];
		}
		
		if(val!=0)
		cout<<"Case #"<<t1<<": "<<"NO"<<endl;
		
		else
		{
			sum-=min;
			cout<<"Case #"<<t1<<": "<<sum<<endl;
		}
		t1++;
	}
	
	return 0;
}
		
		
		
