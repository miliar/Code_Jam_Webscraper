#include<stdio.h>
#include<string.h>
#include <algorithm>
#include<iostream>
using namespace std;
bool cmp(int,int);
bool IsSur(int);
int Best(int,int,int);
int main()
{
	int t,n,s,p,i,sum,num,j,k,a[101];
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int f[101]={0};
		cin>>n>>s>>p;
		sum=0;num=0;
		for(j=0;j<n;j++)
			cin>>a[j];
		if(!s&&!p)
		{
			cout<<"Case #"<<i<<": "<<n<<endl;
			continue;
		}
		sort(a,a+n,cmp);
		for(j=0;j<n;j++)
			if(IsSur(a[j])) 
			{	f[j]=1;
			num=num+1;
			}
		for(j=0;j<n;j++)
		{
			if(f[j]==1)
			{
				if(num>s)
				{
					if(Best(a[j],p,0)&&Best(a[j],p,1))
						{sum=sum+Best(a[j],p,0);num=num-1;}
					else if(s!=0){sum=sum+Best(a[j],p,1);s=s-1;}
					else {sum=sum+Best(a[j],p,0);num=num-1;}
				}
				else sum=sum+Best(a[j],p,1);
			}
			else sum=sum+Best(a[j],p,0);
		}
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}
bool cmp(int a,int b)
{
	return a>b;
}
bool IsSur(int x)
{
	if(x%3==1||x==0) return false;
	else return true;
}
int Best(int x,int p,int flag)
{
	if(IsSur(x)) 
	{
		if(flag==1)
		{
			if(x%3==0)
				if(x/3+1>=p) return 1;
				else return 0;
				else 
					if(x/3+2>=p) return 1;
					else return 0;
		}
		else 
		{
			if(x%3==0)
				if(x/3>=p) return 1;
				else return 0;
				else 
					if(x/3+1>=p) return 1;
					else return 0;
		}
	}
	else if(x==0) return 0;
	else 
		if(x/3+1>=p) return 1;
		else return 0;
}