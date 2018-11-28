#include<iostream>
#include<algorithm>
using namespace std;
int n,m;
bool check(int n,int m)
{
	for (int i=0;i<n;i++)
	{
		if (!(m&1))
			return false;
		m>>=1;
	}
	return true;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin >>t;
	for (int i=1;i<=t;i++)
	{
		cin >>n>>m;
		cout <<"Case #"<<i<<": ";
		if (check(n,m))
			cout <<"ON"<<endl;
		else
			cout <<"OFF"<<endl;
	}
	return 0;
}
