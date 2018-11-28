#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	long long er[50],n,m,i,test,numtest;
	
	ifstream cin ("a.in");
	ofstream cout ("a.out");
	cin >> numtest;
	er[1]=2;
	for(i=2;i<=30;i++) er[i]=er[i-1]+er[i-1];
	for(test=1;test<=numtest;test++)
	{
		cin >> n >> m;
		if((m+1)%er[n]==0) cout << "Case #"<<test<<": ON"<< endl;
		else cout << "Case #"<<test<<": OFF"<< endl;
	}
	
	return 0;
}
