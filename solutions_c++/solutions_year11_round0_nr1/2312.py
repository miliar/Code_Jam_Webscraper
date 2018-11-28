#include<iostream>

/*
 * Reads from stdin and writes to stdout
 *
 * Usage: program < input.txt > output.txt
 */

using namespace std;

int abs(int x)
{
	return (x > 0) ? x : -x;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 0 ; t < T ; t++)
	{
		int pB = 1 , pO = 1;
		int tB = 0 , tO = 0 , next = 0;

		int N;
		int but;
		char buff[10];
		cin >> N;
		for(int i = 0 ; i < N ; i++)
		{
			cin >> buff >> but;
			if(buff[0] == 'B')
			{
				next = max(next + 1 , tB + abs(but - pB) + 1);
				pB = but;
				tB = next;
			}
			else
			{
				next = max(next + 1 , tO + abs(but - pO) + 1);
				pO = but;
				tO = next;
			}
		}
		cout << "Case #" << (t + 1) << ": " << next << "\n";
	}
}
