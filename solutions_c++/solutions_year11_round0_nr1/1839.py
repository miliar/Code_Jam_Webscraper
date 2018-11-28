#include <cstdio>
#include <iostream>
using namespace std;
/*
class act{
	bool robot;
	int button;
	act(char r, int b) {
		this->robot = (r=='O');
		this->button = b;
	}
};
*/
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t,n; cin>>t;
	int to, tb, po, pb;
	char r; int b;
	for (int k=1; k<=t; k++) {
		cin>>n;
		to = tb = 0;
		po = pb = 1;
		for (int i=0; i<n; i++) {
			cin>>r>>b;
			if (r=='O') {
				to = max(to+abs(b-po)+1, tb+1);
				po = b;
			}
			else {
				tb = max(to+1, tb+abs(b-pb)+1);
				pb = b;
			}
		}
	
		cout<<"Case #"<<k<<": "<<max(to,tb)<<endl;
	}
}
