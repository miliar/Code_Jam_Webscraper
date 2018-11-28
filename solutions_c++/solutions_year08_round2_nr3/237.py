#include <algorithm>
#include <iostream>
#include <list>
#include <set>
#include <string>
#include <vector>

void solve_one(int case_n)
{
	int K;
	std::cin >> K;
	int n;
	std::cin >> n;
	std::vector<int> indices;
	for (int i = 0; i < n; ++i) {
		int d;
		std::cin >> d;
		indices.push_back(d);
	}
	std::list<int> deckl;
	std::vector<int> deck;
	for (int i = 0; i < K; ++i) {
		deckl.push_back(i);	
	}
	deck.resize(K);
	int curr = -1;
	std::list<int>::iterator it = deckl.begin();
	for (int i = 0; i < K; ++i) {
		for (int j = 0; j < i; ++j) {
			++it;
			if (it == deckl.end()) {
				it = deckl.begin();
			}		
		}
		deck[*it] = i + 1;
		it = deckl.erase(it);
		if (it == deckl.end()) {
			it = deckl.begin();
		}
	}	
//	for (int i = 1; i <= K; ++i) {
//		std::cout << "it " << i << " curr " << curr << " -> ";
//		for (int j = 0; j < i; ++j) {
//			curr++;
//			curr %= K;
//			while (used[curr]) {
//				curr++;
//				curr %= K;
//			}
//			std::cout << curr << " ";
//		}
//		std::cout << curr << "\n";
//		used[curr] = true;
//		deck[curr] = i;
//	}
//	for (int i = 0; i < K; ++i) {
//		std::cout << deck[i] << " ";
//	}
//	std::cout << "\n";
	std::cout << "Case #" << case_n << ": ";
	for (int i = 0; i < n; ++i) {
		std::cout << deck[indices[i] - 1] << " ";
	}
	std::cout << "\n";
}

int main()
{
	int N;
	std::cin >> N;
	for (int i = 1; i <= N; ++i) {
		solve_one(i);
	}
}
