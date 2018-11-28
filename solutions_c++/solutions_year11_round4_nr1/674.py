#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

class Seq {
	public:
		long double B, E, w;
		Seq(long double bb, long double ee, long double ww) {
			B = bb;
			E = ee;
			w = ww;
		}
};

bool compare(const Seq& a, const Seq& b) {
	return (a.w < b.w);
}

vector<Seq> seq;
long double X, S, R, t, N;

void solve() {
	cin >> X >> S >> R >> t >> N;
	seq.clear();
	seq.assign(N, Seq(0, 0, 0));
	long double totalS = 0;
	for (int i = 0; i < N; ++i) {
		cin >> seq[i].B >> seq[i].E >> seq[i].w;
		totalS += (seq[i].E - seq[i].B);		
	}
	/*
	cout << "tund1" << endl;
	*/
	sort(seq.begin(), seq.end(), compare);

	long double result = 0.0;
	if ((X - totalS) / R <= t) {
		result += (X - totalS) / R;
		t -= (X - totalS) / R;
		X = totalS;
	} else {
		X -= R * t;
		result += t;
		t = 0.0;
	}
	totalS = 0.0;
	for (int i = 0; i < N; ++i) {
		if ((seq[i].E - seq[i].B) / (seq[i].w + R) <= t) {
			result += (seq[i].E - seq[i].B) / (seq[i].w + R);
			t -= (seq[i].E - seq[i].B) / (seq[i].w + R);
		}
		else {
			result += t;
			result += (seq[i].E - seq[i].B - (seq[i].w + R)*t) / (seq[i].w + S);			
			t = 0.0;
		}
		totalS += (seq[i].E - seq[i].B);
	}
	if ((X - totalS) / R <= t) result += (X - totalS) / R;
	else {
		result += t + (X - totalS - R*t) / S;
	}
	cout << setprecision(8) << fixed << result << endl;
}

int main() {
	int nTest;
	cin >> nTest;
	for (int i = 1; i <= nTest; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

