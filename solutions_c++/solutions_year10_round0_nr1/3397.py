#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cassert>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	//ifstream InputFile("A-small-attempt1.in");
	ifstream InputFile("A-large.in");
	ofstream OutputFile("A.out");

	int T;
	InputFile >> T;

	//bool snappers[40];

	for (int i=0; i<T; ++i)
	{
		int N, K;
		InputFile >> N >> K;

		/*for (int j=0; j<N; ++j)
		{
			snappers[j] = false;
		}

		for (int k=0; k<K; ++k)
		{
			for (int l=0; l<N; ++l)
			{
				if (snappers[l])
				{
					snappers[l] = false;
					continue;
				}
				else
				{
					snappers[l] = true;
				}
				break;
			}
		}*/

		string result;
		//if (snappers[N-1])
		int mod = 1;
		for (int j=0; j<N; ++j)
		{
			mod *= 2;
		}
		if ((K+1) % mod == 0)
		{
			result = "ON";
		}
		else
		{
			result = "OFF";
		}

		OutputFile << "Case #" << i+1 << ": " << result << endl;
		cout << "Case #" << i+1 << ": " << result << endl;
	}

	return 0;
}

