#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;
            //abcdefghijklmnopqrstuvwxyz q,z-?
char abc[] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in >> T;

	string t;
	getline(in, t);


	for (int i = 0; i < T; i++)
	{
		string s;
		getline(in, s);
		//alg begin
		transform(s.begin(), s.end(), s.begin(), [](char ch) -> char
		{
			char res = ch;
			if (res != ' ')
			{
				res = abc[res - 'a'];
			}
			return res;
		});
		//alg end

		//output
		out << "Case #" << i + 1 << ": " << s << "\n";
	}

	return 0;
}