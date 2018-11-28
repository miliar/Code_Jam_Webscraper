#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
typedef long long ll;

int a1[20];

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T;
	int r, k, n, p, s;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>r>>k>>n;
		for(int i = 0; i < n; ++i)
			cin>>a1[i];
		p = s = 0;
		while(r--){
			int p1 = p;
			int s1 = a1[p1];
			p1 = (p1+1)%n;
			while(s1 + a1[p1] <= k && p1 != p){
				s1 += a1[p1];
				p1 = (p1+1)%n;
			}
			if(s1 <= k)s += s1;
			p = p1;
		}
		cout<<"Case #"<<tt<<": "<<s<<endl;
	}
	return 0;	
}
