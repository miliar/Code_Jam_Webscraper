#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
using namespace std;

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

int main() {

	int icase = 0;
	int ilett = 0;
	int idict = 0;
	vector<string> dic;
	fstream infile("A-large.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);

	for(int i=0; i<icase; i++)
	{
		int res = 0;
		getline(infile, line);
		sscanf(line.c_str(), "%d %d", &ilett, &idict);
		res = ((idict+1)%int(pow(2, ilett)) == 0);

		if(res)
			cout << "Case #" << i+1 << ": " << "ON" << endl;
		else
			cout << "Case #" << i+1 << ": " << "OFF" << endl;
	}

	return 0;
}
