#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int main (int argc, char * const argv[]) {
    int T;
	/*
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int pd,pg,n;
		cin>>n>>pd>>pg;
		bool posible=0;
		int g=pd/__gcd(100,pd);
		if(g<=n)posible=1;
		if(pg==0&&pd!=0)posible=0;
		if(pg==100&&pd!=100)posible=0;
		cout<<"Case #"<<i<<": ";
		if(posible)cout<<"Possible"<<endl;
		else {
			cout<<"Broken"<<endl;
		}

	}
	 */
	
	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int pd,pg,n;
		cin>>n>>pd>>pg;
//		cout<<n<<pd<<pg<<endl;
		bool posible=0;
		for(int d=1;d<=n;d++)for(int w=0;w<=n;w++)
		{
			if((w*100)%d!=0)continue;
			if((w*100)/d!=pd)continue;
			for(int dg=d;dg<=1000;dg++)for(int wg=w;wg<=dg-d+w;wg++)
			{
				if((wg*100)%dg!=0)continue;
				if((wg*100)/dg!=pg)continue;
			//	cout<<w<<" "<<d<<" "<<wg<<" "<<dg<<endl;
					posible=1;
				wg=dg=d=w=1<<20;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(posible)cout<<"Possible"<<endl;
		else {
			cout<<"Broken"<<endl;
		}
	}
    return 0;
}
