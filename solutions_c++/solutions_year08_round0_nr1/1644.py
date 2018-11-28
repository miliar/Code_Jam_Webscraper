#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

void solve_one(int case_n)
{
	int S;
	std::cin >> S;
	std::vector<std::string> names;
	names.resize(S);
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int i = 0; i < S; ++i) {
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	}
	int Q;
	std::cin >> Q;
	int switches = 0;
	std::set<std::string> used;
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int i = 0; i < Q; ++i) {
		std::string query;
		std::getline(std::cin, query);
		used.insert(query);
		if (used.size() == S) {
			switches++;
			used.clear();
			used.insert(query);
		}
	}
	std::cout << "Case #" << case_n << ": " << switches << "\n";
}

int main()
{
	int N;
	std::cin >> N;
	for (int i = 1; i <= N; ++i) {
		solve_one(i);
	}
}
