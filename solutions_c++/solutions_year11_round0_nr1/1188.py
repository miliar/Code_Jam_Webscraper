#include <iostream>
#include <cstdio>
using namespace std;

int pa,pb,t,n,c,d,pc,ta,tb;
char ch;
int xabs( int u) {
	return u>=0?u:-u;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	cin>>c;
	for (int pc=1;pc<=c;++pc) {
		cin>>n;

		pa = 1;
		pb = 1;
		ta = 0;
		tb = 0;
		t = 0;
		for (int i=0;i<n;++i) {
			cin>>ch>>d;
			if (ch == 'O') {
				t = max(t+1, ta + xabs(d-pa)+1);
				pa = d;
				ta = t;
			} else {
				t = max(t+1, tb + xabs(d-pb)+1);
				pb = d;
				tb = t;
			}
		}
		cout<<"Case #"<<pc<<": ";
		cout<<t<<endl;
	}
	return 0;
}
