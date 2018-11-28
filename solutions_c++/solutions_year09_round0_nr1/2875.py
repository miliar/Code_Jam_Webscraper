#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<map>

using namespace std;


int main()
{
	int n,d,i,j,num=0,flag=0,found=1,pos;
	int l,counter;
	map <string,int> m;
	map<string,int>::iterator iter;
	vector <string> vec;
	int a[20][26];

	cin>>l>>d>>n;
	string str,empty;
	counter=0;
	int check[20][26];
	for(i=0;i<l;i++)
		for(j=0;j<26;j++)
			a[i][j]=0;
	
	for(i=0;i<d;i++)
	{
		cin>>str;
		vec.push_back(str);
		m[str]=1;
		for(j=0;j<str.size();j++)
			a[j][str[j]-'a']=1;
	}
	
	while(n--)
	{
		cin>>str;
		num++;
		counter=0;
		pos=0;
		string temp;
		for(i=0;i<l;i++)
			for(j=0;j<26;j++)
				check[i][j]=0;
		flag=0;
		j=0;
		int first=0;
		while(j<str.size())
		{
			if(str[j]==')')
			{
				flag=0;		
			}
			else if(str[j]=='(')
			{
				flag=1;
				if(first!=0)
					pos++;
				else 
					first++;
			}
			else if(str[j]>='a' && str[j]<='z')
			{
				
			   if(flag==1)
			   {
				temp+=str[j];
				check[pos][str[j]-'a']=1;
			   }
			else if(flag==0)
			{
				if(first!=0)
					pos++;
				else 
					first++;
				check[pos][str[j]-'a']=1;
				
			}
			}
			j++;
		}
		
		
				
		for(i=0;i<vec.size();i++)
		{
			found=1;
			for(j=0;j<l;j++)
			{
				if(check[j][vec[i][j]-'a']==0)
				{
					found=0;
					break;
				}
			}
			if(found==1)
				counter++;
		}
		
		
		cout<<"Case #"<<num<<": "<<counter<<endl;
	}
}



	
	
	
	 
	
		
		
		
		
