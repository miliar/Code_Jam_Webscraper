#include <iostream>

using namespace std;

int main()
{
	freopen("2.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int po,pb;
	int i,test,n;
	char r,prer;
	int p,prep,ans,timeo,timeb;
	cin>>test;
	for(i=1;i<=test;i++)
	{
		cin>>n;
		po=pb=1;
		ans=0;
		timeo=timeb=0;
		cin>>r>>p;
		prer=r;prep=p;
		if(r=='O') {timeo=1+abs(p-1);po=p;}
		else{timeb=1+abs(p-1);pb=p;}
		n--;
		while(n>0)
		{
			cin>>r>>p;
			if(r==prer)
			{
				if(r=='O')
				{
					timeo+=1+abs(p-prep);
					po=p;
				}
				else
				{
					timeb+=1+abs(p-prep);
					pb=p;
				}
			}
			else
			{
				if(r=='O')
				{
					timeo+=1+abs(p-po);
					if(timeo<=timeb) timeo=timeb+1;
					po=p;
				}
				else
				{
					timeb+=1+abs(p-pb);
					if(timeb<=timeo) timeb=timeo+1;
					pb=p;
				}
			}
			prer=r;prep=p;
			n--;
		}
		ans=timeo;
		if(timeb>timeo)ans=timeb;
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}