#include<iostream>
using namespace std;
int p2(int x)
{
	if(x==0)return 1;
	return 2*p2(x-1);
}
int main()
{
	int tc;
	cin>>tc;
	int C=1;
	while(tc--){
		int a,b;
		cin>>a>>b;
		int ga=p2(a);
		if(ga-1!=b%ga)cout<<"Case #"<<C++<<": OFF"<<endl;
		else cout<<"Case #"<<C++<<": ON"<<endl;
	}
}