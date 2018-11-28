#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
using namespace std;
long long n;
int main()
{
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		int ind=0;
		int pm[1231]={0};
		for(int i=2;i<=n;i++)
		{
			if(!pm[i])
			{
				for(int q=i*i;q<1001;q+=i)
				{
					pm[q]=1;
				}
				pm[ind++]=i;
			}
		}
		//for(int i=0;i<ind;i++)
		//	cout<<pm[i]<<"   ";cout<<endl;
		int mn=ind,mx=1;
		int bj[12311]={0};
		for(int i=2;i<=n;i++)
		{
			bool fk=0;
			int ii=i;
			for(int q=0;q<ind;q++)
			{
				int z=0;
				while(ii%pm[q]==0)
				{
					z++;
					ii/=pm[q];
				}
				if(bj[q]<z)
				{
					bj[q]=z;
					fk=1;
				}
			}
			mx+=fk;
		}
		//cout<<mx<<endl;
		if(n==1)mn=1;
		printf("Case #%d: %d\n",cas++,mx-mn);
	}
}