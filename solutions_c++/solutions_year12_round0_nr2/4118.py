#include "stdlib.h"
#include "iostream"
#include "vector"
#include "algorithm"

using namespace std;

bool compare(int a, int b) {
	if (a > b) {
		return true;
	} else {
		return false;
	}
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		int s;
		int p;
		cin >> n >> s >> p;
		std::vector<int> mas;
		for (int j = 0; j < n; j++) {
			int temp;
			cin >> temp;
			mas.push_back(temp);
		}
		sort(mas.begin(), mas.end(), compare);
		int answer = 0;
		for (int i = 0; i < n; i++) {
			int min_score;
			if (p < 1) {
				min_score = 0;
			} else {
				min_score = p - 1;
			}
			int sum_min_no_surprise = p + min_score + min_score;
			if (mas[i] >= sum_min_no_surprise) {
				answer++;
			} else {
				int min_score;
				if (p < 2) {
					min_score = 0;
				} else {
					min_score = p - 2;
				}
				int sum_min_surprise = p + min_score + min_score;
				if (mas[i] >= sum_min_surprise && s > 0) {
					s--;
					answer++;
				} else {
					break;
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << answer << endl;
	}
	return 0;
}
