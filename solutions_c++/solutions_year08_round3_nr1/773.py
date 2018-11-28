#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct Freq
{
	int fr;
	int val;
	Freq (int fr) : fr(fr) {
	}
};


bool sortF (const Freq& f1, const Freq& f2)
{
	return f1.fr > f2.fr;
}

int
processTc()
{
	int p, k, l;
	cin >> p >> k >> l;

	int fr;
	vector<Freq> frequencies;
	for (size_t i = 0; i < l; ++i) {
		cin >> fr;
		frequencies.push_back(Freq(fr));
	}

	sort(frequencies.begin(), frequencies.end(), sortF);

	int value = 1;
	int j = 0;
	for (int i = 0; i < l ; ++i) {
		if (j < k) {
			++j;
		} else {
			value++;
			j = 1;
		}
		frequencies[i].val = value;
	}
	int sol = 0;
	for (int i = 0; i < l; ++i) {
		sol += frequencies[i].fr * frequencies[i].val;
	}
	return sol;
}

int main()
{
	int numTcs;
	cin >> numTcs;
	for (size_t i = 0; i < numTcs; ++i){
		int sol = processTc();
		cout << "Case #" << i+1 << ": " << sol << endl;
	}
}
