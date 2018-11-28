#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cassert>
#include <algorithm>
#include <list>

using namespace std;

int q[1000];

int main(int argc, char* argv[])
{
	ifstream InputFile("C-small-attempt0.in");
	ofstream OutputFile("C.out");

	int T;
	InputFile >> T;

	for (int i=0; i<T; ++i)
	{
		int R, k, N;
		InputFile >> R >> k >> N;

		for (int j=0; j<N; ++j)
		{
			InputFile >> q[j];
		}

		long money = 0;
		int front = 0;
		int oldfront = 0;
		for (int j=0; j<R; ++j)
		{
			int people=0;

			while (true)
			{
				if (people + q[front] > k)
				{
					oldfront = front;

					money += people;
					break;
				}
				else
				{
					people += q[front];
					++front;
				}
				front = front % N;
				if (front == oldfront)
				{
					money += people;
					break;
				}
			}
		}

		OutputFile << "Case #" << i+1 << ": " << money << endl;
		cout << "Case #" << i+1 << ": " << money << endl;
	}

	return 0;
}

