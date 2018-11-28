#include <iostream>
#include <cmath>
using namespace std;
int t,n,k;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_large_out.out","w",stdout);
	int i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		cin >> n >> k;
		cout << "Case #"<< i << ": ";
		int x=pow(2.0,n);
		if ((k+1)%x==0)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}
}