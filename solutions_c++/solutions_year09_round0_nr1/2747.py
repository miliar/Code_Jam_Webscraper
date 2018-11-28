#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
#define f 1
void getAnswer(vector<string> v1,vector<string> v2,int add,string s,int& num)
{
	if(add==v1.size())
	{
		if(find(v2.begin(),v2.end(),s)>=v2.end())
			;
		else
			num++;
		return;
	}
	bool isPossible=false;
	for(int i=0;i<v1[add].length();i++)
	{
		for(int j=0;j<v2.size();j++)
		{
			if(v2[j][add]==v1[add][i])
			{
				isPossible=true;break;
			}
		}
		if(isPossible)
		{
			s+=v1[add][i];
			getAnswer(v1,v2,add+1,s,num);
			s=s.substr(0,s.length()-1);
			isPossible=false;
		}
	}
}
int main()
{	
	int L,D,N;
	vector<string> lib;
	vector<string> c;
	string temp="";
#if f
	fstream fs1("A-large.in",fstream::in);
	if(!fs1)
	{
		cerr<<"read error"<<endl;
		return 1;
	}
	
	fs1>>L>>D>>N;
	while(D--)
	{
		fs1>>temp;
		lib.push_back(temp);
	}
	int num=N;
	while(num--)
	{
		fs1>>temp;
		c.push_back(temp);

	}
	fs1.close();
	fstream fs2("out.out",fstream::out);
	if(!fs2)
	{
		cerr<<"write error"<<endl;
		return 1;
	}
	
#else
	cin>>L>>D>>N;
	while(D--)
	{
		cin>>temp;
		lib.push_back(temp);
	}
	int num=N;
	while(num--)
	{
		cin>>temp;
		c.push_back(temp);

	}
#endif
	int count;
	string s;
	vector<string> vec;
	for(int i=1;i<=N;i++)
	{
		vec.clear();
		count=0;
		s=c[i-1];
		bool isLeft=false;
		string tempS="";
		for(int j=0;j<s.length();j++)
		{
			if(s[j]=='(')
			{
				isLeft=true;
				continue;
			}
			if(s[j]==')')
			{			
				isLeft=false;
				vec.push_back(tempS);
				tempS="";
				continue;
			}		
			if(s[j]!='('&&isLeft==false)
			{
				tempS=s[j];
				vec.push_back(tempS);
				tempS="";
			}else
			{
				tempS+=s[j];
			}
		}
		for(int j=0;j<lib.size();j++)
		{
			int t=lib[i].length();
			for(int k=0;k<lib[j].length();k++)
			{
				
				if(find(vec[k].begin(),vec[k].end(),lib[j][k])>=vec[k].end())
				{
					t=k;
					break;
				}
				
			}
			if(t<lib[i].length())
				;
			else
				count++;
		}
		//for(int k=0;k!=vec.size();k++)
		//	cout<<vec[k]<<endl;
		//getAnswer(vec,lib,0,"",count);//
		//cout<<s<<endl;
#if f
		fs2<<"Case #"<<i<<": "<<count<<endl;
#else
		cout<<"Case #"<<i<<": "<<count<<endl;
#endif
	}
#if f
	fs2.close();
#else
#endif
	return 0;
}

