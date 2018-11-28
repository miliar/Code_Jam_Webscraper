#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef double datum;

int main(void) {
	int Kase; cin >> Kase;
	for(int kase = 0; kase < Kase; ++kase) {
		datum X, S, R, T; int N;
		cin >> X >> S >> R >> T >> N;
		
		vector<pair<datum, datum> > data;
		datum sigma = 0;
		for(int n = 0; n < N; ++n) {
			datum B, E, W;
			cin >> B >> E >> W;

			datum delta = E-B;
			sigma += delta;
			data.push_back(make_pair(W, delta));
		}
		data.push_back(make_pair(0., X - sigma));

		sort(data.begin(), data.end());

		double boost_left = T;
		double time_total = 0.;
		size_t size = data.size();
		for(size_t i = 0; i < size; ++i) {
			pair<datum, datum>& d = data[i];
			datum speed_bonus = d.first;
			datum length_part = d.second;

			if(boost_left*(R+speed_bonus) >= length_part) {
				double time_part = (double)length_part / (R+speed_bonus);
				boost_left -= time_part;
				time_total += time_part;
				length_part = 0;
				continue;
			}
			if(boost_left*(R+speed_bonus) <= length_part) {
				double time_part = boost_left;
				boost_left = 0.;
				time_total += time_part;
				length_part -= time_part*(R+speed_bonus);
			}
			double time_part = (double)length_part / (S+speed_bonus);
			time_total += time_part;
		}
		cout << "Case #" << (kase+1) << ": " << setprecision(9) << fixed << time_total << endl;
	}
	return 0;
}
