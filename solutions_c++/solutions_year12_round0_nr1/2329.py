#include <iostream>
#include <string>
#include <cstring>
#include <sstream>

using namespace std;

char GtoE[256];

string translate(string google)
{
	for(int i=0; i < google.size(); ++i)
		google[i] = GtoE[google[i]];
	return google;
}


int main() {

	int T;
	cin >> T;

	memset(GtoE, ' ', sizeof(GtoE));

	GtoE['y'] = 'a';
	GtoE['n'] = 'b';
	GtoE['f'] = 'c';
	GtoE['i'] = 'd';
	GtoE['c'] = 'e';
	GtoE['w'] = 'f';
	GtoE['l'] = 'g';
	GtoE['b'] = 'h';
	GtoE['k'] = 'i';
	GtoE['u'] = 'j';
	GtoE['o'] = 'k';
	GtoE['m'] = 'l';
	GtoE['x'] = 'm';
	GtoE['s'] = 'n';
	GtoE['e'] = 'o';
	GtoE['v'] = 'p';
	GtoE['z'] = 'q';
	GtoE['p'] = 'r';
	GtoE['d'] = 's';
	GtoE['r'] = 't';
	GtoE['j'] = 'u';
	GtoE['g'] = 'v';
	GtoE['t'] = 'w';
	GtoE['h'] = 'x';
	GtoE['a'] = 'y';
	GtoE['q'] = 'z';

	string line;
	getline(cin,line);

	for(int t=0; t < T; ++t){
		getline(cin, line);
		cout << "Case #" << t+1 << ": " << translate(line) << endl;
	}

	return 0;
}


