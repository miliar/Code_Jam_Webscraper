#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

//#define p_calc(x, y) ((x|y) - (x&y))
#define	p_calc(x, y)	(x^y)

int main(int argc, char **argv)
{
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
	if (!fin || !fout)
		exit(1);
	int test_cases;
	fin >> test_cases;
	for(int test_cases_i = 0; test_cases_i < test_cases; test_cases_i++) {
		int num_input;
		fin >> num_input;
		vector<int> in;
		for(int i = 0;i < num_input;i++) {
			int tmp;
			fin >> tmp;
			in.push_back(tmp);
		}
		// process input
		/*
		cout << "test case " << test_cases_i << endl;
		for(int i = 0; i < in.size(); i++)
			cout << in[i] << " ";
		cout << '\n';
		*/
		// test for whether there is a solution
		int p_sum = 0;
		int sum = 0;
		for(int i = 0; i < num_input; i++) {
			p_sum ^= in[i];
			sum += in[i];
		}
		int res = -1;
		fout << "Case #" << test_cases_i+1 << ": ";
		if (p_sum == 0) {
			sort(in.begin(), in.end());
			res = sum-in[0];
			fout << res << endl;
		}
		else
			fout << "NO" << endl;
	}

	fin.close();
	fout.close();
	return 0;
}