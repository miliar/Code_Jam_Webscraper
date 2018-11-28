// 2011-qual-C.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <algorithm>


using std::cin;
using std::cout;
using std::endl;
using std::min;


void test_case(int case_num)
{
	int num_pieces = 0;
	unsigned int total = 0, v;
	unsigned int smallest = 0xffffffff;
	int impossible = 0;

	cin >> num_pieces;

	for (int i = 0; i < num_pieces; i++)
	{
		cin >> v;
		impossible ^= v;
		total += v;
		smallest = min(smallest, v);
	}
	
	cout << "Case #" << case_num + 1 << ": ";
	if (impossible)
		cout << "NO";
	else
		cout << total - smallest;
	cout << endl;

}



int main(int argc, char* argv[])
{
	int num_cases = 0;
	cin >> num_cases;

	for (int i = 0; i < num_cases; i++)
		test_case(i);

	return 0;
}

