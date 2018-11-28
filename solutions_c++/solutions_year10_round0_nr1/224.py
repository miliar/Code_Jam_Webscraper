#include<fstream>
#include<iostream>
using namespace std;
int SnapperChain()
{
	int cas=0;
	int T;
	ifstream F("A-large.in");
	ofstream G("A-large.out");
	F>>T;
	int n,k;
	cout<<"SnapperChain Called\n";
	while(T--)
	{
		cas++;
		F>>n>>k;
		G<<"Case #"<<cas<<": ";
		if ((k+1)%(1<<n)==0)
		{
			G<<"ON"<<endl;
		}else{
			G<<"OFF"<<endl;
		}
	}
	return 0;
return 0;
}