#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool smaller(int index, vector<int> &val, vector<int> &biggest) {
	int i = index;
	int j = biggest.size() - 1;
	if (biggest[j] < val[i] || val[i] == 0) {
		return false;
	} else if (biggest[j] > val[i]) {
		return true;
	} else {
		i--;
		if (i == -1)
			i = val.size() - 1;
	}
	j--;
	
	while (i != index )
	{
		if (biggest[j] < val[i]) {
			return false;
		} else if (biggest[j] > val[i]) {
			return true;
		} else {
			i--;
			if (i == -1)
				i = val.size() - 1;
		}
		j--;
	}
	return true;
}


bool notCymetricAndSmaller(int index, vector<int> &val) {

	int i = index;
	int j = val.size() - 1;
	if (val[j] != val[i])
		return val[j] > val[i];
	i--;
	if (i == -1)
		i = val.size() - 1;
	j--;
	
	while (i != index )
	{
		if (val[j] != val[i])
			return val[j] > val[i];
		i--;
		if (i == -1)
			i = val.size() - 1;
		j--;
		
	}
	return false;
}

vector<int> toInt(int val) {
	vector<int> ret;
	while (val > 0) {
		ret.push_back(val % 10);
		val /= 10;
	}
	return ret;
}

void incr(vector<int> &val) {
	int i = 0;
	val[i]++;
	while (i < val.size() && val[i] == 10) {
		val[i] = 0;
		i++;
		if (i < val.size())
			val[i]++;
	}
}

int vecToInt(int index, vector<int> &val) {
	int i = index;
	int ret = val[i];
	i--;
	if (i < 0)
		i = val.size() - 1;
	while (i != index) {
		ret = ret * 10 + val[i];
		i--; 
		if (i < 0)
			i = val.size() - 1;
	}
	return ret;
}

int main() {
	std::cout << "Hello world" << std::endl;
	
	ifstream inFile;
    inFile.open("C-small-attempt0.in");

	ofstream outFile;
	outFile.open("out");

	int caase = 1;
	int total;
	inFile >> total;

	while ( caase <= total )
	{
		int LOWER;
		int UPPER;
		inFile >> LOWER;
		inFile >> UPPER;
		vector<int> lower = toInt(LOWER);
		vector<int> upper = toInt(UPPER);
		set<pair<int, int> > setje;

		long res = 0;
		for (int i = LOWER; i <= UPPER; i++) { // < or <= ?
			for (int j = 0; j < lower.size() - 1; j++)
			{
				if (smaller(j, lower, upper) && notCymetricAndSmaller(j, lower)) {
					int niew = vecToInt(j, lower);
					pair<int, int> p(niew, i);
					if (niew >= LOWER && niew <= UPPER) {
						setje.insert(p);
					}
				}
			}

			incr(lower);
		}
		outFile << "Case #" << caase << ": "<< setje.size() << endl;
		cout << "Case #" << caase << ": "<< setje.size() << endl;
		caase++;
	}
	cin.get();
}