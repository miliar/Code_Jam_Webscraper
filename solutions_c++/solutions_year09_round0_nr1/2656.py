#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	int a, b, c, hits;
	string s, *dic, *exp;
	ifstream input;
	input.open ("A-large.in");

	input >> a >> b >> c;

	dic = new string[b];
	for (int i = 0; i < b; i++){
		input >> dic[i];
	}

	for (int no_exp = 0; no_exp < c; no_exp++){
		exp = new string[a];
		input >> s;
		int j = 0;
		for (int i = 0; i < s.length(); i++){
			if (s[i] == '(') {
				i++;
				while (s[i] != ')'){
					exp[j] += s[i];
					i++;
				}
			}
			else {
				exp[j] = s[i];
			}
			j++;
		}
		hits = 0;
		cout << "Case #" << no_exp + 1 << ": ";
		for (int word = 0; word < b; word++){
			int found = 0;
			for (int letter = 0; letter < a; letter++){
				if (exp[letter].find(dic[word][letter]) != string::npos)
					found ++;
				else
					break;
			}
			if (found == a)
				hits++;
		}
		cout << hits << endl;
	}

	input.close();
	return 0;
}
