#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main()
{
	ifstream inputFile("input.txt", ifstream::in);
	ofstream outputFile("output.txt", ifstream::out);

	long t;

	inputFile >> t;

	for(long round = 0; round < t; ++round) {

		long r, k, n;
		long totalRevenue = 0;
		list<long> groupList;

		inputFile >> r;
		inputFile >> k;
		inputFile >> n;

		//		cout << "Round: " << round << endl;
		//		cout << "N: " << n << " K: " << k << endl;

		long tempVal;
		for(long n0 = 0; n0 < n; ++n0) {
			inputFile >> tempVal;
			groupList.push_back(tempVal);
		}
		
		int k0, g, kPerR;
		for(int r0 = 0; r0 < r; ++r0) {

			k0 = 0;
			kPerR = 0;

			while(k0 < k)
			{
				g = groupList.front();

				if(g > (k-k0) || kPerR == (n))
					break;

				k0 += g;
				groupList.pop_front();
				groupList.push_back(g);
				++kPerR;
			}

			totalRevenue += k0;
		}

		outputFile << "Case #" << round+1 << ": " << totalRevenue << endl;
	}

	return 0;
}