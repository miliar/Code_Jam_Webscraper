#include <map>
#include <deque>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{	
	int cases;
	string tmp;
	ifstream input("input.txt");	
	ofstream output("output.txt");
	input >> cases;
	int n;
	vector<int> v1, v2;
	for(int l = 1; l <= cases; l++)
	{		
		input >> n;
		v1.assign(n, 0);
		v2.assign(n, 0);
		for(int i = 0; i < n; i++)
			input >> v1[i];
		for(int i = 0; i < n; i++)
			input >> v2[i];
		sort(v1.begin(), v1.end());
		sort(v2.rbegin(), v2.rend());
		long long mlp = 0;
		for(int i = 0; i < n; i++)
			mlp += v1[i] * v2[i];
		output << "Case #" << l << ": " << mlp << endl;
	}
	return 0;
}