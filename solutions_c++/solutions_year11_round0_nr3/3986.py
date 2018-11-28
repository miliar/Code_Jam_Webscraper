#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int k=1;k<=t;k++){
		int n;
		vector <int> c;
		cin >> n;
		for(int i=0;i<n;i++){
			int temp;
			cin >> temp;	c.push_back(temp);
		}
		sort(c.begin(), c.end());

		int m = 0;
		for(int i=0;i<pow(2.0, n);i++){
			if(i==0 || i==pow(2.0, n)-1)	continue;
			int ssum = 0, psum = 0, wsum = 0;
			for(int j=0;j<n;j++){
				if(0x01&(i>>j))	{ ssum += c[j]; wsum = wsum ^ c[j]; }
				else			{ psum = psum ^ c[j]; }
			}
			if(wsum==psum && ssum>m)	m = ssum;
		}
		if(m<=0)	printf("Case #%d: NO\n", k);
		else		printf("Case #%d: %d\n", k, m);
	}
	return 0;
}