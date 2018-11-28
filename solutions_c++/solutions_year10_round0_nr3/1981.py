#include<iostream>

using namespace std;

/*
n = number of groups
r = number of cycles
k = number of seats

*/

int main()
{
	long long int profit, sp[1001], grp[1001], prevsum,tc;
	int i=0, round[1001],c=0, prevstart=0, flag=0;
	int t,r,n,j,k;


	cin>>t;
	
	while(c++<t)
	{

		for(i=0;i<1001;i++)
		{
			round[i]= 0;
			sp[i] = 0;
		}
		cin>>r>>k>>n;
		i=0;
		while(i<n)
			cin>>grp[i++];

		j=0;
		profit = 0;
		prevsum=0;
		prevstart=0;
		flag=0;
		tc=0;
		int first =0;
		int myflag =1;

		for(i=0;i<r;i++)
		{	

			if(first ==1 && myflag==1)
			{
				first =0;
				myflag =0;
				int numofgroupinloop = round[j]-prevstart;
				long long int loopsum = sp[j]- prevsum;
				
				int leftcycle = r- i;
				profit += (leftcycle/numofgroupinloop) * loopsum;
				int remaining = leftcycle % numofgroupinloop;

				if(remaining == 0) break;
				i= r- remaining;  
			}
			
			tc=0;
			flag=n;
			while(flag && ((tc + grp[j]) <= k))
			{
				tc += grp[j++];
				if(j==n) j=0;
				flag--;
			}
			profit+=tc;
			
			if(sp[j] != 0 || j==0)
			{ 
				first =1;
				prevstart = round[j];
				prevsum= sp[j];
			}
			round[j]= i+1;
			sp[j] = profit;
//			cout<<"round"<<j<<" "<<round[j]<<" sp"<<j<<" "<<sp[j]<<"\n"; 	
		}	
		cout<<"Case #"<<c<<": "<<profit<<endl;
	}
return 0;
}
