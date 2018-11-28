#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

enum inv {Q=0,W, E, R, A, S, D, F, OTHER};

inv char_to_inv(char c)
{
	switch (c) {
		case 'Q' : return Q;
		case 'W' : return W;
		case 'E' : return E;
		case 'R' : return R;
		case 'A' : return A;
		case 'S' : return S;
		case 'D' : return D;
		case 'F' : return F;
		default: return OTHER;
	}
}

char get_combine_rule(char n_char, char l_char, char rules[8][8])
{
	inv n, l;
	n = char_to_inv(n_char);
	l = char_to_inv(l_char);
	if (l == OTHER)
		return 0;
	return rules[n][l];
}

bool is_oppose_rule(char n_char, vector<char> &list, char rules[8][8])
{
	inv n, l;
	n = char_to_inv(n_char);
	for(int i = 0; i < list.size(); i++) {
		if ((l=char_to_inv(list[i])) == OTHER)
			continue;
		else if (rules[n][l] == -1)
			return true;
	}
	return false;
}

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
		char c_rules[8][8];
		char o_rules[8][8];
		cout << "test case " << test_cases_i+1 << endl;
		for(int i = 0; i < 8; i++)
			for(int j = 0; j < 8; j++) {
				c_rules[i][j] = 0;
				o_rules[i][j] = 0;
			}
		int num_combine_rules;
		fin >> num_combine_rules;
		for(int i = 0; i < num_combine_rules; i++) {
			char tmpa, tmpb, comb;
			fin >> tmpa >> tmpb >> comb;
			cout << "combine rule: " << tmpa << tmpb << comb << endl;
			inv a, b;
			a = char_to_inv(tmpa);
			b = char_to_inv(tmpb);
			c_rules[a][b] = comb;
			c_rules[b][a] = comb;
		}

		int num_opposed_rules;
		fin >> num_opposed_rules;
		for(int i = 0; i < num_opposed_rules; i++) {
			char tmpa, tmpb;
			fin >> tmpa >> tmpb;
			cout << "oppose rule: " << tmpa << tmpb << endl;
			inv a, b;
			a = char_to_inv(tmpa);
			b = char_to_inv(tmpb);
			o_rules[a][b] = -1;
			o_rules[b][a] = -1;
		}
		/*
		 * testing reading input - passed
		 * */
		/*
		{
		cout << "rules are" << endl;
		for(int i = 0; i < 8; i++) {
			for(int j = 0; j < 8; j++)
				if (rules[i][j]==-1)
					cout << '*' << '\t';
				else
					cout << rules[i][j] << '\t';
			cout << '\n';
		}
		}
		*/
		int num_invokes;
		fin >> num_invokes;
		string invokes;
		fin >> invokes;

		vector<char> result;
		char last_char;

		result.push_back(invokes[0]);
		last_char = invokes[0];
		for(int in_i = 1;in_i < num_invokes;in_i++) {
			char c = invokes[in_i];
			char tmp;
			if ((tmp=get_combine_rule(c, last_char, c_rules)) != 0) {
				result.pop_back();
				result.push_back(tmp);
				last_char = tmp;
			} else if (is_oppose_rule(c, result, o_rules)) {
				result.clear();
				last_char = 0;
			} else {
				result.push_back(c);
				last_char = c;
			}
		}
		cout << "result is ";
		for(int i = 0; i < result.size(); i++)
			cout << result[i] << '\t';
		cout << '\n';

		fout << "Case #" << test_cases_i+1 << ": [";
		for(int i = 0; i < result.size(); i++)
			if (i == result.size()-1)
				fout << result[i];
			else
				fout << result[i] << ", ";
		fout  << "]" << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
