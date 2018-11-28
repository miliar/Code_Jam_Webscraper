#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in("A.in");
	ofstream out("A.out");

	char mapping[26];

	for(int i = 0; i < 26; ++i)
		mapping[i] = '*';

	mapping[25] = 'q'; //from the hint
	mapping[16] = 'z'; //by inspection

	string sampleIn = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string sampleOut = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	for(int i = 0; i < sampleIn.length(); ++i)
		mapping[sampleIn[i] - 'a'] = sampleOut[i];

	/*for(int i = 0; i < 26; ++i)
		cout << (char)('a' + i) << " ";
	cout << endl;

	for(int i = 0; i < 26; ++i)
		cout << mapping[i] << " ";*/

	int T;
	in >> T >> ws;

	string line;
	for(int i = 0; i < T; ++i)
	{
		getline(in, line);
		out << "Case #" << i+1 << ": ";
		for(int j = 0; j < line.length(); ++j)
			if(line[j] == ' ')
				out << " ";
			else
				out << mapping[line[j] - 'a'];
		out << endl;
	}

	/*int a;
	cin >> a;*/
	return 0;
}