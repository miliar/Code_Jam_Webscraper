#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cstdlib>
using namespace std;
string next_num(string num)
{
		string s=num;
	if(next_permutation( num.begin(), num.end() ))
		return num;
	else
	{
		num=s;
		int len=num.length();
		bool temp;
		num.insert(0,1,48);
		temp=next_permutation( num.begin(), num.end() );
				/*
				s=num;
				while(s>=num)
				{
					cout<<num<<' '<<s<<'\n';
				//sort(num.begin(),num.end());
				temp=next_permutation( num.begin(), num.end() );

				}*/

		return num;
	}
}
int main()
{
	int num_cases;
	string num;
	cin>>num_cases;

	for(int i=0;i<num_cases;i++)
	{
		cin>>num;
		cout<<"Case #"<<i+1<<": "<<next_num(num)<<'\n';
	}
	return(0);
}




