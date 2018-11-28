#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int T;
void stuff()
{
	vector<int> v;
	int comb[26][2],opose[26]={-1};
	int have[30]={0};
	int C,last=-1;
	char a,b,c;
	for(int i=0;i<26;i++)
	{
		comb[i][0]=-1;
		opose[i]=-1;
	}
	cin>>C;
	getchar();
	for(int i=0;i<C;i++)
	{
		cin>>a>>b>>c;
		getchar();
		comb[a-'A'][0]=b-'A';
		comb[b-'A'][0]=a-'A';
		comb[b-'A'][1]=c-'A';
		comb[a-'A'][1]=c-'A';
	}
	int D;
	cin>>D;
	getchar();
	for(int i=0;i<D;i++)
	{
		cin>>a>>b;
		getchar();
		opose[a-'A']=b-'A';
		opose[b-'A']=a-'A';
	}
	int N;
	cin>>N;
	getchar();
	for(int i=0;i<N;i++)
	{
		cin>>a;
do_this:
		if(last==-1)
		{
			v.push_back(a-'A');
			have[a-'A']=1;
			last=a-'A';
		}
		else if(comb[a-'A'][0] != -1 && last==comb[a-'A'][0])
		{
			v.pop_back();
			have[comb[a-'A'][0]]--;
			a=comb[a-'A'][1]+'A';
			if(v.empty())
				last=-1;
			else
				last=v.back();
			goto do_this;
		}
		else if(opose[a-'A']!= -1 && have[opose[a-'A']]!=0)
		{
			v.clear();
			for(int k=0;k<30;k++)
				have[k]=0;
			last=-1;
		}
		else
		{
			v.push_back(a-'A');
			have[a-'A']++;
			last=a-'A';			
		}
	}
	if(!v.empty())
	{
		a=v[0]+'A';
		cout<<a;
	}
	for(int i=1;i<v.size();i++)
	{
		a=v[i]+'A';
		cout<<", "<<a;
	}
}
int main(void)
{
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": [";
		stuff();
		cout<<"]"<<endl;
	}
	
}
