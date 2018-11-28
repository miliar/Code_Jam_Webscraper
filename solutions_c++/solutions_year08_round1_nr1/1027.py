#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <functional>
#include <numeric>

using namespace std;

int main (int argc, char *argv[])
{
	if (argc < 2) return 1;
	ifstream file(argv[1]);
	if (!file) return 2;
	unsigned int num;
	file >> num;
	//	cout << num;
	unsigned int caseNum = 1;

	while ( caseNum <= num )
	{
		cout <<"Case #" <<caseNum <<": ";
		int n;
		file >>n;
		vector<int> x, y;
		int tmp;
		for (int i=0; i<n; i++)
		{
			file >> tmp;
			x.push_back(tmp);
		}
		for (int i=0; i<n; i++)
		{
			file >> tmp;
			y.push_back(tmp);
		}
		sort(x.begin(), x.end(), less<int>());
		sort(y.begin(), y.end(), greater<int>());
		int res = inner_product(x.begin(), x.end(), y.begin(), 0);

		cout <<res <<endl;
		caseNum++;
	}
	return 0;
}
