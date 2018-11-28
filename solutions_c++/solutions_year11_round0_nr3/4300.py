#include <iostream>
#include <cstddef>
using namespace std;

int main()
{
	int number_of_problems;
	cin >> number_of_problems;
	for (int i = 0; i < number_of_problems; ++i)
	{
		int min_number = 0x7FFFFFFF, total_xor = 0, total_sum = 0;
		int size_of_problem;
		cin >> size_of_problem;
		for (int j = 0; j < size_of_problem; ++j)
		{
			int i;
			cin >> i;
			total_xor ^= i;
			total_sum += i;
			min_number = min(i, min_number);
		}
		cout << "Case #" << i + 1 << ": ";
		if (total_xor == 0) cout << total_sum - min_number;
		else cout << "NO";
		cout << endl;
	}
}
