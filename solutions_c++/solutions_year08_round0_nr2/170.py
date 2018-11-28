#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

int main(){
	int n,tt,na,nb,i,j,h,m;
	char dummy;
	cin >> n;
	for (i=0;i<n;i++) {
		int a=0, b=0;
		cin >> tt;
		cin >> na >> nb;
		deque<int> a_start,a_ready,b_start,b_ready;
		for (j=0;j<na;j++) {
			cin >> h >> dummy >> m ;
			a_start.push_back(m+h*60);
			cin >> h >> dummy >> m ;
			b_ready.push_back(m+h*60+tt);
		}
		for (j=0;j<nb;j++) {
			cin >> h >> dummy >> m ;
			b_start.push_back(m+h*60);
			cin >> h >> dummy >> m ;
			a_ready.push_back(m+h*60+tt);
		}
		sort(a_start.begin(),a_start.end());
		sort(b_start.begin(),b_start.end());
		sort(a_ready.begin(),a_ready.end());
		sort(b_ready.begin(),b_ready.end());
		for (j=0;j<na;j++) {
			int t = a_start[j];
			if (!a_ready.empty() && a_ready.front()<=t) {
				a_ready.pop_front();
			} else {
				a++;
			}
		}
		for (j=0;j<nb;j++) {
			int t = b_start[j];
			if (!b_ready.empty() && b_ready.front()<=t) {
				b_ready.pop_front();
			} else {
				b++;
			}
		}
		cout << "Case #" <<  (i+1) << ": " << a << " " << b << endl;
	}
}

