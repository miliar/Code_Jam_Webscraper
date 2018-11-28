#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

int main()
{
	string e = "yhesocvxduiglbkrztnwjpfmaq";

	int T;
	fin >> T;
	string s;
	getline(fin, s); 
	for(int caseID=1; caseID<=T; caseID++) {
		getline(fin, s); 
		for(int i=0; i<s.size(); i++) {
			if(s[i]!=' ')
				s[i] = e[s[i]-'a'];
		}
		fout << "Case #" << caseID << ": ";
		fout << s << endl;
	}

	return 0;
}
