#include <iostream>
#include <algorithm>
#include <vector>


size_t N;
char A[100][100];
double Sum[100];
size_t Cnt[100];

std::vector<double> Work() {
	std::cin >> N;
	for (size_t i = 0; i < N; ++i)
		std::cin >> A[i];
	std::vector<double> WP, OWP, OOWP, res;
	for (size_t i = 0; i < N; ++i) {
		Sum[i] = 0.0;
		Cnt[i] = 0;
		for (size_t j = 0; j < N; ++j) {
			if (A[i][j] != '.') {
				Sum[i] += (A[i][j] == '1' ? 1.0 : 0.0);
				++Cnt[i];
			}
		}
		WP.push_back(Cnt[i] ? Sum[i] / Cnt[i] : 0.0);
	}
	for (size_t i = 0; i < N; ++i) {
		double osum = 0.0;
		size_t ocnt = 0;
		for (size_t j = 0; j < N; ++j) {
			if (A[j][i] != '.') {
				size_t cnt = Cnt[j] - 1;
				osum += (cnt ? (Sum[j] - (A[j][i] == '1' ? 1 : 0)) / cnt : 0.0);
				++ocnt;
			}
		}
		OWP.push_back(ocnt ? osum / ocnt : 0.0);
//		std::cout << std::endl << "*****" << std::endl << WP[i] << ' ' << OWP[i] << std::endl;
	}
	for (size_t i = 0; i < N; ++i) {
		double oosum = 0.0;
		size_t oocnt = 0;
		for (size_t j = 0; j < N; ++j) {
			if (A[i][j] != '.') {
				oosum += OWP[j];
				++oocnt;
			}
		}
		OOWP.push_back(oocnt ? oosum / oocnt : 0.0);
		res.push_back(0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
	}
	return res;
}

void Output(int t, const std::vector<double> &res) {
	std::cout << "Case #" << t << ":" << std::endl;
	for (std::vector<double>::const_iterator it = res.begin(), end = res.end(); it != end; ++it)
		std::cout << *it << std::endl;
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		Output(i, Work());
	}
	return 0;
}

