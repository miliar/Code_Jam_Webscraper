#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

ifstream in("D:/JAM/C-large.in");
ofstream out("D:/JAM/out.txt");

int solve_case(vector<int> values) 
{
	int res = 0;
	int min = 0;
	int sum = 0;

	for (int i = 0; i < values.size(); i++) {
		res = res ^ values[i];
		if (values[i] < values[min]) min = i;
		sum += values[i];
	}
	
	if (! res) {
		return sum - values[min];
	} else {
		return -1;
	}
}

int main() 
{
	int n_cases;
	in >> n_cases;
	for (int i = 1; i <= n_cases; i++) {
		int n_candies;
		in >> n_candies;
		vector<int> values;
		for (int j = 1; j <= n_candies; j++) {
			int n;
			in >> n;
			values.push_back(n);
		}
		int res = solve_case(values);
		out << "Case #" << i << ": ";
		if (res == -1) {
			out << "NO" << endl;
		} else {
			out << res << endl;
		}
	}
}



