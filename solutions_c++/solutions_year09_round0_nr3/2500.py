#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdio>

using namespace std;

int count_wtcj(string &s, string &p, int os, int op)
{
	int sum, i;

	if(op >= p.length()){
		return 1;
	}

	sum = 0;
	for(i = os; i < s.length(); i++){
		if(s.at(i) == p.at(op)){
			sum += count_wtcj(s, p, i, op + 1) % 10000;
		}
	}
	return sum;
}

int main()
{
	int i, n;
	string s;
	string p = "welcome to code jam";
	ifstream ifs("C-small-attempt1.in");
	ofstream ofs("C-small-attempt1.out");

	ifs >> n;
	ifs.ignore();
	for(i = 1; i <= n; i++){
		getline(ifs, s);
		ofs << "Case #" << i << ": " << setw(4) << setfill('0') << count_wtcj(s, p, 0, 0) << endl;
	}
	return 0;
}