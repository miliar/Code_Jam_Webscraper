#include <fstream>
#include <iostream>

using std::ifstream;
using std::cout;
using std::endl;
using std::cin;

inline int abs(int x) 
{
	return x < 0 ? -x : x;
}

int main()
{
	int T = 0;
	int N = 0;

	ifstream in("in.in");

	in >> T;

	for(int k = 0; k < T; k++)
	{
		in >> N;
		char* colors = new char[N];
		int* buttons = new int[N];
		for(int j = 0; j < N; j++)
		{
			in >> colors[j];
			in >> buttons[j];
		}

		int lastBpos = 1;
		int lastOpos = 1;
		int lastOtime = 0;
		int lastBtime = 0;
		int seconds = 0;

		for(int i = 0; i < N; i++)
		{
			if(colors[i] == 'O')
			{
				if(abs((buttons[i] - lastOpos)) > (seconds - lastOtime))
				{
					seconds += abs((buttons[i] - lastOpos)) - (seconds - lastOtime) + 1;
				}else
				{
					seconds++;
				}
				lastOpos = buttons[i];
				lastOtime = seconds;
			}else if(colors[i] == 'B')
			{
				if(abs((buttons[i] - lastBpos)) > (seconds - lastBtime))
				{
					seconds += abs((buttons[i] - lastBpos)) - (seconds - lastBtime) + 1;
				}else
				{
					seconds++;
				}
				lastBpos = buttons[i];
				lastBtime = seconds;
			}
		}

		cout << "Case #" << k+1 << ": " << seconds << endl;

		delete[] colors;
		delete[] buttons;
	}

	return 0;
}