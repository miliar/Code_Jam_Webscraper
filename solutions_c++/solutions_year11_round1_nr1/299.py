#include <iostream>
using namespace std;
void doo()
{
	long long  a, b, c;
	cin >> a >> b >> c;
	if(c==0&&b!=0){
		cout<<"Broken"<<endl;
		return ;
	}
	if(c==100&&b!=100){
		cout<<"Broken"<<endl;
		return ;
	}
	if(c==0&&b==0){
		cout<<"Possible"<<endl;
		return ;
	}
	//cerr<<b<<endl;
	for(long long  i=1; i<=a; i++){
		if(i*b%100==0){
			cout<<"Possible"<<endl;
			return ;
		}
	}
	cout<<"Broken"<<endl;
}
int  main()
{
	long long  ncase=0;
	cin>>ncase;
	for(long long  i=0; i<ncase; i++)
	{
		cout<<"Case #"<<i+1<<": ";
		doo();
	}
}
