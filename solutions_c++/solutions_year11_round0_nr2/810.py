#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int C,N;
vector<string> form;
vector<string> clear;

char combine(string& list,char& ch1,char& ch2)
{
	for(int c=0;c<C;c++)
	{
		if(ch1==form[c][0] && ch2==form[c][1])
		{
			//ch1=form[c][2];
			//ch2=' ';
			return form[c][2];
		}
		else if(ch2==form[c][0] && ch1==form[c][1])
		{
			//ch1=form[c][2];
			//ch2=' ';
			return form[c][2];
		}
	}
	return ' ';
}

bool allclear(string& list,char ch0)
{
	for(int n=0;n<N;n++)
	{
		if(clear[n][0]==ch0)
		{
			for(int k=0;k<list.size();k++)
				if(clear[n][1]==list[k])
					return true;
		}
		if(clear[n][1]==ch0)
		{
			for(int k=0;k<list.size();k++)
				if(clear[n][0]==list[k])
					return true;
		}
	}
	return false;
}

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		cin>>C;
		form.assign(C,"");
		for(int i=0;i<C;i++)
			cin>>form[i];
		
		cin>>N;
		clear.assign(N,"");
		for(int i=0;i<N;i++)
			cin>>clear[i];
		
		int D; cin>>D;
		string str; cin>>str;
		
		string list("");
		for(int t=0;t<D;t++)
		{
			//cerr<<(str[t])<<": "<<list<<endl;
			if(t>0)
			{
				char& ch0=list[list.size()-1];
				char combined=combine(list,ch0,str[t]);
				if(combined!=' ')
				{
					//cerr<<"\tcomb "<<combined<<endl;
					ch0=combined;
					continue;
				}
				
				bool result2=allclear(list,str[t]);
				if(result2==true)
				{
					//cerr<<"\tall clear "<<endl;
					list.clear();
					continue;
				}
			}
			//cerr<<"\tpush "<<str[t]<<endl;
			list.push_back(str[t]);
		}
		//cerr<<list<<endl;
		
		printf("Case #%d: [",ds);
		for(int i=0;i<list.size();i++)
		{
			printf("%c",list[i]);
			if(i+1!=list.size())
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
