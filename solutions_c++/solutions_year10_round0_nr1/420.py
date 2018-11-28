#include <iostream>
#include <cstdio>
using namespace std;

int main () {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int n;
	cin >> n;
	for (int i=0;i<n;i++) {
		int x,y;
		cin >> x >> y;
		cout << "Case #" << i+1 << ": ";
		if ((y+1)%(1<<x)==0) cout << "ON"; else cout << "OFF";
		cout << endl;
	}
}
