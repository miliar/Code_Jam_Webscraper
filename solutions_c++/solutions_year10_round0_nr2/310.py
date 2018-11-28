#include <fstream>
#include <iostream>
#include <stack>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#define LL long long
using namespace std;
LL gcd (LL a, LL b) {
	return b ? gcd (b, a % b) : a;
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	LL T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		int n;
		cin>>n;
		vector<LL> a(n),b(n);
		for(int i=0;i<n;i++)cin>>a[i];
		sort(a.begin(),a.end());
		int gc=a[1]-a[0];
		//if(n==2) gc=gcd(a[0],a[1]);
		for(int i=2;i<n;i++)
		{
			gc=gcd(gc,a[i]-a[i-1]);
		}
		int mx=0;
		for(int i=0;i<n;i++)
		{
			b[i]=(gc-a[i]%gc);
		}
		cout<<"Case #"<<ti<<": "<<b[0]%gc<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}