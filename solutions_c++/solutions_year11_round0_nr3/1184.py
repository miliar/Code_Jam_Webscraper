#include <iostream>
#include <cstdio>
#include <memory.h>
#include <vector>
using namespace std;

int n,s,m,sum,c,d;
int xmin(int u,int v) {
	return u<v?u:v;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> c;
	for (int ccc = 1; ccc <= c; ++ccc) {

		cin>>n;
		s = 0;
		m = 10000000;
		sum = 0;
		for (int i = 0;i<n;++i) {
			cin>>d;
			s = s ^ d;
			m = xmin(d,m);
			sum+=d;
		}

		cout << "Case #" << ccc << ": ";
		if (s==0) {
			cout<<sum-m<<endl;
		} else {
			cout<<"NO"<<endl;
		}

	}
	return 0;
}
