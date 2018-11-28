#include<iostream>
#include<cmath>

using namespace std;

int digits(int x);


int main()
{
	int num_cases,count,j,i,orig;
	cin>>num_cases;
	for (i=0;i<num_cases;i++)
	{
		count = 0;
		int llim, ulim;
		cin>>llim>>ulim;
		int num_dig = digits(llim);
		int val = pow(10,(num_dig-1));
		for(j=llim; j<=ulim; j++)
		{
			orig=j;
			for(int k=1; k<num_dig; k++)
			{
				int last = orig%10;
				int non_last = orig/10;
				orig = (last*val)+non_last;
				if ((j<orig)&&(orig<=ulim)&&(orig>=llim))
				{
					//cout<<j<<" "<<orig<<endl;
					count++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}

int digits(int x)
{
	int count = 0;
	while(x!=0)
	{
		x=x/10;
		count++;
	}
	return count;
}
	
