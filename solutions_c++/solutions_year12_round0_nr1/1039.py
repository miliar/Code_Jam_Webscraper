#include <fstream>
#include <string>
using namespace std;
const char CODE[] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int t, i, l, j;
	string s;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	getline(fin, s);
	for(i = 1; i <= t; i++)
	{
		getline(fin, s);
		l = s.size();
		for(j = 0; j < l; j++)
			if(s[j] != ' ')
				s[j] = CODE[s[j] - 'a'];
		fout << "Case #" << i << ": " << s << endl;
	}
	return 0;
}