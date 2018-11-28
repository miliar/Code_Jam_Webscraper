#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int n,s,p,t,div,rem;
	
	int T;cin>>T;
	
	
	
	for(int test_case=1;test_case<=T;test_case++)
	{
		cin>>n;cin>>s;cin>>p;
		int sure_one=0;
	
		int sure_zero=0;
		int maybe_zero=0;
	
		int sure_two=0;
		int maybe_two=0;
		int total_maybe=0;
		
		for(int i=0;i<n;i++)
		{
			cin>>t;
			
			div=t/3;
			rem=t%3;
			
			if(rem==1)
			{
				div++;
				if(div>=p) sure_one++;
			}
			
			else if(rem==0)
			{
				if(t!=0)
				{
					if(t==30) sure_zero++;
					else if(div>=p) sure_zero++;
					else if(div==p-1) maybe_zero++;
				}
				else if(p==0) sure_zero++;
			}
			
			else
			{
				div++;
				if(div>=p) sure_two++;
				//else if(div+1==p) maybe_two++;
				else if(div==p-1) maybe_two++;
			}
		}	
		total_maybe=maybe_two+maybe_zero;
		if(s<total_maybe)
		{
			cout<<"Case #"<<test_case<<": "<<s+sure_one+sure_zero+sure_two<<endl;
		}
		else cout<<"Case #"<<test_case<<": "<<total_maybe+sure_one+sure_zero+sure_two<<endl;
			
		
		
	}
	
	
	return 0;
}
