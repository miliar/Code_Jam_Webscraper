#include <iostream>
#include <vector>

using namespace std;

typedef int datum;

bool my_divides(datum a, datum n) {
	if(a == 0L) { return false; }
	return (n%a) == 0L;
}

int main(void)
{
	int T; cin >> T;
	for(int t = 0; t < T; ++t) {
		datum N, L, H; cin >> N >> L >> H;
		vector<datum> data;
		for(datum n = 0; n < N; ++n) {
			datum d; cin >> d;
			data.push_back(d);
		}
		datum good = 0L;
		for(datum tune = L; tune <= H; ++tune) {
			bool ah = true;
			for(int i = 0; i < N; ++i) {
				bool harmony = my_divides(tune, data[i]) || my_divides(data[i], tune);
				if(!harmony) { ah=false; break; }
			}
			if(ah) {
				good = tune;
				break;
			}
		}
		cout << "Case #" << (t+1) << ": ";
		if(good == 0) {
			cout << "NO" << endl;
		}
		else {
			cout << good << endl; 
		}
	}
	return 0;
}
