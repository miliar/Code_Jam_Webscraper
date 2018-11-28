#include<iostream>
#include <FSTREAM>
using namespace std;

int main()
{
	int T;//
	int s;//惊讶数
	int p;//高分
	int n;//人数
	int now;
	int i,j,pn,sn,ans;
	ifstream cin("B-large.in",ios::in);
	ofstream cout("2.txt",ios::out);
	cin>>T;
	for(i=0;i<T;i++)
	{
		
		cin>>n>>s>>p;	
		pn=p*3-2;
		sn=p*3-4;
		if(pn<0)
			pn=0;
		if(sn<0)
			sn=p;
		ans=0;
		for(j=0;j<n;j++)
		{
			cin>>now;
			if (now>=pn)
			{
				ans++;
				continue;
			}
			else if (now>=sn&&s>0)
			{
				ans++;
				s--;
				continue;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

}
