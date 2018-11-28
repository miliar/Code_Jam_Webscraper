#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<bool> lon;

int main()
{
	ifstream cin("a2.in");
	ofstream cout("a2.out");

	int t;
	cin>>t;
//	cout<<t<<endl;
	for (int i=0;i<t;++i) {
		int n,k;
		cin>>n>>k;
		bool power(true);
		for (int p=0;p<n;++p) {
			long long j(1<<p);
			if (!(j&k)) {
				power=false;
				break;
			}
		}
		
		if (power) 
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	return 0;
}
