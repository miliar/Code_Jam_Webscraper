//In the name of Allah
//
//
#include <iostream>
using namespace std;
int n,t,l,h;
int list[1000];
bool ts(int a)
{
	for (int i=0;i<n;i++) if (a%list[i]!=0 && list[i]%a!=0)
		return 0;
	return 1;
}
int main()
{
	cin>>t;
	for (int c=1;c<=t;c++)
	{
		cin>>n>>l>>h;
		for (int i=0;i<n;i++)
			cin>>list[i];
		cout<<"Case #"<<c<<": ";
		bool av=true;
		for (int i=l;i<=h;i++) if (ts(i))
		{
			cout<<i<<endl;
			av=false;
			break;
		}
		if (av)
			cout<<"NO"<<endl;

	}
}
