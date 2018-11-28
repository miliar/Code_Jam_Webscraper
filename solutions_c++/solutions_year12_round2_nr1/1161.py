// GoogleJam.cpp : Defines the entry point for the console application.
//

#include "stdlib.h"
#include "iostream"
#include "vector"
#include "algorithm"

using namespace std;

struct mas_index {
	int value;
	int index;
};

bool compare(mas_index a, mas_index b) {
	if (a.value > b.value) {
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
		int N;
		cin >> N;
		int sum_values = 0;
		std::vector<mas_index> mas;
		for (int j = 0; j < N; j++) {
			int temp;
			cin >> temp;
			sum_values += temp;
			mas_index t;
			t.index = j;
			t.value = temp;
			mas.push_back(t);
		}
		sort(mas.begin(), mas.end(), compare);

		float sum_dop;
		int index;
		std::vector<float> vote;
		for (int k = 0; k < N; k++) {
			int max_number = mas[k].value;
			sum_dop = 0.f;
			vote.clear();
			vote.resize(N, 0);
			for (int j = k + 1; j < N; j++) {
				int d;
				d = max_number - mas[j].value;
				vote[j] += (float)d / (float)sum_values;
				sum_dop += vote[j];
			}
			if (sum_dop <= 1.f) {
				index = k + 1;
				break;
			}
		}
		float sum_all = (1.f - sum_dop) / (float)(N - index + 1);
		for (int j = index - 1; j < N; j++) {
			vote[j] += sum_all;
		}

		cout << "Case #" << (i + 1) << ": " ;
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (mas[k].index == j) {
					printf("%.6f ", vote[k] * 100);	
					break;
				}
			}
		}
		cout << endl;
	}
	return 0;
}

