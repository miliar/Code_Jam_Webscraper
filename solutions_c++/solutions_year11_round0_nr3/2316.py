#include<iostream>

/*
 * Reads from stdin and writes to stdout
 *
 * Usage: program < input.txt > output.txt
 */

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 0 ; t < T ; t++)
	{
		cerr << "Test #" << t + 1 << "\n";
		int N;
		int x = 0 , sum = 0 , m = 100000000;
		cin >> N;
		for(int i = 0 ; i < N ; i++)
		{
			int cur;
			cin >> cur;
			x ^= cur;
			sum += cur;
			m = min(m , cur);
		}
		if(x == 0)
			cout << "Case #" << t + 1 << ": " << sum - m << "\n";
		else
			cout << "Case #" << t + 1 << ": NO\n";
	}
}
