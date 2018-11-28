#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<string>
#include<stack>
using namespace std;
vector<string> arr;
int l,d,n;
vector<string> lang;

int traverse(string token,vector<string> &aalang,int posn)
{
	//for(int i=0;i<aalang.size();i++)cout<<aalang[i]<<" ";cout<<endl;
	
	token = arr[posn];
	//cout<<token<<" "<<aalang.size()<<endl;
	vector<string> newlang;
	for(int i=0;i<(int)token.length();i++)
	{
		
		for(int j=0;j<(int)aalang.size();j++)
		{
				if(token[i]==aalang[j][posn])
				{newlang.push_back(aalang[j]);}
		}
		
	}if(newlang.size()==0){cout<<"0\n";return 0;}
	//for(int i=0;i<aalang.size();i++)cout<<aalang[i]<<" ";cout<<endl;
	if(posn==l-1){cout<<aalang.size()<<endl;return 0;}
	
	traverse(arr[posn+1],newlang,posn+1);
	
}	
//a(ab)(bc)  (27*15)  + (5000*15*27)*500 = ...
void procc(string temp)
{
	int i=0;string str;
	
	while(i!=((int)temp.length()))
	{
		
		str="";
		if(temp[i]=='(')
		{	i++;
			while(temp[i]!=')')
			{str=str+temp[i];i++;}
			
		}else if(temp[i]!='('){str=str+temp[i];}
		arr.push_back(str);
		i++;
	}
	//for(int i=0;i<arr.size();i++)cout<<arr[i]<<" ";cout<<endl;
	int ct=0;
	int flag1=0,flag2=0,j=0,k=0;
	for(i=0;i<d;i++)
	{
		
		flag1=0;
		for(j=0;j<(int)lang[i].length();j++)
		{	
			//cout<<lang[i]<<endl;
			flag2=0;
			
			for(k=0;k<(int)arr[j].length();k++)
			{

				if(lang[i][j]==arr[j][k])
				{flag2=1;}
			}
			if(flag2==1)continue;
			if(flag2==0){flag1=1;break;}
			
		}
		//cout<<lang[i]<<endl;
		if(flag1==0){ct++;}
	}
	cout<<ct<<endl;	
	//traverse(arr[0],lang,0);
}

			
int main()
{
	string temp;
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;i++)
	{
		cin>>temp;
		lang.push_back(temp);
		
	}
	for(int i=0;i<n;i++)
	{
		cin>>temp;
		arr.clear();
		cout<<"Case #"<<i+1<<": ";
		procc(temp);
	}
	return 0;
}
