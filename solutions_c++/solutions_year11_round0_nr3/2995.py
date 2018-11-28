#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <fstream>
using namespace std;
typedef long long ll;

int ary[1024];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, n, m, xx, sum;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n;
		m = (1 << 29);
		xx = sum = 0;
		for(int i = 0; i < n; ++i){
			cin>>ary[i];
			xx ^= ary[i];
			m = min(m, ary[i]);
			sum += ary[i];
		}
		cout<<"Case #"<<tt<<": ";
		if(xx != 0){
			cout<<"NO"<<endl;
		}else {
			cout<<sum - m<<endl;
		}
	}
	return 0;
}
			
