#include <iostream>
#include <cmath>
using namespace std;

int t,n,k;

int slove(int n,int k)
{
	int mark=(1<<n)-1;
	if((k&mark)==mark)
		return 1;
	else
		return 0;
}

int main()
{
#ifdef _DEBUG
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
#endif
	int j=1;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		cout<<"Case #"<<j<<": ";
		if(slove(n,k)==1)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
		j++;
	}
	return 0;
}