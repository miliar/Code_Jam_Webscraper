#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>

//#include <cctype>
#include <cmath>

#include <fstream>

using namespace std;

class Googlerese
{
public:
	string translate(string s)
	{
		const char * dict = "yhesocvxduiglbkrztnwjpfmaq";

		int n = s.length();
		string out = s;
		for (int i = 0; i < n; i++)
		{
			out[i]=dict[s[i]-'a'];
		}

		return out;
	}

};

//----------------------------------------------------------//
int main(int argc, char *argv[])
{
	if (argc < 2) {cout << "wrong input" << endl;return 0;}
	Googlerese g;
	//g.init();

	ifstream infile;
	infile.open(argv[1]);
	int n = 0;
	if (infile.is_open())
	{
		char cc[200] = {0};
		infile.getline(cc,150,'\n');
		n = atoi(cc);

		string line;
		int i = 1;
		while (i<=n)
		{
			char cc[200] = {0};
			infile.getline(cc,150,'\n');
			line = string(cc);

			cout << "Case #" << i << ": " << g.translate(line) << endl;
			i++;
		}
	}

	return 0;

}
