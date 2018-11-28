#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

vector<int> tokenize(const string &s);
void convertCharArrayToString(string &s, char *c);
int recycle(string &a, string&b, int aint, int bint);
bool stringsSimilar(string &a, string&b);
bool numberStringsSimilar(string &a, string &b);
bool noLeadingZeros(string &s);

int main(int argc, char *argv) {
	string infile = "D:/input.txt";
	string outfile = "D:/output.out";
	
	const int DATASET = 1000;

	ifstream in;
	ofstream out;

	string s = "";
	int count = 0;
	int size = 0;
	vector<int> outputs;

	in.open(infile);
	while ((getline(in, s)) && (count <= size)) {
		if (count == 0) {
			size = atoi(s.c_str());
		}
		else {
			vector<int> tokens = tokenize(s);

			for (unsigned int i = 0; i < tokens.size(); i++) {
				cout << tokens[i] << " ";
			}
			cout << endl;

			char buffer[10];
			string s1;
			string s2;
			itoa(tokens[0], buffer, 10);
			convertCharArrayToString(s1, buffer);
			itoa(tokens[1], buffer, 10);
			convertCharArrayToString(s2, buffer);

			cout << "String 1 = \"" << s1 << "\"" << endl;
			cout << "String 2 = \"" << s2 << "\"" << endl;

			if ((s1.length()) == (s2.length())) {
				if ((tokens[0] >= 1) && (tokens[0] <= tokens[1]) && (tokens[1] <= DATASET)) {
					outputs.push_back(recycle(s1, s2, tokens[0], tokens[1]));
				}
			}
		}

		count++;
	}

	//Output the results
	out.open("D:/output.out", ios::trunc);
	for (unsigned int i = 0; i < outputs.size(); i++) {
		out << "Case #" << i + 1 << ": " << outputs[i] << endl;
	}

	out.close();
	in.close();

	cin >> s;

	return 0;
}

vector<int> tokenize(const string &s) {
	vector<int> tokens;
	int start = 0;
	int end = 0;
	int ptr = 0;

	while (ptr != string::npos) {
		ptr = s.find_first_of(" ", start);

		if (ptr == string::npos) {
			end = s.length();
		}
		else {
			end = ptr;
		}

		tokens.push_back(atoi(s.substr(start, end - start).c_str()));

		start = end + 1;
	}

	return tokens;
}

void convertCharArrayToString(string &s, char *c) {
	int i = 0;

	while (c[i] != '\0') {
		s += c[i];

		i++;
	}
}

int recycle(string &a, string&b, int aint, int bint) {
	int count = 0;
	int start = 0;
	int end = 1;
	string c;
	int rc1 = 0;
	int rc2 = 0;


	for (int n = aint; n < bint; n++) {
		for (int m = n + 1; m <= bint; m++) {
			end = 1;

			if ((end) < a.length()) {
				char buffer[10];
				string s1;
				string s2;
				itoa(n, buffer, 10);
				convertCharArrayToString(s1, buffer);
				itoa(m, buffer, 10);
				convertCharArrayToString(s2, buffer);

				if (numberStringsSimilar(s1, s2)) {
					//cout << "index n = "<< n;
					//cout << ", index m = "<< m << endl;

					for (int i = 0; i < s1.length() - 1; i++) {
						c = s1.substr(s1.length() - end, end);
						//if (n == 2212 && m == 2221) cout << c << endl;
						//string d = s1.substr(start, s1.length() - end);
						c += s1.substr(start, s1.length() - end);
						//if (n == 2212 && m == 2221) cout << d << endl;
						//if (n == 2212 && m == 2221) cout << c << endl;

						//if (noLeadingZeros(c)) {
							rc1 = atoi(c.c_str());
						
							if (rc1 == m) {
								cout << "{"<< n << ", " << m << "}  =  " << rc1 << " < - > " << m << endl;
								count++;
							}
						//}

						end++;
					}
				}
			}
		}
	}

	return count;
}

bool stringsSimilar(string &a, string&b) {
	vector<char> av;
	vector<char> bv;

	for (int i = 0; i < a.length(); i++) {
		av.push_back(a[i]);
	}

	for (int i = 0; i < b.length(); i++) {
		bv.push_back(b[i]);
	}

	while ((av.size() > 0) || (bv.size() > 0)) {
		if ((av.size() == 0) || (bv.size() == 0)) return false;

		char c = a[0];
		bool hasC = false;
		int breakpoint = -1;

		for (int i = 0; i < bv.size(); i++) {
			if (c == bv[i]) {
				if (breakpoint < 0) {
					breakpoint = i;
					hasC = true;
				}
			}
		}

		if (!hasC) {
			return false;
		}
		else {
			av.erase(av.begin());
			bv.erase(bv.begin() + breakpoint);
		}
	}

	return true;
}

bool numberStringsSimilar(string &a, string &b) {
	int acount[10];
	int bcount[10];

	for (int i = 0; i < 10; i++) {
		acount[i] = 0;
		bcount[i] = 0;
	}

	for (int i = 0; i < a.length(); i++) {
		acount[a[i] - '0']++;
	}

	for (int i = 0; i < b.length(); i++) {
		bcount[b[i] - '0']++;
	}

	for (int i = 0; i < 10; i++) {
		if (!(acount[i] == bcount[i])) return false;
	}
	
	return true;
}

bool noLeadingZeros(string &s) {
	int i = 0;

	while (i < s.length()) {
		if (s[i] - '0' != 0) return true;
		else return false;
		i++;
	}

	return true;
}