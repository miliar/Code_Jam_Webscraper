#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int n,m,tt,ii;

int main()
{
	freopen("al.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>n>>m;
		m%=(1<<n);
		if (m==(1<<n)-1)
			cout<<"Case #"<<ii<<": ON"<<endl;
		else
			cout<<"Case #"<<ii<<": OFF"<<endl;
	}
	return 0;
}
	
