#include<iostream>
using namespace std;
int N,Pd,Pg;
int pro()
{
	int i;
	if(Pg==0)
	{
		if(Pd==0)
			return 1;
		else
			return 0;
	}
	else if(Pg==100)
	{
		if(Pd==100)
			return 1;
		else
			return 0;
	}
	else if(N>=100)
	{
		return 1;
	}
	else
	{
		for(i=1;i<=N;++i)
		{
			if((i*Pd/100)*100==i*Pd)
			{
				return 1;
			}
		}
		return 0;
	}
}
int main()
{
	int T,t;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	cin>>T;
	for(t=1;t<=T;++t)
	{
		cin>>N>>Pd>>Pg;
		if(pro())
			cout<<"Case #"<<t<<": Possible"<<endl;
		else
			cout<<"Case #"<<t<<": Broken"<<endl;
	}
	return 0;
}