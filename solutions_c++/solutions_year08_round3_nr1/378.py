#include <iostream>
#include <vector>

using namespace std;

int main() {
	string noinp;
	cin >> noinp;

	// Az inputok szamaszor megcsinalja amit kell...
	for (int i=0; i < atoi(noinp.c_str()); ++i) {

		//Adatok beolvasasa:
		string str;
		int p, k, l;
		cin >> str;
		p = atoi(str.c_str());
		cin >> str;
		k = atoi(str.c_str());
		cin >> str;
		l = atoi(str.c_str());

		vector<int> freq_of_l;
		for (int j = 0; j < l; ++j) {
			cin >> str;
			freq_of_l.push_back(atoi(str.c_str()));
		}

		//Osszeg kiszámítása:
		sort(freq_of_l.begin(), freq_of_l.end(), greater<int>());
		long long sum = 0;
		int szorzo = 0;
		for (int j = 0; j < freq_of_l.size(); ++j) {
			if ((j%k) == 0)
				++szorzo;
			sum += szorzo * freq_of_l[j];
		}

		//Eredmeny kiiratasa:
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
}

