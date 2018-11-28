#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	string str;
	getline(cin, str);
	stringstream ss(str);
	ss >> T;
	for (int test = 1; test <= T; ++test)
	{
		string num;
		getline(cin, num);
		if (!next_permutation(num.begin(), num.end()))
		{
			num += "0";
			sort(num.begin(), num.end());
			size_t p = num.find_first_not_of('0');
			swap(num[0], num[p]);
		}

		cout << "Case #" << test << ": " << num << endl;
	}

	return 0;
}
