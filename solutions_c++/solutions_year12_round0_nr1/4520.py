#include <iostream>
#include <fstream>
#include <string>
#include <cassert>

using namespace std;

const char *dic_input = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char *dic_output = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char gToEn[26];
const char *dic = "yhesocvxduiglbkrztnwjpfmaq";

string solve_a(string &str)
{
	string ret_str=str;
	for(int i=0; i<str.size(); i++) {
		if (str[i] != ' ') {
			ret_str[i] = dic[str[i]-'a'];
		}
	}
	return ret_str;
}

int main(int argc, char *argv[]) {
	int dic_len = strlen(dic_input);
	assert(strlen(dic_input) == strlen(dic_output));
	for(int i = 0; i<dic_len; i++) {
		gToEn[dic_input[i]-'a'] = dic_output[i];
	}
	for(int i=0; i<26; i++) {
		char c = i+'a';
		cout << c;
	}
	cout << std::endl;
	for(int i=0; i<26; i++) {
		char c = i+'a';
		cout << gToEn[i];
	}
	cout << std::endl;

	std::ifstream ifs(argv[1]);
	if (!ifs.is_open()) return -1;
	std::string ofilename = std::string(argv[1]) + ".out";
	std::ofstream ofs(ofilename.c_str());
	int num;
	ifs >> num;
	char buf[200];
	ifs.getline(buf, 200);
	for(int c=1; c<=num; c++) {
		ifs.getline(buf, 200);
		cout << "Solving " << c << std::endl;
		string ans = solve_a(string(buf));
		ofs << "Case #" << c << ": " << ans << std::endl;
	}

	return 0;
}
