#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// ynficwlbkuogxsevmpdrjgthaq = abcdefghijklmnopqrstuvwxyz
const char map[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 
	                'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 
			  	    'j', 'g', 't', 'h', 'a', 'q'};

int search(char c)
{
	for (int i = 0;i < 26;++i)
	{
		if (map[i] == c)
			return i;
	}

	return -1;
}

int main()
{
	ifstream in("E:\\GoogleCodeJam2012\\QRound\\A-small-attempt0.in");
	ofstream out("E:\\GoogleCodeJam2012\\QRound\\a-small-out.txt");

	if (in.is_open())
	{
		int lines;
		string s;

		in >> lines;

		getline(in, s);

		for (int i = 1;i <= lines;++i)
		{
			getline(in, s);

			for (int j = 0;j < (int)s.length();++j)
			{
				if (s[j] != ' ') s[j] = 'a' + search(s[j]);
			}

			out << "Case #" << i << ": " << s << endl;
		}
	}

	return 0;
}