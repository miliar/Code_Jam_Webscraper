#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <strstream>
#include <map>
#include <math.h>
#include <deque>
using namespace std;

int k, i;

int mas[10];

struct Vec {
	int mas[10];
	Vec(const int m[10]) { for (int i = 0; i< 10; ++i) mas[i] = m[i]; }
	Vec& operator = (const Vec& vec) { for (int i = 0; i < 10; ++i) mas[i] = vec.mas[i]; return *this; }
	bool operator <(const Vec& vec) const { 
		for (int i = 0; i < 10; ++i) 
			if (mas[i] < vec.mas[i]) 
				return true;
			else
				if (mas[i] > vec.mas[i])
					return false;
		return false; 
	}
	Vec() {}
};

int n;
bool check(const Vec& vec) {
	for (int i = 0; i < n; ++i)
		if (vec.mas[i] > i + 1)
			return false;
	return true;
}

map<Vec, int> mapa;
deque<Vec> decc;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> k;
	for (int i  = 0 ;i < k ;++i) {

		cin >> n;
		
		for (int m = 0; m < n; ++m) {
			string str;
			cin >> str;
			
			mas[m] = 0;
			for (int j = str.size() - 1; j >= 0; --j)
				if (str[j] == '1') {
					mas[m] = j + 1;
					break;
				}
		}
		
		mapa.clear();
		decc.clear();
		mapa[Vec(mas)] = 1;
		decc.push_back(Vec(mas));
		
		int res = -1;


		Vec vec;

		if (check(Vec(mas)))
			res = 0;
		else
		while (true) {
			vec = decc.front();
			decc.pop_front();
			int id = mapa[vec];

			for (int j = 0; j < n - 1; ++j) {
				swap(vec.mas[j], vec.mas[j + 1]);

				if (check(vec)) {
					res = id;
					break;
				}


				if ( mapa[vec] == 0) {
					mapa[vec] = id + 1;
					decc.push_back(vec);
				}

				swap(vec.mas[j], vec.mas[j + 1]);
			}

			if (res > -1)
				break;

		}

		

		/*
		int res = 0;
		for (int j = 0; j < n; ++j)
			if (mas[j] > j + 1) {
				res += mas[j] - (j + 1);
				int tmp = mas[j];
				for (int m = j + 1; m < tmp; ++m)
					mas[m - 1] = mas[m];
				mas[tmp - 1] = tmp;
				--j;
			}

		*/
		printf("Case #%d: %d\n", i + 1, res);
	}




	return 0;
}