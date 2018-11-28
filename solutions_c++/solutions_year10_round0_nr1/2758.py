#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int t,n,k;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		cin>>n>>k;
		bool state=false;
		bool cnt=false;
		int tmp=pow((double)2,n-1);
		state=(k/tmp)%2;
		if((k+1)%tmp==0)
			cnt=true;
		else
			cnt=false;
		if(cnt&&state)
			cout<<"Case #"<<tt<<": ON"<<endl;
		else
			cout<<"Case #"<<tt<<": OFF"<<endl;
	}
	system("pause");
	return 0;
}