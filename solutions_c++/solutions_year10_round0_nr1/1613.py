#include <iostream>
using namespace std;

int main() {
	//freopen("small.in","r",stdin);
	//freopen("small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int tn,cn;
	cin>>tn;
	cn=tn;
	while (cn--)
	{
		int n,k;
		cin>>n>>k;
		cout<<"Case #"<<tn-cn<<": ";
		if ((k + 1) % (1 << n)==0)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
			
	}
	return 0;
}
