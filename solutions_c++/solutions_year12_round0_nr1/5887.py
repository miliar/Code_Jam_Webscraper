#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>

using namespace std;

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
    is.open(argv[1]);

	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;

	char encr[] = "yhesocvxduiglbkrztnwjpfmaq";

	for(int i = 1; i <= tc; i++)
	{
		string out;
		cout << "Case #" << i << ": ";
		getline(is,s); 
		for (int i = 0; i < s.size(); ++i) {
		    if (s[i] == ' ') {
			    out += " ";
			}
		    else {
			    out += encr[s[i]-'a'];
			}
	    }
		cout << out << endl;
	}
	is.close();
	return 0;
}
