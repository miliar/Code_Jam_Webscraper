
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t, n, k;
	cin >> t;
	for (int i=1; i<t+1; i++)
	{
		cin>>n>>k;
		n=(1<<n)-1;
		cout<<"Case #"<<i<<": ";
		if((k&n)==n) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	return 0;
}
