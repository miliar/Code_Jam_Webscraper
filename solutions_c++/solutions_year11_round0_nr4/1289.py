#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

float permutations(int total, int looking = 1);
float factorial(int y, int lower=0);

int main(int argc, char **args)
{
	int T=0;
	cin >> T;
	for(int qwerty = 0; qwerty < T; qwerty++) {
		vector<int> elements, sorted;
		int count, t, needSorting=0;
		cin >> count;
		for(int i=0; i < count; i++) {
			cin >> t;
			elements.push_back(t);
		}
		sorted = elements;
		sort(sorted.begin(), sorted.end());
		for(int i=0; i < sorted.size(); i++) {
			if(elements[i] != sorted[i]) {
				needSorting++;
			}
		}
		printf("Case #%d: %.6f\n", qwerty+1, permutations(needSorting));
	}
	return 0;
}

float factorial(int y, int lower)
{
	float total = y;
	for(int i=y-1; i > lower; i--) {
		total *= i;
	}
	return total;
}

float permutations(int total, int looking)
{
	return factorial(total, total - looking);
}