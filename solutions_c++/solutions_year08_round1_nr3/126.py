#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	for (int cNum = 1; cNum <= cases; cNum++)
	{
		int num;
		
		int digs[] = {1, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
		
		int n;
		cin >> n;
		num = digs[n];
		
		cout << "Case #" << setw(0) << cNum << ": " << setfill('0') << setw(3) << num << endl;
	}
	return 0;
}