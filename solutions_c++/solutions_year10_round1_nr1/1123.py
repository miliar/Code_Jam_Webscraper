#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

class Rotate {
public:
	string solve(int n, int k, vector<vector<char> >& table)
	{
		string R(k, 'R');
		string B(k, 'B');
		bool found_R = false;
		bool found_B = false;
		for (vector<vector<char> >::iterator p =table.begin(); p != table.end(); ++p) {
			vector<char> line(*p);
			for (int cnt = 0; cnt < n - 1; cnt++) {
				for (int i = cnt; i < n && line[cnt] == '.'; i++) {
					rotate(line.begin() + cnt, line.begin() + cnt + 1, line.end());
				}
			}
			*p = line;
		}
		string line;
		for (int i = 0; i < n; i++) {
			line = "";
			for (int j = 0; j < n; j++) line += table[i][j];
			if (line.find(R) != string::npos)found_R = true;
			if (line.find(B) != string::npos)found_B = true;
		}
		for (int i = 0; i < n; i++) {
			line = "";
			for (int j = 0; j < n; j++) line += table[j][i];
			if (line.find(R) != string::npos)found_R = true;
			if (line.find(B) != string::npos)found_B = true;
		}
		for (int i = 0; i < n; i++) {
			line = "";
			for (int j = 0; j < n - i; j++) line += table[j+i][j];
			if (line.find(R) != string::npos)found_R = true;
			if (line.find(B) != string::npos)found_B = true;
//			cerr << line << endl; /////
		}
		for (int i = 0; i < n; i++) {
			line = "";
			for (int j = 0; j < n - i; j++) line += table[j][j+i];
			if (line.find(R) != string::npos)found_R = true;
			if (line.find(B) != string::npos)found_B = true;
//			cerr << line << endl; /////
		}
		for (int i = 0; i < n; i++) {
			line = "";
			for (int j = 0; j < n - i; j++) line += table[j+i][n-j-1];
			if (line.find(R) != string::npos)found_R = true;
			if (line.find(B) != string::npos)found_B = true;
//			cerr << line << endl; /////
		}
		for (int i = 0; i < n; i++) {
			line = "";
			for (int j = 0; j < n - i; j++) line += table[j][n-j-1-i];
			if (line.find(R) != string::npos)found_R = true;
			if (line.find(B) != string::npos)found_B = true;
//			cerr << line << endl; /////
		}

		string ans;
		if (found_R && found_B) ans = "Both";
		else if (found_R) ans = "Red";
		else if (found_B) ans = "Blue";
		else ans = "Neither";
		return ans;
	}
};

int main()
{
//	fstream fs("test.in", ios_base::in);
//	fstream fs("A-small-attempt0.in", ios_base::in);
	fstream fs("A-large.in", ios_base::in);
	string line;
	stringstream ss;

	Rotate rt;

	getline(fs, line);
	ss.str(line);
	int T, N, K;
	ss >> T;
	ss.clear();  ss.str("");
	int cnt = 0;
	for (int i = 0; i < T; i++) {
		vector<vector<char> > table;
		getline(fs, line);
		ss.str(line);
		ss >> N >> K;
		ss.clear();  ss.str("");
		for (int j = 0; j < N; j++) {
			getline(fs, line);
			ss.str(line);
			vector<char> temp;
			for (int k = 0; k < line.size(); k++)
				temp.push_back(line[k]);
			reverse(temp.begin(), temp.end());
			table.push_back(temp);
			ss.clear();  ss.str("");
		}
		cout << "Case #" << ++cnt << ": " << rt.solve(N, K, table) << endl;
	}

	return 0;
}
