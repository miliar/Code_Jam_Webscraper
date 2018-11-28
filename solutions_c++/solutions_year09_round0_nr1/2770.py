#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int len, count, cases;
	in >> len >> count >> cases;
	getline(in, string());

	vector<string> tokens(count);
	for(int i = 0; i < count; i++)
		getline(in, tokens[i]);

	for(int i = 0; i < cases; i++){
		vector<string> word(len);
		int open = 0;
		int index = 0;
		string line;
		getline(in, line);
		const char *p = line.c_str();
		while(*p != 0){
			if(*p == '('){
				open++;
				p++;
				continue;
			}else if(*p == ')'){
				open--;
				p++;
				index++;
				continue;
			}
			if(open) word[index] += *p;
			else word[index++] = *p;
			p++;
		}

		int found = 0;
		
		for(int i = 0; i < count; i++){
			bool match = true;
			for(int j = 0; j < len; j++){
				match = match && (word[j].find(tokens[i][j]) != string::npos);
				if(!match) break;
			}
			if(match) found++;
		}
		out << "Case #" << i+1 << ": " << found << endl;
	}

}