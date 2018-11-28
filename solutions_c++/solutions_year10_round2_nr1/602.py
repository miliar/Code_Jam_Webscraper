#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>

using namespace std;
int N,M;
int coun;
map<string,int> MAP;

void fun(string str)
{
//	cout<<"str "<<str<<endl;
	if(str=="")
		return;
	if(MAP.find(str)!=MAP.end())
		return;
	
	int len= str.length();
	int j=len-1;

	int start=j;
	while(str[j]!='/')
		j--;

	string temp="";
	for(int k=0;k<j;k++)
	{
		temp+=str[k];
	}

	if( MAP.find(temp)== MAP.end())
	{
		fun(temp);
	}

	for(int k=j;k<=start;k++)
		temp+=str[k];
	MAP[temp]=1;
	coun++;
//	cout<<temp<<" "<<coun<<endl;
	return;
}


int main()
{
	int notimes;
	scanf("%d",&notimes);

	for(int cp=1;cp<=notimes;cp++ )
	{
		
		int answer=0;
		cin>>N>>M;
		string str;
		
		MAP.clear();
		string cons="/";
		MAP[cons]=1;

		for(int i=0;i<N;i++)
		{
			cin>>str;
			MAP[str]=1;
		}
		coun=0;

		for(int i=0;i<M;i++)
		{
			cin>>str;
			fun(str);
		}	
				
		answer=coun;			
			
			
		cout<<"Case #"<<cp<<": "<<answer<<endl;
	}
	return 0;
}
