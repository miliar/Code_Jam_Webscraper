#include<iostream> 
using namespace std;
bool cal(int N, int Pd, int Pg)
{
	int d,g;
	for (d=1;d<=N;d++)
		if (d*Pd%100==0)
		{
			for (g=d;g<100000;g++)
				if (g*Pg%100==0 && g*Pg>=d*Pd)
				{
					//if (d==5 && g==25) cout<<g*Pg-d*Pd<<endl;
					if (g*Pg-d*Pd<=(g-d)*100)
					//cout<<g<<" "<<d<<endl;
						return true;	
				}
		}
	return false;
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int cs,c,N,Pd,Pg;
	cin>>cs;
	for (c=1;c<=cs;c++)
	{
		cin>>N>>Pd>>Pg;
		if (cal(N,Pd,Pg)) cout<<"Case #"<<c<<": Possible"<<endl;
		else cout<<"Case #"<<c<<": Broken"<<endl;
	}
	return 0;
}
