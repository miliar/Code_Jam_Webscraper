#include <iostream>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <stack>
#include <deque>
#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;
 
int main()
{freopen("A-small-attempt0.in","r",stdin);
        freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int yy=0;yy<t;yy++)
{
	char a[1000],b[101];int c[100];
	gets(a);int i=0;int j=0,ret=0,s[2],g[2][100];s[0]=s[1]=1;
	int n;
	if(a[j+1]<'0' || a[j+1]>'9')
	{n=a[j]-'0';j+=2;}
	else
	if(a[j+2]<'0' || a[j+2]>'9')
	{n=(a[j]-'0')*10+(a[j+1]-'0');j+=3;}
	else
	{n=(a[j]-'0')*100+(a[j+1]-'0')*10+(a[j+2]-'0');j+=3;}
	int p;
	
	for(;a[j-1]!='\0';j++){
		b[i]=a[j];
		j+=2;
		if(a[j+1]<'0' || a[j+1]>'9')
		{c[i]=a[j]-'0';j+=1;}
		else
		if(a[j+2]<'0' || a[j+2]>'9')
		{c[i]=(a[j]-'0')*10+(a[j+1]-'0');j+=2;}
		else
		{c[i]=(a[j]-'0')*100+(a[j+1]-'0')*10+(a[j+2]-'0');j+=3;}
		i++;
	}int o[2];o[0]=0;o[1]=0;
	for(int ii=0;ii<n;ii++)
	{
		if(b[ii]=='O')p=0;else p=1;
		g[p][o[p]++]=c[ii];
	}int x=o[0];o[0]=0;int y=o[1];o[1]=0;//cout<<x;
	for(int ii=0;ii<n;ii++)
	{
	if(b[ii]=='O')
	{
		p=0;
		if(g[p][o[p]]-s[p]>0)
		{//cout<<g[p][o[p]]<<" "<<s[p]<<endl;
			while(g[p][o[p]]!=s[p])
			{
				s[p]++;
				ret++;
				if(g[1][o[1]]-s[1]>0)
				s[1]++;
				if(g[1][o[1]]-s[1]<0)
				s[1]--;
			}//o[p]++;
	
		}
	
		else
		if(g[p][o[p]]-s[p]<0)
		{
			while(g[p][o[p]]!=s[p])
			{
				s[p]--;
				ret++;
				if(g[1][o[1]]-s[1]>0)
				s[1]++;
				if(g[1][o[1]]-s[1]<0)
				s[1]--;
			}//o[p]++;
		
		}
		ret++;if(g[1][o[1]]-s[1]>0)
				s[1]++;
				else
				if(g[1][o[1]]-s[1]<0)
				s[1]--;o[p]++;
	}else
	{
		p=1;
		if(g[p][o[p]]-s[p]>0)
		{
			while(g[p][o[p]]!=s[p])
			{
				s[p]++;
				ret++;
				if(g[0][o[0]]-s[0]>0)
				s[0]++;
				if(g[0][o[0]]-s[0]<0)
				s[0]--;
			}//o[p]++;
	
		}
		
		else
		if(g[p][o[p]]-s[p]<0)
		{
			while(g[p][o[p]]!=s[p])
			{
				s[p]--;
				ret++;
				if(g[0][o[0]]-s[0]>0)
				s[0]++;
				if(g[0][o[0]]-s[0]<0)
				s[0]--;
			}//o[p]++;
		
		}
		ret++;if(g[0][o[0]]-s[0]>0)
				s[0]++;
				else
				if(g[0][o[0]]-s[0]<0)
				s[0]--;o[p]++;
	}
	}
	cout<<"Case #"<<yy+1<<": "<<ret<<endl;
}return 0;
};
