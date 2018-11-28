#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>

using namespace std;

int a[1000001];

int main () {
	fstream cin("C-large.in");
	ofstream cout("output.txt");
	int T;
	cin>>T;
	for (int run=1;run<=T;++run) {
		int n;
		cin>>n;	
		int sum = 0;
		for (int i=0;i<n;++i) {
			cin>>a[i];
			sum+=a[i];
		}
		sort (a,a+n);
		sum =sum - a[0];
		bool found = true;
		for (int j=0;j<=20;++j) {
			int count = 0;
			for (int i=0;i<n;++i) {
				int x = (a[i]>>j) & 1;
				count+=x;
			}
			if (count%2==1) {
				found = false;
				break;	
			}
		}
		if (!found) cout<<"Case #"<<run<<": NO"<<endl;
		else cout<<"Case #"<<run<<": "<<sum<<endl;
	}
	cin>>T;
	return 0;	
}
