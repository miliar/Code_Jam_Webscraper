#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;


int mini(int a,int b)
{
	if(a<b)return a;
	return b;
}

void doit(int test)
{
	int V,M,i,k;
	int tobe0[20000]={0};
	int tobe1[20000]={0};
	int c[20000]={0};
	int val[20000]={0};
	cin>>M>>V;
	for(i=0;i<M;i++)
	{
		cin>>k;
		val[i+1]=k;
		tobe0[i+1]=1000000;
		tobe1[i+1]=1000000;
		if(i>=M/2)
		{
			if(k==0)
			{
				tobe0[i+1]=0;
				tobe1[i+1]=1000000;
			}
			else
			{
				tobe0[i+1]=1000000;
				tobe1[i+1]=0;
			}
		}
		else
		{
			cin>>k;
			c[i+1]=k;
		}
	}
	for(i=M/2;i>=1;i--)
	{
		if(c[i]==1)
		{
			if(val[i]==0)
			{
				tobe0[i]=mini(tobe0[i*2]+tobe0[i*2+1],1+mini(tobe0[i*2]+tobe1[i*2+1],tobe1[i*2]+tobe0[i*2+1]));
				tobe1[i]=mini(tobe1[i*2]+tobe1[i*2+1],mini(tobe0[i*2]+tobe1[i*2+1],tobe1[i*2]+tobe0[i*2+1]));
			}
			else
			{
				tobe0[i]=mini(tobe0[i*2]+tobe0[i*2+1],mini(tobe0[i*2]+tobe1[i*2+1],tobe1[i*2]+tobe0[i*2+1]));
				tobe1[i]=mini(tobe1[i*2]+tobe1[i*2+1],1+mini(tobe0[i*2]+tobe1[i*2+1],tobe1[i*2]+tobe0[i*2+1]));
			}
		}
		else
		{
			if(val[i]==0)
			{
				tobe0[i]=tobe0[i*2]+tobe0[i*2+1];
				tobe1[i]=mini(tobe1[i*2]+tobe1[i*2+1],mini(tobe0[i*2]+tobe1[i*2+1],tobe1[i*2]+tobe0[i*2+1]));
			}
			else
			{
				tobe0[i]=mini(tobe0[i*2]+tobe0[i*2+1],mini(tobe0[i*2]+tobe1[i*2+1],tobe1[i*2]+tobe0[i*2+1]));
				tobe1[i]=tobe1[i*2]+tobe1[i*2+1];
			}
		}
	}
	cout<<"Case #"<<test<<": ";
	if(V==0)
	{
		if(tobe0[1]>100000)cout<<"IMPOSSIBLE";
		else cout<<tobe0[1];
	}
	else 
	{
		if(tobe1[1]>100000)cout<<"IMPOSSIBLE";
		else cout<<tobe1[1];
	}
	cout<<endl;
}

int main()
{
	int T,t;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		doit(t);
	}
	return 0;
}