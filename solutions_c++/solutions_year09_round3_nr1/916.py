#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
using namespace std;
unsigned long long min_base(string s)
{
	int len=s.length();
	int num_count=0,ch_count=0;
	int base;
	vector<bool> num(10,false);
	vector<bool> ch(26,false);
	vector<char> index_num(10,-1);
	vector<char> index_ch(26,-1);
	string result;
	for(int i=0;i<len;i++)
	{
		if(isdigit(s[i]))
		{
			if(!num[s[i]-48])
			{
				num[s[i]-48]=true;
				num_count++;
			}
		}
		else
		{

			if(!ch[s[i]-97])
			{
				ch[s[i]-97]=true;
				ch_count++;
			}
		}
	}
	base=ch_count+num_count;
	if(base==1)
		base++;
	result=s;
	if(isdigit(result[0]))
	{
		index_num[result[0]-48]=49;
	}
	else
		index_ch[result[0]-97]=49;
	result[0]=49;
	int index=1;
	char temp,val;
	while(index<len)
	{
		temp=result[index];

		if(isdigit(temp))
		{
			if(index_num[temp-48]==-1)
			{
				index_num[temp-48]=48;
				result[index]=48;

				break;
			}
			else
				result[index]=index_num[temp-48];

		}
		else
		{
			if(index_ch[temp-97]==-1)
			{
				index_ch[temp-97]=48;
				result[index]=48;
				break;
			}
			else
				result[index]=index_ch[temp-97];
		}
		index++;

	}
	index++;
	val=49;
	for(;index<len;index++)
	{
		temp=result[index];
		if(isdigit(temp))
		{
			if(index_num[temp-48]==-1)
			{
				val++;
				index_num[temp-48]=val;
				result[index]=val;
			}
			else
			{
				result[index]=index_num[temp-48];
			}
		}
		else
		{
			if(index_ch[temp-97]==-1)
			{
				val++;
				index_ch[temp-97]=val;
				result[index]=val;
			}
			else
			{
				result[index]=index_ch[temp-97];
			}

		}
	}
	unsigned long long carry=0,n=1,sol=0;
	for(int i=len-1;i>=0;i--)
	{
		temp=result[i];
		sol=sol+n*(temp-48);
		n=n*base;
	}




//	cout<<result<<'\n';
	return sol;	
}

int main()
{
	string s;
	int num_cases;
	cin>>num_cases;
	for(int i=0;i<num_cases;i++)
	{
		cin>>s;
		cout<<"Case #"<<i+1<<": "<<min_base(s)<<'\n';
	}
	return(0);
}



		
	


			



	



				




