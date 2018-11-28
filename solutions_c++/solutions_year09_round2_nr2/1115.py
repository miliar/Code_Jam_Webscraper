#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;


main()
{
	long long int num,temp;
	vector<int> am(10,0);
	string str="",S;
	int T;
	
	cin >> T;
	for(int i=0;i<T;i++)
	{
		cin >>S;
		str=S;
		int len=str.length();
		//cout<<len<<'\n';	
		for(int j=0;j<10;j++)am[j]=0;
		for(int j=0;j<len;j++)am[str[j]-'0']++;	
		//for(int j=0;j<10;j++)cout<<am[j]<<' ';
		//	cout<<'\n';	
		
		cout<<"Case #"<<i+1<<": ";
		if(next_permutation(str.begin(),str.end()))
		{
			cout<<str<<'\n';
		}
		else
		{
			int count=0,flag=0;
			am[0]++;
			for(int j=0;j<10;j++)
			{
				if(count==0 && am[j]>0 && j!=0)
				{
					cout<<j;
					for(int k=0;k<am[0];k++)cout<<"0";
					for(int k=0;k<am[j]-1;k++)cout<<j;
					count++;
				}
				else if(am[j]>0 && j!=0)
				{ 
					
					for(int k=0;k<am[j];k++)cout<<j;
					count++;
					
				}
			}	
				cout<<'\n';
					
		}
		
	}
}
			
			
	
		
		
		
