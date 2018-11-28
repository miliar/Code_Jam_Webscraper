#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int t,n,c,pt,sum,smallest,flag;
	vector<int> bin;
	vector<int> num;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		num.clear();
		bin.clear();

		for(int j=0;j<20;j++)
		{
			bin.push_back(0);
		}
	
		for(int j=0;j<n;j++)
		{
			cin>>c;
			num.push_back(c);
			pt=0;
			while(c)
			{
				bin[pt]=(bin[pt]+(c%2))%2;
				pt++;
				c/=2;
			}
		}
		flag=0;
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;j<bin.size();j++)
		{
			//cout<<bin[j];
			if(bin[j]!=0)
			{
				cout<<"NO"<<endl;
				flag=1;
				break;
			}
		}//cout<<endl;
		if(flag)
		{
			continue;
		}
		else
		{
			smallest=num[0];
			sum=0;
			for(int j=0;j<num.size();j++)
			{
				if(smallest>num[j])
					smallest=num[j];
				sum+=num[j];
			}
			cout<<sum-smallest<<endl;
		}
		
	}
	return 0;
}
