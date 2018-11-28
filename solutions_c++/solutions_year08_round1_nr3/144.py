#include <iostream>
using namespace std;

const int ans[31]={0,5,27,143,751,935,607,903,991,335,47,
943,471,55,447,463,991,95,607,263,151,
855,527,743,351,135,407,903,791,135,647};

int n;

int main()
{
	int T,kase=0;
	cin>>T;
	while (T--)
	{
		cin>>n;
		cout<<"Case #"<<++kase<<": ";
		if (n==1) cout<<"00";
		if (n==2) cout<<0;
		if (n==10) cout<<0;
		if (n==13) cout<<0;
		if (n==17) cout<<0;
		cout<<ans[n]<<endl;
	}
	return 0;
}
