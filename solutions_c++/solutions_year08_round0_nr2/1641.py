#include <algorithm>
#include <deque>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int get_hour()
{
	int h, m;
	std::cin >> h;
	std::cin.ignore(1);
	std::cin >> m;
	return h*60 + m;
}

void solve_one(int case_n)
{
	int T, NA, NB;
	int start_a = 0, start_b = 0;
	std::cin >> T >> NA >> NB;
	std::vector<int> ab, ba;
	std::deque<int> a, b;
	for (int i = 0; i < NA; ++i) { //A to B
		ab.push_back(get_hour());
		b.push_back(get_hour() + T);
	}
	for (int i = 0; i < NB; ++i) { //B to A
		ba.push_back(get_hour());
		a.push_back(get_hour() + T);
	}
	std::sort(ab.begin(), ab.end());
	std::sort(ba.begin(), ba.end());
	std::sort(a.begin(), a.end());
	std::sort(b.begin(), b.end());
	for (size_t i = 0; i < ab.size(); ++i) {
		if (a.empty()) {
			++start_a;
		} else {
			if (a.front() <= ab[i]) {
				a.pop_front();
			} else {
				++start_a;
			}
		}
	}
	for (size_t i = 0; i < ba.size(); ++i) {
		if (b.empty()) {
			++start_b;
		} else {
			if (b.front() <= ba[i]) {
				b.pop_front();
			} else {
				++start_b;
			}
		}
	}
	std::cout << "Case #" << case_n << ": " << start_a << " " << start_b << "\n";	
}



















int main()
{
	int N;
	std::cin >> N;
	for (int i = 1; i <= N; ++i) {
		solve_one(i);
	}
}
