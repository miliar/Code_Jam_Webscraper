#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int n, k;
		cin >> n >> k;
		int cnt = 0;
		for (int i = 0; i < n; ++i)
			cnt = cnt*2+1;
		cout << "Case #" << test << ": ";
		if ( k%(cnt+1) != cnt )
			cout << "OFF";
		else
			cout << "ON";
		cout << endl;
	}
	return 0;
}