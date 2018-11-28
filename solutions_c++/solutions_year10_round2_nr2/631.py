#include<iostream>
#include<map>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	int kk;
	cin>>kk;
int tll=0;
	while(kk--)
	{
tll++;
		int n,k,t,b;
		cin>>n>>k>>b>>t;
		int loc[n],sp[n];
		for(int i=0;i<n;i++)
			cin>>loc[i];
		for(int i=0;i<n;i++)
			cin>>sp[i];
		int cnt=0,tot=0;
		int rchd=0,i;
		for(i=n-1;i>=0;i--)
		{
			if(rchd>=k)
				break;
			if((b-loc[i])<=sp[i]*t)
			{
				rchd++;
				tot+=cnt;
			}
			else
				cnt++;

		}
if(rchd>=k)
		cout<<"Case #"<<tll<<": "<<tot<<endl;
else
		cout<<"Case #"<<tll<<": "<<"IMPOSSIBLE"<<endl;


	}
}
