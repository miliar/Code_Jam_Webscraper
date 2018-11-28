#include <iostream>
#include <vector>
#include <vector>
#include <algorithm>
using namespace std;

typedef long FREQ;
FREQ ans;



int main() {
	int t;
	cin >> t;
	vector<FREQ> frq;
	int N,L,H;

	for (int tn=0;tn<t;tn++) {
		cin >> N >> L >> H;
		frq.clear();
		for (int i=0;i<N;i++) {
			FREQ t;
			cin >> t;
			frq.push_back(t);
		}

		ans = -1;
		//std::sort(frq.begin(),frq.end());
		for (FREQ t = L;t<=H;t++) {
			bool f = true;
			for (int i=0;i<N;i++) {
				if (t%frq[i] != 0 && frq[i]%t != 0) {
					//cout << t << " ! " << frq[i] << endl;
					f=false;
					break;
				}
			}
			if (f) {
				ans = t;
				break;
			}
		}

		cout << "Case #" << (tn+1) << ": " ;
		if (ans>0) {
			cout << ans << endl;
		} else {
			cout << "NO" << endl;
		}
		

	}

	return 0;
}
