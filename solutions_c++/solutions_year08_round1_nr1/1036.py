#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

struct case_data {
	vector<int> v1;
	vector<int> v2;
};

void read_case(ifstream &in, case_data &cd)
{
	int n, c = 0;
	in >> n;
	while (c++ != n) {
		int temp;
		in >> temp;
		cd.v1.push_back(temp);
	}
	c = 0;
	while (c++ != n) {
		int temp;
		in >> temp;
		cd.v2.push_back(temp);
	}
}

long long sp(case_data &cd) {
	long long ret = 0;
	for (vector<int>::iterator i(cd.v1.begin()), i2(cd.v2.begin()), e(cd.v1.end()); i != e; ++i, ++i2) {
		ret += *i * *i2;
	}
	return ret;
}

void solve_case(int case_num, case_data &cd)
{
	long long min = sp(cd);
	case_data cd2(cd);
	while (next_permutation(cd2.v1.begin(), cd2.v1.end())) {
		long long min2 = sp(cd2);
		if (min2 < min) min = min2;
	}
	while (prev_permutation(cd.v1.begin(), cd.v1.end())) {
		long long min2 = sp(cd);
		if (min2 < min) min = min2;
	}
	cout << "Case #" << case_num << ": " << min  << endl;
}


int main(int argc, char* argv[])
{
	//make sure we have an argument
	if (argc == 1) {
		cout << "Usage: " << argv[0] << " <filename>" << endl;
		return 1;
	}
	//read the data
	int N, case_num;
	ifstream in(argv[1]);
	in >> N;

	for (case_num = 1; case_num <= N; ++case_num) {
		case_data cd;
		//read case data into structure
		read_case(in, cd);	
		//solve this case 
		solve_case(case_num, cd);
	}

	in.close();
	return 0;
}

