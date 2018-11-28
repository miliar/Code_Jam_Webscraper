#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

ifstream in("D:/JAM/B-small-attempt0.in");
ofstream out("D:/JAM/out.txt");

vector<char> solve_case(vector<string> comb, vector<string> ops, string input) 
{
	vector<char> v;
	int n = -1;

	for (int i = 0; i < input.size(); i++) {
		v.push_back(input[i]);
		n++;

		if (n >= 1) {
			for (int j = 0; j < comb.size(); j++) {
				if (v[n] == comb[j][0] && v[n - 1] == comb[j][1] || v[n] == comb[j][1] && v[n - 1] == comb[j][0]) {
					v.pop_back();
					v.pop_back();
					v.push_back(comb[j][2]);
					n--;
					break;
				} 
			}
		}
		
		for (int j = 0; j < ops.size(); j++) {
			for (int k = 0; k < v.size(); k++) {
				if (v[n] == ops[j][0] && v[k] == ops[j][1] || v[n] == ops[j][1] && v[k] == ops[j][0]) {
					v.clear();
					n = -1;
					break;
				}
			}
		}
	}

	return v;
	
}

int main() 
{
	int n_cases;
	in >> n_cases;
	for (int i = 1; i <= n_cases; i++) {
		vector<string> ops;
		vector<string> combs;
		string input;

		int n_combs;
		in >> n_combs;

		for (int j = 1; j <= n_combs; j++) {
			string comb;
			in >> comb;
			combs.push_back(comb);
		}

		int n_ops;
		in >> n_ops;

		for (int j = 1; j <= n_ops; j++) {
			string op;
			in >> op;
			ops.push_back(op);
		}

		in >> n_ops; //just to take the input that isnt used
		in >> input;
		vector<char> solution = solve_case(combs, ops, input);
		out << "Case #" << i << ": [";
		for (int i = 0; i < solution.size(); i++) {
			out << solution[i];
			if (i != solution.size() - 1) {
				out << ", ";
			}
		}

		out << "]" << endl;
	}
}



