#include <iostream>
using namespace std;

void solve(int case_no)
{
	int xor_val=0, sum=0, min=0;
	int n, i;
	cin >> n;
	for(i = 0; i < n; i++) {
		int cur;
		cin >> cur;
		xor_val ^= cur;
		sum += cur;
		if(i == 0 || cur < min)
			min = cur;
	}
	if(xor_val != 0)
		cout << "Case #" << case_no << ": NO" << endl;
	else
		cout << "Case #" << case_no << ": " << (sum-min) << endl;
}

int main()
{
	int case_count;
	cin >> case_count;
	for(int i = 1; i <= case_count; i++)
		solve(i);
	return 0;
}
