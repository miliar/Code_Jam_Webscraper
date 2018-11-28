#include<iostream>
#include<cmath>
#include<cstdio>
#include<string.h>
using namespace std;


int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);


	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++)
	{
		int c;
		long long l,p;
		cin>>l>>p>>c;
		int ca=0;
		long long ll=l;
		while(ll<p)
		{
			ll*=c;
			ca++;
		}
		int ans=0;
		if(ca==0)
			ans=0;
		else
		{
			int h=0;
			long long tt=1;
			if(ca==1)
				h=0;
			else
			{
			for(h=1;((h<=10000)&&(tt<ca));h++)
			{
				tt*=2;
				if(tt>=ca)
					break;
			}
			}
			ans=h;
		}



		cout<<"Case #"<<i<<": "<<ans<<endl;
	}

return 0;
}
