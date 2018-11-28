// 2010-qual-A.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;

using std::min;
using std::max;
using std::abs;


void test_case(int case_num)
{
	int num_buttons;

	char who;
	int button;

	int o_last = 0, o_pos = 1;
	int b_last = 0, b_pos = 1;

	int diff;


	cin >> num_buttons;

	for (int i = 0; i < num_buttons; i++)
	{
		cin >> who >> button;

		if (who == 'O')
		{
			diff = abs(o_pos - button) + 1;
			o_last = max(o_last + diff, b_last + 1);
			o_pos = button;
		}
		else
		{
			diff = abs(b_pos - button) + 1;
			b_last = max(b_last + diff, o_last + 1);
			b_pos = button;
		}
	}

	cout << "Case #" << case_num + 1 << ": " << max(o_last, b_last) << endl;



}



int main(int argc, char* argv[])
{
	int num_cases = 0;

	cin >> num_cases;

	for (int i = 0; i < num_cases; i++)
		test_case(i);

	return 0;
}

