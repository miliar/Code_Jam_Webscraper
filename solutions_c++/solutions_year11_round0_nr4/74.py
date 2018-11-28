// 2011-qual-D.cpp : Defines the entry point for the console application.
//



#include <iostream>


using std::cin;
using std::cout;
using std::endl;


void test_case(int case_num)
{
	int count = 0;

	int num_ints = 0, v = 0;

	cin >> num_ints;

	for (int i = 1; i <= num_ints; i++)
	{
		cin >> v;
		if (v != i)
			count++;
	}
	

	cout << "Case #" << case_num + 1 << ": " << count << ".000000" << endl;

}


int main(int argc, char* argv[])
{
	int num_cases = 0;
	cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
		test_case(i);
	
	return 0;
}

