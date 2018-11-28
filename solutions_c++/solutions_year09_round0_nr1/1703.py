#include<iostream>
#include<map>
using namespace std;


int main()
{
	int L,D,N;
	string array[5001],str;
	int number[5001];
	cin>>L>>D>>N;
	for(int i=0;i<D;i++)
	{
		cin>>array[i];
		number[i]=0;
	}
	int count=0;
	for(int i=1;i<=N;i++)
	{
		cin>>str;
		count=0;
		int j=0;
		int flag=0;
		int ans=0;
		for(int k=0;k<D;k++)
			number[k]=0;
		while(str[j]!='\0')
		{
			if(str[j]=='(')
			{
				flag=1;
			}
			else if(str[j]==')')
			{
				count++;
				flag=0;		
			}
			else
			{
				for(int k=0;k<D;k++)
				{
					if(array[k][count]==str[j])
						number[k]++;
				}
				if(flag==0)
				{
					count++;
				}
			}
			j++;
		}
		
		for(int k=0;k<D;k++)
		{
			if(number[k]==L)					
				ans++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;	
	}
	return 0;
}
		
	
