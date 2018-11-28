#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;
void solve(ostream& ofs);
bool search(const vector<char>& vec, char c);

int main()
{
	ofstream ofs("output_b.txt");
	int turns;
	cin >> turns;
	for (int i = 1; i <= turns; ++i) {
		ofs << "Case #" << i << ": ";
		solve(ofs);
	}
	
	system("pause");
	return 0;
}

void solve(ostream& ofs)
{
	vector<string> combination;
	vector<string> opposed;
	
	string line;
	int combination_cases;
	cin >> combination_cases;
	for (int i = 0 ; i != combination_cases; ++i) {
		cin >> line;
		combination.push_back(line);
	}
	int opposed_cases;
	cin >> opposed_cases;
	for (int i = 0; i != opposed_cases; ++i) {
		cin >> line;
		opposed.push_back(line);
	}
	
	int length;
	cin >> length;
	cin >> line;
	
	vector<char> element_list;
	for (string::size_type i = 0; i != length; ++i) {
		if (element_list.size() == 0) {
			element_list.push_back(line[i]);
			continue;
		}
		
		bool flag = false;
		char c = element_list[element_list.size() - 1];
		for (int j = 0; j != combination_cases; ++j) {
			if ((c == combination[j][0] && line[i] == combination[j][1]) ||
			(line[i] == combination[j][0] && c == combination[j][1])) {
				element_list[element_list.size() - 1] = combination[j][2];
				flag = true;
				break;
			}
		}		
		if (!flag) {
			element_list.push_back(line[i]);
		}
		
		for (int j = 0; j != opposed_cases; ++j) {
			if (search(element_list, opposed[j][0]) && search(element_list, opposed[j][1])) {
				element_list.clear();
			}
		}
	}
	
	ofs << '[';
	for (vector<char>::size_type i = 0; i != element_list.size(); ++i) {
		ofs << element_list[i];
		if (i != element_list.size() - 1) {
			ofs << ", ";
		}
	}
	ofs << ']' << endl;
}

bool search(const vector<char>& vec, char c)
{
	for (vector<char>::size_type i = 0; i != vec.size(); ++i) {
		if (vec[i] == c) {
			return true;
		}
	}
	return false;
}
