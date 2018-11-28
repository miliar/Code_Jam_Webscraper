#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	unsigned int t, n, k;
	int round=1;
	cin >> t;
	while (round<=t)
	{
		cin>>n>>k;
		if( (k%(1<<n) & ((1<<n)-1)) == (1<<n)-1 )
			cout<<"Case #"<<round<<": ON"<<endl;
		else
			cout<<"Case #"<<round<<": OFF"<<endl;
		round++;
	}
	return 0;
}
