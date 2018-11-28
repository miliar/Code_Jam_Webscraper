#include <iostream>
using namespace std;

int main()
{
	freopen("result.txt","w",stdout);
	int cs;
	cin>>cs;
	int n,k;
	for(int i=1;i<=cs;i++)
	{
		cin>>n>>k;
		if((k+1)%(1<<n)==0)
			cout<<"Case #"<<i<<": ON\n";
		else cout<<"Case #"<<i<<": OFF\n";
	}
}