#include <iostream>
#include <fstream>
#include <cstring>
#include <queue>

using namespace std;

typedef unsigned int uint;

int main(int argc, char * argv[]) {
	
	fstream dataSet ("data.txt", fstream::in);
	fstream output ("out.txt", fstream::out);

	int testCaseCount;
	dataSet >> testCaseCount;

	for (int z = 0; z < testCaseCount; z++) {
		uint rides, capacity, groupCount;
		uint totalPassengers;		

		dataSet >> rides;
		dataSet >> capacity;
		dataSet >> groupCount;

		queue<uint> groups;
		queue<uint> tmpgroups;

		for (int i = 0; i < groupCount; i++) {
			uint tmp;
			dataSet >> tmp;
			groups.push(tmp);
			totalPassengers += tmp;
			}

		if (totalPassengers <= capacity) {
			output << "Case #" << (z+1) << ": " << totalPassengers * rides << endl;
			continue;
			}

		int total = 0;
		for (int i = 0; i < rides; i++) {
			int c = 0;
			while (groups.size() > 0 && c + groups.front() <= capacity) {
				c += groups.front();
				tmpgroups.push(groups.front());
				groups.pop();
				}

			total += c;

			while (tmpgroups.size() > 0) {
				groups.push(tmpgroups.front());
				tmpgroups.pop();
				}

			if (total % totalPassengers == 0) {
				int t = total;
				int r = i;
				while (i - t >= 0) {
					total += t;
					i -= r;
					}
				}
			}
		

		output << "Case #" << (z+1) << ": " << total << endl;
		}


	dataSet.close();
	output.close();

	return 0;
	}
