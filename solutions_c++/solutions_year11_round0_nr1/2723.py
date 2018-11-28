#include <iostream>
using namespace std;

char r[110];
int p[110];

int main()
{
	freopen("pa.in", "r", stdin);
	freopen("pa.out", "w", stdout);
	
	int T,t;
	int n;
	int op,ot,bp,bt,time,ans,temp,i;

	cin>>T;
	for(t=1; t<=T; t++)
	{
		cin>>n;
		for(i=0; i<n; i++)
		{
			cin>>r[i]>>p[i];
		}

		op=bp=1;
		ot=bt=0;
		time=0;
		for(i=0; i<n; i++)
		{
			if(r[i]=='O')
			{
				temp=abs(p[i]-op)-(time-ot);
				if(temp<0)
					temp=0;
				op=p[i];
				time=ot=time+temp+1;
			}
			if(r[i]=='B')
			{
				temp=abs(p[i]-bp)-(time-bt);
				if(temp<0)
					temp=0;
				bp=p[i];
				time=bt=time+temp+1;
			}
		}
		cout<<"Case #"<<t<<": "<<time<<endl;
	}
	return 0;
}
