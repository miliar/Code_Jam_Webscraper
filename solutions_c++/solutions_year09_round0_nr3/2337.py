
#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;
char tag[20]="welcome to code jam";
char in[510];
int ans,len;
void dfs(int deep,char *temp);
int main()
{
	ifstream fin("C-small-attempt2.in");
	ofstream fout("C-small-attempt2.out");
	int i,cas,k;
	int cur;
	//cin>>cas;
	fin>>cas;
	fin.getline(in,505);
	//cin.getline(in,sizeof(in));
	for(i=1;i<=cas;i++)
	{
		fin.getline(in,sizeof(in));
		ans=0;
		dfs(0,in);
		cur=ans%10000;
		fout<<"Case #"<<i<<": ";
		if(cur==0) 
		{
			//cout<<"0000"<<endl;
			fout<<"0000"<<endl;
			continue;
		}
		k=(int)log10(double(cur))+1;
		for(;k<4;k++) fout<<'0';
		fout<<cur<<endl;
	}
	return 0;
}
void dfs(int deep,char *temp)
{
	char *p;
	p=strchr(temp,tag[deep]);
	if(p==NULL) return;
	if(deep==18)
	{
		ans+=1;
		p=strchr(p+1,tag[deep]);
		while(p!=NULL) 
		{
			ans++;
			p=strchr(p+1,tag[deep]);
		}
		return;
	}
	else
	{
		while(p!=NULL)
		{
			dfs(deep+1,p+1);
			p=strchr(p+1,tag[deep]);
		}
	}
}