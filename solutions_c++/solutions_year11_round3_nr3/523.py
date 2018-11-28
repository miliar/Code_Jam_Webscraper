#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

int T,N,L,H;

int other[128];
bool ok(int x)
{
	int i;
	for(i=0;i<N;++i)
	{
		if(x%other[i] && other[i]%x ) return false;
	}
	return true;
}
int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int t;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		
		cout<<"Case #"<<t<<": ";
		cin>>N>>L>>H;
		int i;
		for(i=0;i<N;++i)
			cin>>other[i];
		for(i=L;i<=H;++i)
		{
			if(ok(i))
			{
				break;
			}
		}
		if(i<=H) cout<<i<<endl;
		else cout<<"NO"<<endl;

	}

	return 0;
}
