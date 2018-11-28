//Program By ganesh:1pi06cs032
#include<iostream>
#include<map>
#include<string>
using namespace std;

int main()
{
	int temp=0;
	string str[5000];
	string  blank("");
	int cnt=0;
	int Length,Data,name,m;

	cin>>Length>>Data>>name;
	m=name;
	for(int i=0;i<Data;i++)
	{
		cin>>str[i];
	}
	while(name--)
	{
		string str1,s[5000];
		map<char,int> arr[500];
		cin>>str1;
		
			for(int i=0;i<Length;i++)
			{
				int temp=str1.find_first_of(")");
				if(i>=Length){temp=1;break;}
				if(str1[0]=='(')
				{
				string str2(str1.begin()+1,str1.begin()+temp);
				string str3(str1.begin()+temp+1,str1.end());
				s[i]=str2;
				str1=str3;
				}
				else
				{
				s[i]=str1[0]+blank;
				string str3(str1.begin()+1,str1.end());
				str1=str3;
				}
			  for(int i1=0;i1<s[i].length();i1++)
			    	arr[i][s[i][i1]]=1;
			}
			
			
			for(int i1=0;i1<Data;i1++)
			{
				int j1;
				for(j1=0;j1<Length;j1++)
				{
					if(arr[j1][str[i1][j1]]!=0)
						;
					else
						break;
				}
				if(j1==Length)
					cnt++;
			}
			cout<<"Case #"<<m-name<<": "<<cnt<<endl;
			cnt=0;
			temp=0;
	}
   return 0;	
}
