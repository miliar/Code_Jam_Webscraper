#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<int> except_number_set;

int count_number_of_digits(int number)
{
	int counts = 1;
	for(int i = 10 ; number / i != 0 ; i *= 10) {
		++counts;
	}
	return counts;
}

int get_number(const vector<int>& numbers)
{
	int number = 0;
	int pow_number = 1;
	for(size_t i = 0 ; i < numbers.size() ; ++i, pow_number *= 10) {
		number += numbers.at(numbers.size() - 1 - i) * pow_number;
	}
	return number;
}

int factorial(int n)
{
	if (n == 0)
		return 1;
	return n * factorial(n - 1);
}

int make_except_number_set(const int A, const int B)
{
	int targetcounts = 0;

	const int number_of_digits = count_number_of_digits(A);
	vector<int> numbers;

	int numberA = A;
	for(int i = number_of_digits - 1 ; i >= 0 ; --i, numberA /= 10) {
		numbers.insert(numbers.begin(), numberA % 10);
	}

	for (int i = 0 ; i < number_of_digits - 1 ; ++i) {
		const int temp = numbers.at(numbers.size() - 1);
		numbers.pop_back();
		numbers.insert(numbers.begin(), temp);

		const int number = get_number(numbers);
		if (A < number && number <= B && count_number_of_digits(number) == number_of_digits && except_number_set.end() == except_number_set.find(number)) {
			except_number_set.insert(number);
			++targetcounts;
		}
	}

	if (targetcounts < 2)
		return targetcounts;

	const int n = targetcounts + 1;
	const int r = 2;
	return factorial(n) / (factorial(r) * factorial(n - r));
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.txt", "w", stdout);

	int T;
	cin >> T;

	for (int i = 0 ; i < T ; ++i) {
		int A;
		cin >> A;
		int B;
		cin >> B;

		int counts = 0;
		except_number_set.clear();
		if (A / 10) {
			for (int n = A ; n < B ; ++n) {
				if (except_number_set.end() != except_number_set.find(n))
					continue;

				counts += make_except_number_set(n, B);
			}
		}

		cout << "Case #" << i + 1 << ": ";
		cout << counts << endl;
	}
}
