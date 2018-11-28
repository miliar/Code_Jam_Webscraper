#include <iostream>
#include <cmath> 
#include <vector>
#include <algorithm>
#include <numeric>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <set>
#include <list>
#include <utility>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <windows.h>

using namespace std; 

int num_rec(int first, int last){
	string a, b;
	stringstream ss; 
	ss << first << " " << last; 
	ss >> a >> b;
	string cm = "";
	string cn = "";

	if(a.length() == 1 && b.length() == 1)
		return 0;

	map<string, bool>result; 
	vector<string>ranges;
	int count = 0;

	for(int i = first; i <= last; i++){
		stringstream parse;
		string test; 
		parse << i; 
		parse >> test; 
		ranges.push_back(test);
	}

	for(int i = 0; i < ranges.size(); i++){
		cm = ranges[i];
		cn = ranges[i];

		int len = ranges[i].length();

		for(int j = 0; j < len; j++){
			cm = cm.substr(j) + cm.substr(0, j);
			stringstream sr; 
			int y, z;
			sr << cm << " " << cn;
			sr >> y >> z;
			if(y <= last && y > z && y >= first){
				result[cn + cm] = true;
			}
		}
	}
	return result.size();
}

void main()
{
	int n, j = 1; 
	string in;

	string filename = "input.txt";
	fstream fin(filename.c_str(), ios::in);
	fstream fout("output.txt", ios::out);

	fin >> n;
	fin.ignore();

	while(n--){
		string out = "";
		int a, b, t = 0;
		stringstream ss;
		ss << "Case #" << j << ": ";

		fin >> a >> b;

		t = num_rec(a, b);

		ss << t;
		getline(ss, out);
		if(n != 0)
			out += "\n";
		
		fout << out;
		j++;
	}
	system("pause");
}