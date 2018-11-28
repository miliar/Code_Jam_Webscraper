#include<iostream>
#include<cstdio>
using namespace std;
#define rep(ini,n) for(int i=ini;i<n;i++)
int tage[101];
int  calc(int n)
{
	int factor=1,prime[5]={2,3,5,7},denom=100;
	for(int i=0;i<4;i++)
	{
		while(n%prime[i]==0 && denom%prime[i]==0)
		{
			factor*=prime[i];
			n/=prime[i];
			denom/=prime[i];
		}
	}
	return factor;
}
int main()
{

	for(int i=1;i<=100;i++)
	{
		tage[i]=calc(i);
	}
	tage[0]=1;
	int t,pg,pd,n,matchd,wond,matchg,wong;
	cin>>t;
	
	for(int test=1;test<=t;test++)
	{
		cout<<"Case #"<<test<<": "; 
		scanf("%d %d %d",&n,&pd,&pg);
		if(pd==0 && pg==0)
		{
			cout<<"Possible"<<endl;
			continue;		
		}
		if(pg==100 && pd==0 ||pg==0 && pd==100)
		{
			cout<<"Broken"<<endl;
			continue;
		}
		
		if(pd==0)
		{
			matchd=1;
			wond=0;
		}		
		else
		{
			matchd=100/tage[pd];
			wond=pd/tage[pd];
		}
		if(matchd>n)
		{
			cout<<"Broken"<<endl;
			continue;
		}
		matchg=100/tage[pg];
		wong=pg/tage[pg];
		if(matchg<matchd)
		{
			
			int scale;
			if(matchd%matchg==0)
			scale=matchg*matchd/matchg;
			else
			scale=matchg*(matchd/matchg+1);
			
			matchg*=scale;
			wong*=scale;
//			cout<<"s"<<wong<<" "<<matchg;
		}
//		cout<<"w"<<wond;
		if(matchd-wond>matchg-wong)
		{
			cout<<"Broken"<<endl;
			continue;
		}

		
		
		if(wond>wong)
		{
			cout<<"Broken"<<endl;
			continue;
		}
		cout<<"Possible"<<endl;
	}
	return 0;
}
