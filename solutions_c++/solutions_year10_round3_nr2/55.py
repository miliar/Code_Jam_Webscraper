#include<iostream>
#include<vector>
using namespace std;
vector<int> parts;
int fac;
int num(int n)
{
	int cnt=0;
	while(n)
	{
		n/=2;
		cnt++;
	}
	return cnt;
}
	
	
	
main()
{
	int test,i;
	cin>>test;
	for(i=1;i<=test;i++)
	{
		int low,high;
		cin>>low>>high>>fac;
		//parts.push_back(high);
		while(high/fac >= low)
		{
			if((high%fac)==0 && (high/fac)==low)
			break;
			if((high%fac)==0)
			parts.push_back(high/fac);
			else
			parts.push_back(high/fac + 1);
			high=parts.back();
		}
		//parts.push_back(low);
	//	for(int j=0;j<parts.size();j++)
		//cout<<parts[j]<<" ";
		cout<<"Case #"<<i<<": "<<num(parts.size())<<endl;
		parts.clear();
	}
}
		
			
			
	
