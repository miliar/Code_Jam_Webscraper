#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i=0;i<t;i++) {
		int n;
		int bpos = 1, opos = 1;
		int btime = 0, otime = 0;
		deque<int> bb,oo;
		cin >> n;

		for (int j=0;j<n;j++) {
			char c;
			int p;
			cin >> c >> p;
			if (c=='B') {
				btime+= abs(bpos-p) + 1;
				bpos = p;
				if (btime <= otime) btime = otime+1;
				//cout << "b" << btime << endl;
			} else {
				otime+= abs(opos-p) + 1;
				opos = p;
				if (otime <= btime) otime = btime+1;
				//cout << "o" << otime << endl;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << max(btime,otime) << endl;

	
	}

	return 0;
}
