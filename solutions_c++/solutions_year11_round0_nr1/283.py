#include <iostream>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		int N;
		cin >> N;
		int op=1, ot=0, bp=1, bt=0;
		fu(i,0,N) {
			int p; char c;
			cin >> c >> p;
			//cout << p << c << endl;
			//cout << ot << op << bt << bp << endl;

			if(c=='O') {
				ot += abs(op-p);
				op = p;
				ot = max(ot, bt);
				ot++;
			}
			
			if(c=='B') {
				bt += abs(bp-p);
				bp = p;
				bt = max(bt, ot);
				bt++;
			}
		}
		cout << "Case #" << tc << ": " << max(ot,bt) << endl;
	}
}
